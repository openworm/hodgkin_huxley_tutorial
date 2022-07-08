import ipywidgets
import numpy as np
import pylab as plt

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
    slider_amplitude.value   = 50
    slider_width.value       = 0
    slider_translation.value = 50
    
#function to change slider handle colour when move from default
def highlight_slider():
    inputList    = [slider_capacitance, slider_cond_Na, slider_cond_K, slider_cond_L, slider_pot_Na, slider_pot_K, slider_pot_L]
    inputDefault = [1.0, 120, 36, 0.3, 50, -77, -54.387]
    for l, d in zip(inputList,inputDefault):
        if l.value == d:
            l.style.handle_color = 'white'
        else:
            l.style.handle_color = 'orange'
    if slider_width.value == 0.0:
        slider_amplitude.style.handle_color = 'white'
        slider_width.style.handle_color = 'white'
        slider_translation.style.handle_color = 'white'
    else:
        slider_amplitude.style.handle_color = 'orange'
        slider_width.style.handle_color = 'orange'
        slider_translation.style.handle_color = 'orange'
            
header_capacitance = ipywidgets.HTMLMath(value=r"<b><font color='blue'>Membrane Capacitance, \(\mu{F}/cm^2\)</b>")
header_conductance = ipywidgets.HTMLMath(value=r"<b><font color='blue'>Maximum Conductances, \(mS/cm^2\)</b>")
header_potential   = ipywidgets.HTMLMath(value=r"<b><font color='blue'>Nernst Reverasal Potentials, \(mV\)</b>")
header_simTime     = ipywidgets.HTMLMath(value=r"<b><font color='blue'>Simulation Time, \(ms\)</b>")
header_injCurrent  = ipywidgets.HTMLMath(value=r"<b><font color='blue'>Injection Current, \(\mu{A}/cm^2\)</b>")
injCurrent_note    = ipywidgets.HTML(value=f"<i>*For injection current width = 0, the model uses default two pulse signal from tutorial</i>")
slider_capacitance = ipywidgets.FloatSlider(value=1,min=0,max=3,step=0.1,description='Capacitance',readout_format='.1f',continuous_update=False)
slider_cond_Na     = ipywidgets.FloatSlider(value=120,min=0,max=160,step=0.1,description='Sodium',readout_format='.1f',continuous_update=False)
slider_cond_K      = ipywidgets.FloatSlider(value=36,min=0,max=80,step=0.1,description='Potassium',readout_format='.1f',continuous_update=False)
slider_cond_L      = ipywidgets.FloatSlider(value=0.3,min=0,max=1,step=0.1,description='Leak',readout_format='.1f',continuous_update=False)
slider_pot_Na      = ipywidgets.FloatSlider(value=50,min=-100,max=100,step=0.1,description='Sodium',readout_format='.1f',continuous_update=False)
slider_pot_K       = ipywidgets.FloatSlider(value=-77,min=-100,max=100,step=0.1,description='Potassium',readout_format='.1f',continuous_update=False)
slider_pot_L       = ipywidgets.FloatSlider(value=-54.387,min=-100,max=100,step=0.1,description='Leak',readout_format='.1f',continuous_update=False)
time_start         = ipywidgets.FloatText(value=0,description='Start Time',disabled=True)
time_end           = ipywidgets.FloatText(value=450,description='Total Time',disabled=False)
time_step          = ipywidgets.FloatText(value=0.01,description='Time Step',disabled=False)
slider_amplitude   = ipywidgets.FloatSlider(value=50,min=-20,max=200,step=0.1,description='Amplitude',readout_format='.1f',continuous_update=False)
slider_width       = ipywidgets.FloatSlider(value=0,min=0,max=500,step=0.1,description='Width',readout_format='.1f',continuous_update=False)
slider_translation = ipywidgets.FloatSlider(value=50,min=0,max=250,step=0.1,description='Start at',readout_format='.1f',continuous_update=False)

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
h9=ipywidgets.HBox([header_injCurrent])
h10=ipywidgets.HBox([injCurrent_note])
h11=ipywidgets.HBox([slider_amplitude,slider_width,slider_translation])
h12=ipywidgets.HBox([reset_button])
modelInputs=ipywidgets.VBox([h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12])