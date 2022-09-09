import ipywidgets

#define interactive textboxes for loading source path and LEMS filename
def loadpath(sourcePath, LEMS_file, net_file):
    return sourcePath, LEMS_file, net_file

sourcePath_tb  = ipywidgets.Text(value='../../Tutorial/Source/',placeholder='Path to NeuroML Source Dirctory',description='Path:',disabled=False,layout=ipywidgets.Layout(width='80%'))
LEMS_file_tb   = ipywidgets.Text(value='LEMS_HH_Simulation.xml',placeholder='LEMS Filename',description='LEMS:',disabled=False,layout=ipywidgets.Layout(width='80%'))
network_file_tb   = ipywidgets.Text(value='HHCellNetwork.net.nml',placeholder='Network Filename',description='Network:',disabled=False,layout=ipywidgets.Layout(width='80%'))

header = ipywidgets.HTML(value="<font size='+2'><i>Enter Path to NeuroML Model and LEMS filename below: </i></font>")
loader = ipywidgets.interactive(loadpath, sourcePath=sourcePath_tb, LEMS_file=LEMS_file_tb, net_file=network_file_tb)

#define run button
update_button = ipywidgets.Button(description="Update Model",button_style='info',tooltip='Update NeuroML file with current widget inputs')

#define run button
run_button = ipywidgets.Button(description="Run NeuroML",button_style='info',tooltip='Execute NeuroML Model with saved inputs')

#define validate button
validate_button = ipywidgets.Button(description="Validate Model",button_style='warning',tooltip='Validate NeuroML Model for above inputs')

#arrange run and validate button in a row
buttons=ipywidgets.HBox([update_button,validate_button, run_button])

#define plot button
plot_button = ipywidgets.Button(description="Plot Output",button_style='success',tooltip='Plot outputs recorded in LEMS file')