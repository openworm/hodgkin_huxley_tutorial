Exercises
=========

Some exercises which can be carried out with the Python or NeuroML versions of the HH model. See `here <Tutorial.html>`_ for installation instructions.



**1) Adjust the input current to the cell to investigate the changes in membrane potential and Na, K current behaviour**

    To change the scripts for the HH model:

+---------------+----------------------------------------------------------------------------------------------------------------+
| *Python*      | adjust values in method *I_inj* in `HodgkinHuxley.py <Hodgkin%20Huxley.html>`_                                 |
+---------------+----------------------------------------------------------------------------------------------------------------+
| *NeuroML2*    | adjust values for *amplitude* in <pulseGenerator> elements in `HHCellNetwork.net.nml <HHCellNetwork.html>`_    |
+---------------+----------------------------------------------------------------------------------------------------------------+

    1.1 What is the minimum current you can inject that will cause at least one spike?

    1.2 Adjust the input current duration to stimulate the cell for the full duration of the simulation. What is the minimum current you need to inject to get the cell to fire for the full duration?
    
    1.3 How much does a 10-fold increase in injected current from the repetitive firing current increase the firing rate? 
    
    1.4 What happens for a 100-fold increase? Why does this happen?

    1.5 Is there any current you can inject to get a half height action potential?
    
    1.6 Single action potentials can also be elicited by transient current pulses, even when the duration of the current pulse is shorter than the action potential. What is the effect of pulse duration on threshold current for eliciting a single action potential? Generate a plot of threshold current vs. pulse duration for pulse widths between 0.1 ms and 5 ms (You don't need to write code for this, you can just run the existing code several times to find the data points and then make a plot).  Is there a simple relationship between pulse width and threshold current? 


**2) Adjusting properties of Na & K**

+---------------+----------------------------------------------------------------------------------------------------------------+
| *Python*      | adjust values for *g_Na*, *g_K*, *E_Na*, etc. in `HodgkinHuxley.py <Hodgkin%20Huxley.html>`_                   |
+---------------+----------------------------------------------------------------------------------------------------------------+
| *NeuroML2*    | adjust values for *condDensity*, *erev* in <channelDensity> elements in `hhcell.cell.nml <hhcell.html>`_       |
+---------------+----------------------------------------------------------------------------------------------------------------+
   
   2.1 Return the input current injection to the original values. Reduce the conductance densities of Na and K. What is the impact on the AP?
   
   2.2 Restore the original conductance densities. Reduce the reversal potential (e.g. to 20mV) of Na to simulate a decrease in the extracellular Na concentration (i.e. external [Na+] is closer to internal [Na+]). What is the impact on the height/waveform of the action potential? Can a change in the conductance density of Na compensate for this (i.e. increase the height of the AP)? If not, why not?
    
   
   

**3) Hyperpolarizing current injections**

All of the previously used current injection pulses have been depolarising (increasing the membrane potential from resting voltage). We now try some hyperpolarizing current injections (see 1) above for changing current amplitudes). 

    3.1 Set the pulse amplitude to –5 and the pulse duration to 5 ms.  What happens for hyperpolarizing current injections? 
    
    3.2 What is the threshold, in terms of current magnitude and pulse duration, for eliciting this so-called `anode break excitation <https://en.wikipedia.org/wiki/Anode_break_excitation>`_? 
    
    3.3 What mechanisms in the model are responsible for this behaviour? Look at the time course of the activation and inactivation variables n, m and h. 


