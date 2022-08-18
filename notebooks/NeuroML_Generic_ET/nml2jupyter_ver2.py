import os
import ipywidgets
import ui_widget
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from pyneuroml import pynml

#python helper class for updating NeuroML files and running it from Jupyter Notebook
class nml2jupyter():
    
    def __init__(self, path2source, fname_LEMS):
        
        self.path2source      = path2source
        self.fname_LEMS       = fname_LEMS
        self.filelist         = []       #empty list
        self.nmlOutput        = {}       #empty dictionary
        
    #function to get list of  filenames from LEMS and all subsequent files
    def getFileList(self,filename,filelist_local):
        
        filelist_local.append(filename)              #add current file to filelist
        pathfilename=os.path.join(self.path2source, filename)
        root = ET.parse(pathfilename).getroot()
        
        #parse current file for tag names 'include' and append included files in filelist
        for child in root:
            tag_name=child.tag.split("}")[-1]        #spliting to remove namespace, if any
            if(tag_name.lower()=='include'):         #case insensitive search for keyword include
                for key, val in child.attrib.items():
                    if val.endswith('.nml') and val not in filelist_local:           #looking for filenames ending with .nml
                            filelist_local=self.getFileList(val,filelist_local)
        return filelist_local
    
    #function to parse NeuroML files
    def parseNML(self):
        
        #get all the filenames
        self.filelist=self.getFileList(self.fname_LEMS,[])
        
        #get tree for each of the .nml files
        tree=[]
        for file in self.filelist:
            filename=os.path.join(self.path2source, file)
            tree.append(ET.parse(filename))
            
        #registering namespace as blank space (some user tag can also be used)
        ET.register_namespace("","http://www.neuroml.org/schema/neuroml2")
        #ns = {"xmlns":"http://www.neuroml.org/schema/neuroml2"}
        
        return tree
    
    #function to cerate accordion widgets for given root of the xml/nml file
    def createAccordions(self,root):
        
        subwidget_list=[]  #list of subwidgets inside the accordion
        tags=[]            #tags from xml file to be used as accordion tittle
        
        #iterate through each child element to create subwidgets
        for child in root:
            
            tag_name=child.tag.split("}")[-1]        #spliting to remove namespace, if any
            tags.append(tag_name)
            textBox_list = []
            
            #iterate through each attribute of the child element
            for key, val in child.attrib.items():
                    textBox_key   = ipywidgets.Text(value=key,disabled=True,layout=ipywidgets.Layout(width='10%'))
                    textBox_value = ipywidgets.Text(value=val,layout=ipywidgets.Layout(width='40%'))
                    textBox_list.append(ipywidgets.HBox([textBox_key, textBox_value]))
            
            #for notes tag display a textarea and show text as attributes will be empty
            if tag_name=='notes':
                textBox_list.append(ipywidgets.Textarea(value=child.text,layout=ipywidgets.Layout(width='50%')))
            
            #check if grand child exist
            if child:
                #if grand child exist then recursive call to self with root <---> child
                child_accord=self.createAccordions(child)
                textBox_list.append(child_accord)  #append the chlild accordion to parent

            subwidget_list.append(ipywidgets.VBox(textBox_list)) #append sub widgets to the current accordion

        #create accordion widget for the captured subwidgets
        accordion = ipywidgets.Accordion(children=subwidget_list, selected_index=None)
        #set title using tags (xml namespace ignored)
        for i in range(len(tags)):
            accordion.set_title(i, tags[i])
            
        return accordion
        
    #Function to generate basic dashboard with tabs and accordions
    def generateDashboard(self,trees):
       
        tab_list=[]          #creating empty tab list
        for tree in trees:
            root = tree.getroot()
            tab_list.append(self.createAccordions(root))        #add accordions to the tab list
        
        #create a nested tab with accordions
        
        tab_nest = ipywidgets.Tab()
        #create tab headers from filenames
        for i in range(len(tab_list)):
            tab_nest.set_title (i, self.filelist[i])
        
        #set content to tabs
        tab_nest.children = tab_list
        display(tab_nest)
        
    #function to update existing NeuroML file based on widget inputs
    def writeNMLinputFile(self,C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, t_0, t_n, delta_t, I_inj_max, I_inj_width, I_inj_trans):
        print('will do later')
        
    #function to setup full dashboard/gui
    def loadGUI(self):
        
        #function to run NeuroML with given inputs
        def runNMLmodel(b):
            out_log.clear_output()
            out_plot.clear_output()
            with out_log:
                LEMS_file=os.path.join(self.path2source, self.fname_LEMS)
                self.nmlOutput = pynml.run_lems_with_jneuroml(LEMS_file, nogui=True, load_saved_data=True)
                #shell_cmd=['pynml', LEMS, LEMSoption]
                #subprocess.run(shell_cmd)
        
        #function to validate NeuroML model
        def validateNMLmodel(b):
            out_log.clear_output()
            with out_log:
                for file in self.filelist:
                    if(file.endswith('.nml')):
                        pathfilename=os.path.join(self.path2source, file)
                        something=pynml.validate_neuroml2(pathfilename)
                        #shell_cmd=['pynml', pathfilename,'-validate']
                        #subprocess.run(shell_cmd)
                        
        #function to display plot in notebook
        def plotOutput(b):
            out_plot.clear_output()
            with out_plot:
                self.plotData()
                        
        #output windows
        out_log = ipywidgets.Output(layout={'border': '1px solid'}) #for displaying output log from NeuroMl execution
        out_plot = ipywidgets.Output()                              #for displaying plots    
        
        ui_widget.run_button.on_click(runNMLmodel)
        ui_widget.validate_button.on_click(validateNMLmodel)
        ui_widget.plot_button.on_click(plotOutput)

        display(ui_widget.buttons,out_log,ui_widget.plot_button,out_plot)
    
    #function to plot data generated by NeuroML
    def plotData(self):
        plt.close('all')
        for key in self.nmlOutput.keys():
                    if key == "t":
                        continue
                    fig=plt.figure(figsize=(8,2))
                    fig.canvas.header_visible = False
                    
                    htmlBox_tittle    = ipywidgets.HTML(value='<b><p style="text-align:center">{}</p></b>'.format(key),layout=ipywidgets.Layout(border='solid 1px black',width='60%'))
                    plt.xlabel("Time (ms)")
                    plt.ylabel("")
                    plt.grid(True,linestyle="--")
                    
                    plt.xlim(min(self.nmlOutput["t"]),max(self.nmlOutput["t"]))
                    plt.ylim(min(self.nmlOutput[key]),max(self.nmlOutput[key]))
                    
                    plt.plot(self.nmlOutput["t"], self.nmlOutput[key], linewidth=1)
                    
                    plotBox=ipywidgets.VBox([htmlBox_tittle,fig.canvas],layout=ipywidgets.Layout(justify_content='center'))
                    
                    display(plotBox)
#end of class