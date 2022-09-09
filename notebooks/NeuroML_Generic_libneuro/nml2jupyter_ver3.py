import pylab as plt
import numpy as np
import os
import ipywidgets
from pyneuroml import pynml
from neuroml.loaders import read_neuroml2_file

#python helper class for updating NeuroML files and running it from Jupyter Notebook
class nml2jupyter():
    
    def __init__(self, path2source, fname_LEMS, fname_net):
        
        self.path2source   = path2source
        self.fname_LEMS    = fname_LEMS
        self.fname_net     = fname_net
    
    def loadnml(self):
        pathfilename=os.path.join(self.path2source, self.fname_net)
        nml_doc= read_neuroml2_file(pathfilename, include_includes=True)
        return nml_doc

    def createGUI(self,actMemDict):

        masterTab=ipywidgets.Tab()
        masterTab_titles=[]
        masterTab_child=[]

        for key,values in actMemDict.items():
            subTab=ipywidgets.Tab()
            child=[]
            for i in range(len(values)):
                child.append(ipywidgets.Text(value='member details here'))
            subTab.children=child
            for i in range(len(values)):
                subTab.set_title(i,values[i])
            masterTab_child.append(subTab)
            masterTab_titles.append(key)

        masterTab.children=masterTab_child
        for i in range(len(masterTab_titles)):
            masterTab.set_title(i,masterTab_titles[i])
        display(masterTab)


    def summary_mod(self, nml_doc, show_includes=True, show_non_network=True):
        """Get a pretty-printed summary of the complete NeuroMLDocument.
        This includes information on the various Components included in the
        NeuroMLDocument: networks, cells, projections, synapses, and so on.
        """
        import inspect
        info = "*******************************************************\n"
        info+="* NeuroMLDocument: "+nml_doc.id+"\n*\n"
        post = ""
        membs = inspect.getmembers(nml_doc)
        activeMemb={}
        for memb in membs:
            if isinstance(memb[1], list) and len(memb[1])>0 and not memb[0].endswith('_') and not memb[0] == 'networks':
                if (memb[0] == 'includes' and show_includes) or (not memb[0] == 'includes' and show_non_network):
                    post = "*\n"
                    info+="*  "+str(memb[1][0].__class__.__name__)+": "
                    listed = []
                    for entry in memb[1]:
                        if hasattr(entry,'id'):
                            listed.append(str(entry.id))
                        elif hasattr(entry,'name'):
                            listed.append(str(entry.name))
                        elif hasattr(entry,'href'):
                            listed.append(str(entry.href))
                        elif hasattr(entry,'tag'):
                            listed.append(str(entry.tag)+" = "+str(entry.value))
                    info+= str(sorted(listed))+"\n"
                    activeMemb[memb[1][0].__class__.__name__]=listed
        info+= post
        for network in nml_doc.networks:
            info+="*  Network: "+network.id
            if network.temperature:
                info+=" (temperature: "+network.temperature+")"
            info+="\n*\n"
            tot_pop =0
            tot_cells = 0
            pop_info = ""
            for pop in sorted(network.populations, key=lambda x: x.id):
                pop_info+="*     "+str(pop)+"\n"
                tot_pop+=1
                tot_cells+=pop.get_size()
                if len(pop.instances)>0:
                    loc = pop.instances[0].location
                    pop_info+="*       Locations: ["+str(loc)+", ...]\n"
                if len(pop.properties)>0:
                    pop_info+="*       Properties: "
                    for p in pop.properties:
                        pop_info+=(str(p.tag)+'='+str(p.value)+'; ')
                    pop_info+="\n"
            info+="*   "+str(tot_cells)+" cells in "+str(tot_pop)+" populations \n"+pop_info+"*\n"
            tot_proj =0
            tot_conns = 0
            proj_info = ""
            for proj in sorted(network.projections, key=lambda x: x.id):
                proj_info+="*     "+str(proj)+"\n"
                tot_proj+=1
                tot_conns+=len(proj.connections)
                tot_conns+=len(proj.connection_wds)
                if len(proj.connections)>0:
                    proj_info+="*       "+str(len(proj.connections))+" connections: [("+str(proj.connections[0])+"), ...]\n"
                if len(proj.connection_wds)>0:
                    proj_info+="*       "+str(len(proj.connection_wds))+" connections (wd): [("+str(proj.connection_wds[0])+"), ...]\n"
            for proj in sorted(network.electrical_projections, key=lambda x: x.id):
                proj_info+="*     Electrical projection: "+proj.id+" from "+proj.presynaptic_population+" to "+proj.postsynaptic_population+"\n"
                tot_proj+=1
                tot_conns+=len(proj.electrical_connections)
                tot_conns+=len(proj.electrical_connection_instances)
                tot_conns+=len(proj.electrical_connection_instance_ws)
                if len(proj.electrical_connections)>0:
                    proj_info+="*       "+str(len(proj.electrical_connections))+" connections: [("+str(proj.electrical_connections[0])+"), ...]\n"
                if len(proj.electrical_connection_instances)>0:
                    proj_info+="*       "+str(len(proj.electrical_connection_instances))+" connections: [("+str(proj.electrical_connection_instances[0])+"), ...]\n"
                if len(proj.electrical_connection_instance_ws)>0:
                    proj_info+="*       "+str(len(proj.electrical_connection_instance_ws))+" connections: [("+str(proj.electrical_connection_instance_ws[0])+"), ...]\n"
            for proj in sorted(network.continuous_projections, key=lambda x: x.id):
                proj_info+="*     Continuous projection: "+proj.id+" from "+proj.presynaptic_population+" to "+proj.postsynaptic_population+"\n"
                tot_proj+=1
                tot_conns+=len(proj.continuous_connections)
                tot_conns+=len(proj.continuous_connection_instances)
                tot_conns+=len(proj.continuous_connection_instance_ws)
                if len(proj.continuous_connections)>0:
                    proj_info+="*       "+str(len(proj.continuous_connections))+" connections: [("+str(proj.continuous_connections[0])+"), ...]\n"
                if len(proj.continuous_connection_instances)>0:
                    proj_info+="*       "+str(len(proj.continuous_connection_instances))+" connections: [("+str(proj.continuous_connection_instances[0])+"), ...]\n"
                if len(proj.continuous_connection_instance_ws)>0:
                    proj_info+="*       "+str(len(proj.continuous_connection_instance_ws))+" connections (w): [("+str(proj.continuous_connection_instance_ws[0])+"), ...]\n"
            info+="*   "+str(tot_conns)+" connections in "+str(tot_proj)+" projections \n"+proj_info+"*\n"
            if len(network.synaptic_connections)>0:
                info+="*   "+str(len(network.synaptic_connections))+" explicit synaptic connections (outside of projections)\n"
                for sc in network.synaptic_connections:
                    info+="*     "+str(sc)+"\n"
                info+="*\n"
            tot_input_lists = 0
            tot_inputs = 0
            input_info = ""
            for il in sorted(network.input_lists, key=lambda x: x.id):
                input_info+="*     "+str(il)+"\n"
                tot_input_lists += 1
                if len(il.input)>0:
                    input_info+="*       "+str(len(il.input))+" inputs: [("+str(il.input[0])+"), ...]\n"
                    tot_inputs+=len(il.input)
                if len(il.input_ws)>0:
                    input_info+="*       "+str(len(il.input_ws))+" inputs: [("+str(il.input_ws[0])+"), ...]\n"
                    tot_inputs+=len(il.input_ws)
            info+="*   "+str(tot_inputs)+" inputs in "+str(tot_input_lists)+" input lists \n"+input_info+"*\n"
            if len(network.explicit_inputs)>0:
                info+="*   "+str(len(network.explicit_inputs))+" explicit inputs (outside of input lists)\n"
                for el in network.explicit_inputs:
                    info+="*     "+str(el)+"\n"
                info+="*\n"
        info+="*******************************************************"
        return info,activeMemb

    #function to plot data generated by NeuroML
    def plotData(self,fname_NML_output):

        #read data file and import columns as array using numpy
        data = np.loadtxt(fname_NML_output)
        t=data[:,0]*1000    #convert to ms
        V=data[:,1]*1000    #convert to mV
        m=data[:,2]
        h=data[:,3]
        n=data[:,4]
        ina=data[:,5]
        ik=data[:,6]
        il=data[:,7]
        i_inj1=data[:,8]*10**9 #convert to nA
        i_inj2=data[:,9]*10**9 #convert to nA

        plt.rcParams['figure.figsize'] = [12, 8]
        plt.rcParams['font.size'] = 15
        plt.rcParams['legend.fontsize'] = 12
        plt.rcParams['legend.loc'] = "upper right"

        fig=plt.figure()

        ax1 = plt.subplot(4,1,1)
        plt.xlim([np.min(t),np.max(t)])  #for all subplots
        plt.title('Hodgkin-Huxley Neuron')
        #i_inj_values = [self.I_inj(t) for t in t]
        plt.plot(t, i_inj1, 'k')
        plt.plot(t, i_inj2, 'b')
        plt.ylabel('$I_{inj}$ (nA)')      

        plt.subplot(4,1,2, sharex = ax1)
        plt.plot(t, ina, 'c', label='$I_{Na}$')
        plt.plot(t, ik, 'y', label='$I_{K}$')
        plt.plot(t, il, 'm', label='$I_{L}$')
        plt.ylabel('Current')
        plt.legend()

        plt.subplot(4,1,3, sharex = ax1)
        plt.plot(t, m, 'r', label='m')
        plt.plot(t, h, 'g', label='h')
        plt.plot(t, n, 'b', label='n')
        plt.ylabel('Gating Value')
        plt.legend()

        plt.subplot(4,1,4, sharex = ax1)
        plt.plot(t, V, 'k')
        plt.ylabel('V (mV)')
        plt.xlabel('t (ms)')
        #plt.ylim(-1, 40)

        plt.tight_layout()
        plt.show()
#end of class