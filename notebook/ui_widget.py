import ipywidgets

header_capacitance = ipywidgets.HTML(value=f"<b><font color='blue'>Membrane Capacitance, uF/cm^2</b>")
header_conductance = ipywidgets.HTML(value=f"<b><font color='blue'>Maximum Conductances, mS/cm^2</b>")
header_potential   = ipywidgets.HTML(value=f"<b><font color='blue'>Nernst Reverasal Potentials, mV</b>")
header_simTime     = ipywidgets.HTML(value=f"<b><font color='blue'>Simulation Time, ms</b>")
slider_capacitance = ipywidgets.FloatSlider(value=1,min=0,max=3,step=0.1,description='Capacitance',readout_format='.1f',continuous_update=False)
slider_cond_Na     = ipywidgets.FloatSlider(value=120,min=80,max=160,step=0.1,description='Sodium',readout_format='.1f',continuous_update=False)
slider_cond_K      = ipywidgets.FloatSlider(value=36,min=0,max=80,step=0.1,description='Potassium',readout_format='.1f',continuous_update=False)
slider_cond_L      = ipywidgets.FloatSlider(value=0.3,min=0,max=1,step=0.1,description='Leak',readout_format='.1f',continuous_update=False)
slider_pot_Na      = ipywidgets.FloatSlider(value=50,min=-100,max=100,step=0.1,description='Sodium',readout_format='.1f',continuous_update=False)
slider_pot_K       = ipywidgets.FloatSlider(value=-77,min=-100,max=100,step=0.1,description='Potassium',readout_format='.1f',continuous_update=False)
slider_pot_L       = ipywidgets.FloatSlider(value=-54.387,min=-100,max=100,step=0.1,description='Leak',readout_format='.1f',continuous_update=False)
time_start         = ipywidgets.FloatText(value=0,description='Start Time',disabled=True)
time_end           = ipywidgets.FloatText(value=450,description='Total Time',disabled=False)
time_step          = ipywidgets.FloatText(value=0.01,description='Time Step',disabled=False)

def resetTodefault(_):
    slider_capacitance.value = 1
    slider_cond_Na.value     = 120
    slider_cond_K.value      = 36
    slider_cond_L.value      = 0.3
    slider_pot_Na.value      = 50
    slider_pot_K.value       = -77
    slider_pot_L.value       = -54.387
    time_start.value         = 0
    time_end.value           = 450
    time_step.value          = 0.01

reset_button = ipywidgets.Button(description="Reset All")
reset_button.on_click(resetTodefault)

h1=ipywidgets.HBox([header_capacitance])
h2=ipywidgets.HBox([slider_capacitance])
h3=ipywidgets.HBox([header_conductance])
h4=ipywidgets.HBox([slider_cond_Na,slider_cond_K,slider_cond_L])
h5=ipywidgets.HBox([header_potential])
h6=ipywidgets.HBox([slider_pot_Na,slider_pot_K,slider_pot_L])
h7=ipywidgets.HBox([header_simTime])
h8=ipywidgets.HBox([time_start,time_end,time_step])
h9=ipywidgets.HBox([reset_button])
v1=ipywidgets.VBox([h1,h2,h3,h4,h5,h6,h7,h8,h9])