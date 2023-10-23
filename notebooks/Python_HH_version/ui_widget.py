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
default_E_Na         = 63.54
default_E_K          = -74.16
default_E_L          = -54.3
default_t0           = 0
default_tn           = 50
default_deltat       = 0.01
default_ic_amplitude = 2.0
default_ic_duration  = 25
default_ic_delay     = 5

#voltage clamp default values
default_vc_delay         = 10
default_vc_duration      = 30
default_condVoltage   = -65
default_testVoltage   = 10
default_returnVoltage = -65
default_tn_vclamp     = 50
default_deltat_vclamp = 0.0005

#function to reset input values to default on button click
def resetTodefault(_):
    slider_capacitance.value = default_capacitance
    slider_cond_Na.value     = default_cond_Na
    slider_cond_K.value      = default_cond_K
    slider_cond_L.value      = default_cond_L
    slider_E_Na.value      = default_E_Na
    slider_E_K.value       = default_E_K
    slider_E_L.value       = default_E_L
    time_end.value           = default_tn
    time_step.value          = default_deltat
    slider_amplitude.value   = default_ic_amplitude
    slider_width.value       = default_ic_duration
    slider_translation.value = default_ic_delay

    #voltage clamp
    slider_delay.value         = default_vc_delay
    slider_duration.value      = default_vc_duration
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
    inputList    = [slider_capacitance, slider_cond_Na, slider_cond_K, slider_cond_L, slider_E_Na, slider_E_K, slider_E_L, slider_amplitude, slider_width, slider_translation,
                    slider_delay, slider_duration, slider_condVoltage, slider_testVoltage, slider_returnVoltage]
    inputDefault = [default_capacitance, default_cond_Na, default_cond_K, default_cond_L, default_E_Na, default_E_K, default_E_L, default_ic_amplitude, default_ic_duration, default_ic_delay,
                    default_vc_delay, default_vc_duration, default_condVoltage, default_testVoltage, default_returnVoltage]
    for l, d in zip(inputList,inputDefault):
        if l.value == d:
            l.style.handle_color = 'white'
        else:
            l.style.handle_color = 'orange'

#defining the widgets
#Header or texts as HTMLMath to include symbols
header_capacitance = ipywidgets.HTMLMath(value=r"<b> Membrane Capacitance, \(\mu{F}/cm^2\)</b>")
header_conductance = ipywidgets.HTMLMath(value=r"<b> Maximum Conductances, \(mS/cm^2\)</b>")
header_potential   = ipywidgets.HTMLMath(value=r"<b> Reversal Potentials, \(mV\)</b>")
header_simTime     = ipywidgets.HTMLMath(value=r"<b> Simulation Time, \(ms\)</b>")
header_injCurrent  = ipywidgets.HTMLMath(value=r"<b> Injection Current, \(\mu{A}/cm^2\) (or \(pA\) if cell has area 100 \(\mu{m}^2\))</b>")
header_runMode     = ipywidgets.HTML(value=r"<b>Select Run Mode</b>")
header_vclamp_time = ipywidgets.HTMLMath(value=r"<b> Time, \(ms\)</b>")
header_vclamp_volt = ipywidgets.HTMLMath(value=r"<b> Voltage, \(mV\)</b>")

#slider widgets
slider_capacitance = ipywidgets.FloatSlider(value=default_capacitance,min=0,max=3,step=0.1,description='Capacitance',readout=False,continuous_update=False)
slider_cond_Na     = ipywidgets.FloatSlider(value=default_cond_Na,min=0,max=160,step=0.1,description='Sodium',readout=False,continuous_update=False)
slider_cond_K      = ipywidgets.FloatSlider(value=default_cond_K,min=0,max=80,step=0.1,description='Potassium',readout=False,continuous_update=False)
slider_cond_L      = ipywidgets.FloatSlider(value=default_cond_L,min=0,max=1,step=0.1,description='Leak',readout=False,continuous_update=False)
slider_E_Na      = ipywidgets.FloatSlider(value=default_E_Na,min=-100,max=100,step=0.1,description='Sodium',readout=False,continuous_update=False)
slider_E_K       = ipywidgets.FloatSlider(value=default_E_K,min=-100,max=100,step=0.1,description='Potassium',readout=False,continuous_update=False)
slider_E_L       = ipywidgets.FloatSlider(value=default_E_L,min=-100,max=100,step=0.1,description='Leak',readout=False,continuous_update=False)
slider_amplitude   = ipywidgets.FloatSlider(value=default_ic_amplitude,min=-20.0,max=200.0,step=0.1,description='Amplitude',readout=False,continuous_update=False)
slider_width       = ipywidgets.FloatSlider(value=default_ic_duration,min=0,max=500,step=0.1,description='Duration',readout=False,continuous_update=False)
slider_translation = ipywidgets.FloatSlider(value=default_ic_delay,min=0,max=250,step=0.1,description='Time Delay',readout=False,continuous_update=False)

#vclamp sliders
slider_delay            = ipywidgets.FloatSlider(value=default_vc_delay         ,min=0,max=250,step=0.1,description='Time Delay',readout=False,continuous_update=False)
slider_duration         = ipywidgets.FloatSlider(value=default_vc_duration      ,min=0,max=500,step=0.1,description='Duration',readout=False,continuous_update=False)
slider_condVoltage      = ipywidgets.FloatSlider(value=default_condVoltage   ,min=-120,max=100,step=1,description='Conditioning',readout=False,continuous_update=False)
slider_testVoltage      = ipywidgets.FloatSlider(value=default_testVoltage   ,min=-120,max=100,step=1,description='Testing',readout=False,continuous_update=False)
slider_returnVoltage    = ipywidgets.FloatSlider(value=default_returnVoltage ,min=-120,max=100,step=1,description='Returning',readout=False,continuous_update=False)

#text box widgets
time_end           = ipywidgets.FloatText(value=default_tn,description='Total Time',disabled=False)
time_step          = ipywidgets.FloatText(value=default_deltat,description='Time Step',disabled=False)

#text box widgets to link with sliders (included to type in values for slider inputs also)
textBox_capacitance = ipywidgets.FloatText(value=default_capacitance,step=0.1,layout=ipywidgets.Layout(width='10%'))
textBox_cond_Na     = ipywidgets.FloatText(value=default_cond_Na,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_cond_K      = ipywidgets.FloatText(value=default_cond_K,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_cond_L      = ipywidgets.FloatText(value=default_cond_L,step=0.1,layout=ipywidgets.Layout(width='10%'))
textBox_E_Na      = ipywidgets.FloatText(value=default_E_Na,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_E_K       = ipywidgets.FloatText(value=default_E_K,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_E_L       = ipywidgets.FloatText(value=default_E_L,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_amplitude   = ipywidgets.FloatText(value=default_ic_amplitude,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_width       = ipywidgets.FloatText(value=default_ic_duration,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_translation = ipywidgets.FloatText(value=default_ic_delay,step=1,layout=ipywidgets.Layout(width='10%'))

#voltage clamp textboxes to link with sliders
textBox_delay         = ipywidgets.FloatText(value=default_vc_delay,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_duration      = ipywidgets.FloatText(value=default_vc_duration,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_condVoltage   = ipywidgets.FloatText(value=default_condVoltage,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_testVoltage   = ipywidgets.FloatText(value=default_testVoltage,step=1,layout=ipywidgets.Layout(width='10%'))
textBox_returnVoltage = ipywidgets.FloatText(value=default_returnVoltage,step=1,layout=ipywidgets.Layout(width='10%'))

#linking sliders and textbox for values
link_capacitance = link((slider_capacitance, 'value'), (textBox_capacitance, 'value'))
link_cond_Na     = link((slider_cond_Na, 'value'), (textBox_cond_Na, 'value'))
link_cond_K      = link((slider_cond_K, 'value'), (textBox_cond_K, 'value'))
link_cond_L      = link((slider_cond_L, 'value'), (textBox_cond_L, 'value'))
link_E_Na      = link((slider_E_Na, 'value'), (textBox_E_Na, 'value'))
link_E_K       = link((slider_E_K, 'value'), (textBox_E_K, 'value'))
link_E_L       = link((slider_E_L, 'value'), (textBox_E_L, 'value'))
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
defalultValues = ipywidgets.HTMLMath(value=r"\(C = %s\)<br>\(G_{Na} = %s, G_{K} = %s, G_{L} =  %s\)<br>\(E_{Na} =  %s, E_{K} = %s, E_{L} = %s\)" % \
                     (default_capacitance, default_cond_Na, default_cond_K, default_cond_L, default_E_Na, default_E_K, default_E_L))
defalultValues.layout.display = 'none'

#define toggle buttons for iclamp/vclamp run mode
runMode_togglebtns = ipywidgets.ToggleButtons(options=['Current Clamp', 'Voltage Clamp'],description='',button_style='',
                                             tooltips=['Simulate using an injected square current pulse', 'Simulate in voltage clamp mode - inject varying current to force specific voltage profile'])
runMode_togglebtns.observe(runModeChange,'value')

#layout widgets in column using HBox
h1=ipywidgets.HBox([header_capacitance])
h2=ipywidgets.HBox([slider_capacitance, textBox_capacitance])
h3=ipywidgets.HBox([header_conductance])
h4=ipywidgets.HBox([slider_cond_Na,textBox_cond_Na,slider_cond_K,textBox_cond_K,slider_cond_L,textBox_cond_L])
h5=ipywidgets.HBox([header_potential])
h6=ipywidgets.HBox([slider_E_Na,textBox_E_Na,slider_E_K,textBox_E_K,slider_E_L,textBox_E_L])
h7=ipywidgets.HBox([header_simTime])
h8=ipywidgets.HBox([time_end,time_step])
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

#plot selectors
header_plotting = ipywidgets.HTMLMath(value=r"<b> Select plots to show</b>")
injected_current_plot_value = ipywidgets.Checkbox(value=True, description="1) Current injection", disabled=False,)
gating_plot_value = ipywidgets.Checkbox(value=True, description="2) Gating variables", disabled=False,)
cond_scaling_value = ipywidgets.Checkbox(value=False, description="3) Conductance scaling", disabled=False,)
cond_dens_plot_value = ipywidgets.Checkbox(value=True, description="4) Conductance densities", disabled=False,)
driving_force_value = ipywidgets.Checkbox(value=False, description="5) Driving force", disabled=False,)
current_plot_value = ipywidgets.Checkbox(value=True, description="6) Current densities", disabled=False,)
memb_pot_plot_value = ipywidgets.Checkbox(value=True, description="7) Membrane potential", disabled=False,)
plot_selection_row=ipywidgets.VBox([header_plotting, ipywidgets.HBox([injected_current_plot_value, gating_plot_value, cond_scaling_value, cond_dens_plot_value]), ipywidgets.HBox([driving_force_value, current_plot_value, memb_pot_plot_value])])

#layout vertically all the widgets defined above
modelInputs=ipywidgets.VBox([h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,runMode_iclamp,runMode_vclamp,button_row,defalultValues,plot_selection_row])

# Main method to create interactive widget
def launch_interactive_widget():

    import ipywidgets
    from importlib.machinery import SourceFileLoader

    # imports the module from the given path
    HHmodel = SourceFileLoader("HodgkinHuxley.py","../../Tutorial/Source/HodgkinHuxley.py").load_module()

    #function to call python script as a module
    def runHH(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L, t_n, delta_t,
              I_inj_max, I_inj_width, I_inj_trans, vc_delay, vc_duration,
              vc_condVoltage, vc_testVoltage, vc_returnVoltage, runMode,
              injected_current_plot, gating_plot, cond_scaling_plot, cond_dens_plot, driving_force_plot, current_plot, memb_pot_plot):

        highlight_slider()
        runner = HHmodel.HodgkinHuxley(C_m, g_Na, g_K, g_L, E_Na, E_K, E_L,
                                       t_n, delta_t, I_inj_max,
                                       I_inj_width, I_inj_trans, vc_delay,
                                       vc_duration, vc_condVoltage,
                                       vc_testVoltage, vc_returnVoltage,
                                       runMode,
                                       injected_current_plot=injected_current_plot,
                                       gating_plot=gating_plot,
                                       cond_scaling_plot=cond_scaling_plot,
                                       cond_dens_plot=cond_dens_plot,
                                       driving_force_plot=driving_force_plot,
                                       current_plot=current_plot,
                                       memb_pot_plot=memb_pot_plot)
        # init_values are the steady state values for v,m,h,n at zero current injection
        runner.simulate(init_values=[-63.8, 0.0609, 0.5538, 0.3361])

    #create plot area widget and interact with HHmodel
    wid_plotArea=ipywidgets.interactive_output(runHH,{'C_m':slider_capacitance,
                                            'g_Na':textBox_cond_Na, 'g_K':textBox_cond_K, 'g_L':textBox_cond_L,
                                            'E_Na':textBox_E_Na, 'E_K':textBox_E_K, 'E_L':textBox_E_L,
                                            't_n':time_end, 'delta_t':time_step,
                                            'I_inj_max':textBox_amplitude,'I_inj_width':textBox_width,'I_inj_trans':textBox_translation,
                                            'vc_delay':textBox_delay,'vc_duration':textBox_duration,'vc_condVoltage':textBox_condVoltage,
                                            'vc_testVoltage':textBox_testVoltage,'vc_returnVoltage':textBox_returnVoltage,
                                            'runMode':runMode_togglebtns, 'injected_current_plot': injected_current_plot_value,
                                                      'gating_plot':gating_plot_value,
                                                      'cond_scaling_plot':cond_scaling_value,
                                                      'cond_dens_plot':cond_dens_plot_value,
                                                      'driving_force_plot':driving_force_value,
                                                      'current_plot':current_plot_value,
                                                      'memb_pot_plot':memb_pot_plot_value})

    #display the widgets and plot area
    display(modelInputs,wid_plotArea)
