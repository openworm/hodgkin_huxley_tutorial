import os
import pylab as plt
import numpy as np
import ui_widget
import ipywidgets
from pyneuroml import pynml
from neuroml.loaders import read_neuroml2_file
import neuroml.writers as writers

#python helper class for updating NeuroML files and running it from Jupyter Notebook
class nml2jupyter():
    
    def __init__(self, path2source, fname_LEMS, fname_net):
        
        self.path2source   = path2source
        self.fname_LEMS    = fname_LEMS
        self.fname_net     = fname_net
        self.nml_file      = 'NeuroMLProject.nml'
    
    #Function to load neuroml file in python object
    def loadnml(self):
        pathfilename=os.path.join(self.path2source, self.fname_net)
        nml_doc= read_neuroml2_file(pathfilename, include_includes=True,already_included=[])
        return nml_doc

    #function to write NeuroML file based on widget inputs
    def writeNMLinputFile(self,nml_doc):
        writers.NeuroMLWriter.write(nml_doc, self.nml_file)
        display("Written in NeuroML2 format to : " + self.nml_file)
                

    #Fuction to create accordions for given neuroml object
    def createAccordions(self,nmlObj,title):
        mydict=nmlObj.info(True,return_format='dict')
        emptyKeys=[]
        subwidget_list=[]
        textBoxList=[]
        
        #Two loops to keep text boxes on top and accordion on bottom
        #Need to find alternate way to avoid looping twice
        
        #Loop 1 
        #create text box widgets for values of dictionary of type str, int or float
        #make a list of empty keys
        for key,values in mydict.items():
            # check if the member is set to None
            # if it's a container (list), it will not be set to None, it
            # will be empty, []
            # if it's a scalar, it will be set to None or to a non
            # container value
            if values['members'] is None or (isinstance(values['members'], list) and len(values['members']) == 0): 
                emptyKeys.append(key)
                continue
            if isinstance(values['members'],str) or isinstance(values['members'],int) or isinstance(values['members'],float):
                textBox_key   = ipywidgets.Text(value=key,disabled=True,layout=ipywidgets.Layout(width='20%'))
                textBox_value = ipywidgets.Text(value=str(values['members']),layout=ipywidgets.Layout(width='50%'))
                textBoxList.append(ipywidgets.HBox([textBox_key, textBox_value]))
                if (key=='id'): title_id=values['members']
        
        #remove empty keys from dicitonary (to reduce iteration in 2nd loop)
        for key in emptyKeys:
            mydict.pop(key)
        
        #Loop 2
        #create sub-accordions for list of values
        for key,values in mydict.items():
            if isinstance(values['members'],str) or isinstance(values['members'],int) or isinstance(values['members'],float): continue
            if isinstance(values['members'],list):
                for idx, val in enumerate(values['members']):
                    if isinstance(val,str) or isinstance(val,int) or isinstance(val,float): 
                        textBox_key   = ipywidgets.Text(value=key,disabled=True,layout=ipywidgets.Layout(width='20%'))
                        textBox_value = ipywidgets.Text(value=str(val),layout=ipywidgets.Layout(width='50%'))
                        textBoxList.append(ipywidgets.HBox([textBox_key, textBox_value]))
                        if (key=='id'): title_id=values['members']
                    else:
                        child_accord=self.createAccordions(val,key)
                        textBoxList.append(child_accord)
            else:
                child_accord=self.createAccordions(values['members'],key)
                textBoxList.append(child_accord)
        
        subwidget_list.append(ipywidgets.VBox(textBoxList))
        accordion = ipywidgets.Accordion(children=subwidget_list, selected_index=None)
        try: 
            title_with_id = title + ' (' + title_id + ') '
            accordion.set_title(0, title_with_id)
        except:
            accordion.set_title(0, title)
        
        return accordion

    #Function to load LEMS life in python object then get component list to create accordions   
    def createAccordionsLEMS(self):
        pathfilename=os.path.join(self.path2source,self.fname_LEMS)
        lems_doc=pynml.read_lems_file(pathfilename)
        mydict=lems_doc.get_component_list()
        accordList=[]
        component=['id', 'type', 'parameters', 'parent_id']
        for key,values in mydict.items():
            textBoxList=[]
            for attr in component:
                val = getattr(mydict[key],attr)
                if isinstance(val,dict):
                    for k,v in val.items():
                        textBox_key   = ipywidgets.Text(value=k,disabled=True,layout=ipywidgets.Layout(width='20%'))
                        textBox_value = ipywidgets.Text(value=v,layout=ipywidgets.Layout(width='50%'))
                        textBoxList.append(ipywidgets.HBox([textBox_key, textBox_value]))
                    continue
                textBox_key   = ipywidgets.Text(value=attr,disabled=True,layout=ipywidgets.Layout(width='20%'))
                textBox_value = ipywidgets.Text(value=val,layout=ipywidgets.Layout(width='50%'))
                textBoxList.append(ipywidgets.HBox([textBox_key, textBox_value]))
            accordList.append(ipywidgets.VBox(textBoxList))
        accordion = ipywidgets.Accordion(children=accordList, selected_index=None)
        for i,key in enumerate(mydict.keys()):
            accordion.set_title(i,key)
        return accordion

    #Function to create GUI by nesting accordions with first level of neruoml object as Tabs
    def createTabWithAccordions(self,nml_doc):
        parent=nml_doc.info(True,return_format='dict')
        
        masterTab=ipywidgets.Tab()
        masterTab_titles=[]
        masterTab_child=[]
        #create LEMS tab for simulation parameters (using get_component_list) 
        lemsTab=self.createAccordionsLEMS()
        masterTab_child.append(lemsTab)
        masterTab_titles.append('LEMS')
        for key,values in parent.items():
            if values['members'] is None or (isinstance(values['members'], list) and len(values['members']) == 0): continue   #skip empty elements
            
            sub_child=[]
            if isinstance(values['members'],list):
                for val in values['members']:
                    sub_child.append(self.createAccordions(val,key))
            elif isinstance(values['members'],str) or isinstance(values['members'],int) or isinstance(values['members'],float): 
                sub_child.append(ipywidgets.Text(value=str(values['members'])))
            else:
                sub_child.append(self.createAccordions(values['members'],key))
            
            masterTab_child.append(ipywidgets.VBox(sub_child))
            masterTab_titles.append(key)

        masterTab.children=masterTab_child
        for i in range(len(masterTab_titles)):
            masterTab.set_title(i,masterTab_titles[i])

        display(masterTab)

    #function to setup full dashboard/gui
    def loadGUI(self,nml_doc):
        
        #function to run NeuroML with given inputs
        def runNMLmodel(b):
            out_log.clear_output()
            out_plot.clear_output()
            out_validStatus.clear_output()
            with out_log:
                display('Running NeuroML Model...')
                LEMS_file=os.path.join(self.path2source, self.fname_LEMS)
                self.nmlOutput = pynml.run_lems_with_jneuroml(LEMS_file, nogui=True, load_saved_data=True)
                #shell_cmd=['pynml', LEMS, LEMSoption]
                #subprocess.run(shell_cmd)
                display('Completed !!!')
        
        #function to validate NeuroML model
        def validateNMLmodel(b):
            out_log.clear_output()
            out_validStatus.clear_output()
            with out_log:
                display('Validating NeuroML Input File...')
                #pathfilename=os.path.join(self.path2source, self.nml_file)
                checkStatus=pynml.validate_neuroml2(self.nml_file)
                #shell_cmd=['pynml', pathfilename,'-validate']
                #subprocess.run(shell_cmd)
                if checkStatus==True:
                    valid_widget=ipywidgets.Valid(value=True,description='')
                    with out_validStatus:
                        display(ipywidgets.HBox([ipywidgets.HTML(value=self.nml_file,disabled=True),valid_widget]))
                else:
                    valid_widget=ipywidgets.Valid(value=False,description='')
                    with out_validStatus:
                        display(ipywidgets.HBox([ipywidgets.HTML(value=self.nml_file,disabled=True),valid_widget]))
                display('Completed !!!')
                        
        #function to display plot in notebook
        def plotOutput(b):
            out_plot.clear_output()
            with out_plot:
                self.plotData()
        
        #function to update NeuroML files from widget inputs
        def updateNMLfiles(b):
            out_log.clear_output()
            out_plot.clear_output()
            out_validStatus.clear_output()
            with out_log:
                #display('Updating NeuroML Files from GUI inputs...')
                display('Writing NeuroML python model to file ')
                #display(type(self.filelist),len(self.filelist))
                #display(type(self.trees),len(self.trees))
                self.writeNMLinputFile(nml_doc)
                display('Completed !!!')
                        
        #output windows
        out_log  = ipywidgets.Output(layout={'border': '1px solid'}) #for displaying output log from NeuroMl execution
        out_plot = ipywidgets.Output()                              #for displaying plots
        out_validStatus = ipywidgets.Output()                       #for displaying valid widgets after running validate button
        
        ui_widget.run_button.on_click(runNMLmodel)
        ui_widget.validate_button.on_click(validateNMLmodel)
        ui_widget.plot_button.on_click(plotOutput)
        ui_widget.update_button.on_click(updateNMLfiles)
        
        display(ui_widget.buttons,out_validStatus,out_log,ui_widget.plot_button,out_plot)
    
    #function to plot data generated by NeuroML
    def plotData(self):
        plt.close('all')
        for key in self.nmlOutput.keys():
                if key == "t":
                    continue
                plt.ioff()                 #suppress plot console window (plot only at display call)
                fig=plt.figure(figsize=(8,2))
                fig.canvas.header_visible = False

                htmlBox_tittle    = ipywidgets.HTML(value='<b><p style="text-align:center">{}</p></b>'.format(key),layout=ipywidgets.Layout(border='solid 1px black',width='60%'))
                plt.xlabel("Time (ms)")
                plt.ylabel("")
                plt.grid(True,linestyle="--")

                #plt.xlim(min(self.nmlOutput["t"]),max(self.nmlOutput["t"]))
                #plt.ylim(min(self.nmlOutput[key]),max(self.nmlOutput[key]))

                plt.plot(self.nmlOutput["t"], self.nmlOutput[key], linewidth=1)

                plotBox=ipywidgets.VBox([htmlBox_tittle,fig.canvas])

                display(plotBox)
#end of class