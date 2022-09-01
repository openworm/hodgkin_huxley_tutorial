import ipywidgets
import numpy as np
import pylab as plt
from traitlets import link

#running current (default) or voltage clamp
runMode = 'iclamp'

#default input parameters
default_capacitance  = 1
default_cond_Na      = 120
default_cond_K       = 36
default_cond_L       = 0.3
default_pot_Na       = 50
default_pot_K        = -77
default_pot_L        = -54.387
default_t0           = 0
default_tn           = 150
default_deltat       = 0.01
default_amplitude    = 10
default_width        = 100
default_translation  = 25

#voltage clamp default values
default_delay         = 10
default_duration      = 30
default_condVoltage   = -65
default_testVoltage   = 10
default_returnVoltage = -65
default_tn_vclamp     = 50
default_deltat_vclamp = 0.0001

#function to reset input values to default on button click
def resetTodefault(_):
    slider_capacitance.value = default_capacitance
    slider_cond_Na.value     = default_cond_Na
    slider_cond_K.value      = default_cond_K
    slider_cond_L.value      = default_cond_L
    slider_pot_Na.value      = default_pot_Na
    slider_pot_K.value       = default_pot_K
    slider_pot_L.value       = default_pot_L
    time_start.value         = default_t0
    time_end.value           = default_tn
    time_step.value          = default_deltat
    slider_amplitude.value   = default_amplitude
    slider_width.value       = default_width
    slider_translation.value = default_translation

    #voltage clamp
    slider_delay.value         = default_delay
    slider_duration.value      = default_duration
    slider_condVoltage.value   = default_condVoltage
    slider_testVoltage.value   = default_testVoltage
    slider_returnVoltage.value = default_returnVoltage

    #default runMode
    runMode_togglebtns.value='Current Clamp'

def showDefault(response):
    if showValue_togglebtn.value:
        defalultValues.layout.display = ''
    else:
        defalultValues.layout.display = 'none'

def runModeChange(c):
    global runMode
    if runMode_togglebtns.value=='Current Clamp':
        runMode_iclamp.layout.display = ''
        runMode_vclamp.layout.display = 'none'
        runMode = 'iclamp'
        time_step.value = default_deltat
        time_end.value  = default_tn
        
    else:
        runMode_iclamp.layout.display = 'none'
        runMode_vclamp.layout.display = ''
        runMode = 'vclamp'
        time_end.value = default_tn_vclamp
        time_step.value = default_deltat_vclamp
    
#function to change slider handle colour when move from default
def highlight_slider():
    inputList    = [slider_capacitance, slider_cond_Na, slider_cond_K, slider_cond_L, slider_pot_Na, slider_pot_K, slider_pot_L, slider_amplitude, slider_width, slider_translation,
                    slider_delay, slider_duration, slider_condVoltage, slider_testVoltage, slider_returnVoltage]
    inputDefault = [default_capacitance, default_cond_Na, default_cond_K, default_cond_L, default_pot_Na, default_pot_K, default_pot_L, default_amplitude, default_width, default_translation,
                    default_delay, default_duration, default_condVoltage, default_testVoltage, default_returnVoltage]
    for l, d in zip(inputList,inputDefault):
        if l.value == d:
            l.style.handle_color = 'white'
        else:
            l.style.handle_color = 'orange'
    
#defining the widgets
#Header or texts as HTMLMath to include symbols
header_capacitance = ipywidgets.HTMLMath(value=r"<b> Membrane Capacitance, \(\mu{F}/cm^2\)</b>")
header_conductance = ipywidgets.HTMLMath(value=r"<b> Maximum Conductances, \(mS/cm^2\)</b>")
header_potential   = ipywidgets.HTMLMath(value=r"<b> Nernst Reverasal Potentials, \(mV\)</b>")
header_simTime     = ipywidgets.HTMLMath(value=r"<b> Simulation Time, \(ms\)</b>")
header_injCurrent  = ipywidgets.HTMLMath(value=r"<b> Injection Current, \(\mu{A}/cm^2\)</b>")
header_runMode     = ipywidgets.HTML(value=r"<b>Select Run Mode</b>")
header_vclamp_time = ipywidgets.HTMLMath(value=r"<b> Time, \(ms\)</b>")
header_vclamp_volt = ipywidgets.HTMLMath(value=r"<b> Voltage, \(mV\)</b>")

#slider widgets
slider_capacitance = ipywidgets.FloatSlider(value=default_capacitance,min=0,max=3,step=0.1,description='Capacitance',readout=False,continuous_update=False)
slider_cond_Na     = ipywidgets.FloatSlider(value=default_cond_Na,min=0,max=160,step=0.1,description='Sodium',readout=False,continuous_update=False)
slider_cond_K      = ipywidgets.FloatSlider(value=default_cond_K,min=0,max=80,step=0.1,description='Potassium',readout=False,continuous_update=False)
slider_cond_L      = ipywidgets.FloatSlider(value=default_cond_L,min=0,max=1,step=0.1,description='Leak',readout=False,continuous_update=False)
slider_pot_Na      = ipywidgets.FloatSlider(value=default_pot_Na,min=-100,max=100,step=0.1,description='Sodium',readout=False,continuous_update=False)
slider_pot_K       = ipywidgets.FloatSlider(value=default_pot_K,min=-100,max=100,step=0.1,description='Potassium',readout=False,continuous_update=False)
slider_pot_L       = ipywidgets.FloatSlider(value=default_pot_L,min=-100,max=100,step=0.1,description='Leak',readout=False,continuous_update=False)
slider_amplitude   = ipywidgets.FloatSlider(value=default_amplitude,min=-20,max=200,step=0.1,description='Amplitude',readout=False,continuous_update=False)
slider_width       = ipywidgets.FloatSlider(value=default_width,min=0,max=500,step=0.1,description='Duration',readout=False,continuous_update=False)
slider_translation = ipywidgets.FloatSlider(value=default_translation,min=0,max=250,step=0.1,description='Time Delay',readout=False,continuous_update=False)

#vclamp sliders
slider_delay            = ipywidgets.FloatSlider(value=default_delay         ,min=0,max=250,step=0.1,description='Time Delay',readout=False,continuous_update=False)
slider_duration         = ipywidgets.FloatSlider(value=default_duration      ,min=0,max=500,step=0.1,description='Duration',readout=False,continuous_update=False)
slider_condVoltage      = ipywidgets.FloatSlider(value=default_condVoltage   ,min=-100,max=100,step=0.1,description='Conditioning',readout=False,continuous_update=False)
slider_testVoltage      = ipywidgets.FloatSlider(value=default_testVoltage   ,min=-100,max=100,step=0.1,description='Testing',readout=False,continuous_update=False)
slider_returnVoltage    = ipywidgets.FloatSlider(value=default_returnVoltage ,min=-100,max=100,step=0.1,description='Returning',readout=False,continuous_update=False)

#text box widgets
time_start         = ipywidgets.FloatText(value=default_t0,description='Start Time',disabled=True)
time_end           = ipywidgets.FloatText(value=default_tn,description='Total Time',disabled=False)
time_step          = ipywidgets.FloatText(value=default_deltat,description='Time Step',disabled=False)

#text box widgets to link with sliders (included to type in values for slider inputs also)
textBox_capacitance = ipywidgets.FloatText(value=default_capacitance,step=0.1,layout=ipywidgets.Layout(width='10%'))
textBox_cond_Na     = ipywidgets.FloatText(value=default_cond_Na,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_cond_K      = ipywidgets.FloatText(value=default_cond_K,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_cond_L      = ipywidgets.FloatText(value=default_cond_L,step=0.1,layout=ipywidgets.Layout(width='10%'))
textBox_pot_Na      = ipywidgets.FloatText(value=default_pot_Na,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_pot_K       = ipywidgets.FloatText(value=default_pot_K,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_pot_L       = ipywidgets.FloatText(value=default_pot_L,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_amplitude   = ipywidgets.FloatText(value=default_amplitude,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_width       = ipywidgets.FloatText(value=default_width,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_translation = ipywidgets.FloatText(value=default_translation,step=1,layout=ipywidgets.Layout(width='10%'))

#voltage clamp textboxes to link with sliders
textBox_delay         = ipywidgets.FloatText(value=default_delay,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_duration      = ipywidgets.FloatText(value=default_duration,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_condVoltage   = ipywidgets.FloatText(value=default_condVoltage,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_testVoltage   = ipywidgets.FloatText(value=default_testVoltage,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_returnVoltage = ipywidgets.FloatText(value=default_returnVoltage,step=1,layout=ipywidgets.Layout(width='10%'))

#linking sliders and textbox for values
link_capacitance = link((slider_capacitance, 'value'), (textBox_capacitance, 'value'))
link_cond_Na     = link((slider_cond_Na, 'value'), (textBox_cond_Na, 'value'))
link_cond_K      = link((slider_cond_K, 'value'), (textBox_cond_K, 'value'))
link_cond_L      = link((slider_cond_L, 'value'), (textBox_cond_L, 'value'))
link_pot_Na      = link((slider_pot_Na, 'value'), (textBox_pot_Na, 'value'))
link_pot_K       = link((slider_pot_K, 'value'), (textBox_pot_K, 'value'))
link_pot_L       = link((slider_pot_L, 'value'), (textBox_pot_L, 'value'))
link_amplitude   = link((slider_amplitude, 'value'), (textBox_amplitude, 'value'))
link_width       = link((slider_width, 'value'), (textBox_width, 'value'))
link_translation = link((slider_translation, 'value'), (textBox_translation, 'value'))

#voltage clamp slider and textbox link for values
link_delay          = link((slider_delay         , 'value'), (textBox_delay         , 'value'))
link_duration       = link((slider_duration      , 'value'), (textBox_duration      , 'value'))
link_condVoltage    = link((slider_condVoltage   , 'value'), (textBox_condVoltage   , 'value'))
link_testVoltage    = link((slider_testVoltage   , 'value'), (textBox_testVoltage   , 'value'))
link_returnVoltage  = link((slider_returnVoltage , 'value'), (textBox_returnVoltage , 'value'))

#define reset button and connect to fucntion call
reset_button = ipywidgets.Button(description="Reset All",button_style='warning',tooltip='Reset to default values for all user inputs')
reset_button.on_click(resetTodefault)

#define toggle button for default values and connect to fucntion call
showValue_togglebtn = ipywidgets.ToggleButton(value=False,description='Default Values',disabled=False,button_style='info',tooltip='Show/Hide default value below') # 'success', 'info', 'warning', 'danger' or ''
showValue_togglebtn.observe(showDefault)
defalultValues = ipywidgets.HTMLMath(value=r"\(C = 1.0\)<br>\(G_{Na} = 120, G_{K} =  36, G_{L} =  0.3\)<br>\(V_{Na} =  50, V_{K} = -77, G_{L} = -54.387\)")
defalultValues.layout.display = 'none'

#define toggle buttons for iclamp/vclamp run mode
runMode_togglebtns = ipywidgets.ToggleButtons(options=['Current Clamp', 'Voltage Clamp'],description='',button_style='', # 'success', 'info', 'warning', 'danger' or ''
                                             tooltips=['Simulate with given injection current', 'Simulate with fixed voltage input'])
runMode_togglebtns.observe(runModeChange,'value')

#layout widgets in column using HBox
h1=ipywidgets.HBox([header_capacitance])
h2=ipywidgets.HBox([slider_capacitance, textBox_capacitance])
h3=ipywidgets.HBox([header_conductance])
h4=ipywidgets.HBox([slider_cond_Na,textBox_cond_Na,slider_cond_K,textBox_cond_K,slider_cond_L,textBox_cond_L])
h5=ipywidgets.HBox([header_potential])
h6=ipywidgets.HBox([slider_pot_Na,textBox_pot_Na,slider_pot_K,textBox_pot_K,slider_pot_L,textBox_pot_L])
h7=ipywidgets.HBox([header_simTime])
h8=ipywidgets.HBox([time_start,time_end,time_step])
h9=ipywidgets.HBox([header_runMode])
h10=ipywidgets.HBox([runMode_togglebtns])

#widget for current clamp mode (default)
iclamp_sliders=ipywidgets.HBox([slider_amplitude,textBox_amplitude,slider_width,textBox_width,slider_translation,textBox_translation])
runMode_iclamp=ipywidgets.VBox([header_injCurrent,iclamp_sliders])

#widget for voltage clamp mode
vclamp_sliders_time    =ipywidgets.HBox([slider_delay,textBox_delay,slider_duration,textBox_duration])
vclamp_sliders_volt    =ipywidgets.HBox([slider_condVoltage,textBox_condVoltage,slider_testVoltage,textBox_testVoltage,slider_returnVoltage,textBox_returnVoltage])
runMode_vclamp         =ipywidgets.VBox([header_vclamp_time,vclamp_sliders_time,header_vclamp_volt,vclamp_sliders_volt])
runMode_vclamp.layout.display = 'none'

#reset and defalult value buttons in single row
button_row=ipywidgets.HBox([reset_button,showValue_togglebtn])

#layout vertically all the widgets defined above 
modelInputs=ipywidgets.VBox([h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,runMode_iclamp,runMode_vclamp,button_row,defalultValues])