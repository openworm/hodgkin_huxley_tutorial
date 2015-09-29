Exercises
=========

Some exercises which can be carried out with the Python or NeuroML versions of the HH model.



1) Adjust the input current to the cell to investigate the changes in membrane potential and Na, K current behaviour

    To change the scripts for the HH model:

+---------------+----------------------------------------------------------------------------------------------------------------+
| *Python*      | adjust values in method *I_inj* in `HodgkinHuxley.py <Hodgkin%20Huxley.html>`_                                 |
+---------------+----------------------------------------------------------------------------------------------------------------+
| *NeuroML2*    | adjust values for *amplitude* in <pulseGenerator> elements in `HHCellNetwork.net.nml <HHCellNetwork.html>`_    |
+---------------+----------------------------------------------------------------------------------------------------------------+

    - What is the minimum current you can inject that will cause at least one spike?

    - Adjust the input current duration to stimulate the cell for the full duration of the simulation. What is the minimum curent you need to inject to get the cell to fire for the full duration?

    - Is there any current you can inject to get a half height action potential?


2) Adjusting properties of Na & K

+---------------+----------------------------------------------------------------------------------------------------------------+
| *Python*      | adjust values for *g_Na*, *g_K*, *E_Na*, etc. in `HodgkinHuxley.py <Hodgkin%20Huxley.html>`_                   |
+---------------+----------------------------------------------------------------------------------------------------------------+
| *NeuroML2*    | adjust values for *condDensity*, *erev* in <channelDensity> elements in `hhcell.cell.nml <hhcell.html>`_       |
+---------------+----------------------------------------------------------------------------------------------------------------+
   
   - Return the input current injection to the original values
   
   - Reduce the reversal potential (e.g. to 20mV) of Na to simulate a decrease in the extracellular Na concentration (i.e. external [Na+] is closer to internal [Na+]). What is the impact on the height/waveform of the action potential?
    
   - Reduce the conductance densities of Na and K. What is the impact on the AP?
   
   


