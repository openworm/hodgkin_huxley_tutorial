Hodgkin Huxley NeuroML2/LEMS Neuron Model Tutorial
=================================================

In this section, we make line-by-line comparisons of the contents of the HodgkinHuxley.py python script and
the contents of the NML2_SingleCompHHCell.nml NeuroML2 file and the related LEMS_NML2_Ex5_DetCell.xml LEMS file.

Membrane Capacitance
--------------------

This variable from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 8-9

Is used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 71

You can `read more about the capacitance of a membrane <http://www.scholarpedia.org/article/Electrical_properties_of_cell_membranes#Capacitance>`_.

Sodium (Na) Ion Channel Variables
---------------------------------

These variables from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 11-12

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 20-21

Are used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 67

You can `read more about the maximum conductance and reversal potential (zero-current potential) of an ion channel <http://www.scholarpedia.org/article/Ion_channels#Bioelectricity_results_from_currents_in_ion_channels>`_.


Potassium (K) Ion Channel Variables
-----------------------------------

These variables from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 14-15

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 23-24

Are used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 68

You can `read more about the maximum conductance and reversal potential (zero-current potential) of an ion channel <http://www.scholarpedia.org/article/Ion_channels#Bioelectricity_results_from_currents_in_ion_channels>`_.

Passive Leak Channel Variables
------------------------------

These variables from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 17-18

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 26-27

Are used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 66

You can `read more about the maximum conductance and reversal potential (zero-current potential) of an ion channel <http://www.scholarpedia.org/article/Ion_channels#Bioelectricity_results_from_currents_in_ion_channels>`_.

Time of Simulation
------------------

This variable from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 29-30

Is used in this line in LEMS_NML2_Ex5_DetCell.xml:

.. literalinclude:: ../Source/LEMS_NML2_Ex5_DetCell.xml
   :language: XML
   :lines: 24

This specifies that the simulation should run for 450 milliseconds and use a step size for integration of 0.01 milliseconds.

Input Current / Input Current Density
-------------------------------------

The method from HodgkinHuxley.py takes the input in as a current density in the form of uA/cm^2.  NeuroML/LEMS uses an input current in the form of nA, which requires a conversion in the input values.

This method from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.I_inj
   :linenos:

By using a given surface area of 1000.0 um^2 in the cell, it makes the conversion from uA/cm^2 to nA easier.

.. math::

   Surface Area = 4 * pi * (radius)^2 = 4 * pi * (diameter / 2)^2 = 4 * pi * (17.841242 / 2)^2 = 4 * pi * (8.920621)^2 = 1000 um^2

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 51-54

Given a surface area of 1000.0 um^2 in the cell the following equation is used to convert from X uA/cm^2 to Y nA:

.. math::

   (X  uA/cm^2) * (1000.0  um^2) * (1000  nA/uA) / (1 * 10^8  um^2/cm^2) = Y nA

Line 11 can then be translated into the delay, duration and amplitude of the two pulseGenerator objects in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 84-85

Channel Gating Kinetics for Sodium (Na) Channel m
-------------------------------------------------

m is the activation variable for the Sodium (Na) Channel.

The function that governs the activation of this channel is based on the overall
membrane voltage, because the channel opens and closes based on detecting the membrane potential.

You can `read more about these variables <https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model#Voltage-gated_ion_channels>`_.

These methods from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.alpha_m
   :linenos:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.beta_m
   :linenos:

Are used in these lines in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 24-27

Channel Gating Kinetics for Sodium (Na) Channel h
-------------------------------------------------

h is the inactivation variable for the Sodium (Na) Channel.  Inactivation is a
different state than not being activated, which is called "deactivated".  You can
`read more about how Sodium channel gating works <https://en.wikipedia.org/wiki/Sodium_channel#Gating>`_.

The function that governs the activation of this channel is based on the overall
membrane voltage, because the channel opens and closes based on detecting the membrane potential.

You can `read more about these variables <https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model#Voltage-gated_ion_channels>`_.

These methods from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.alpha_h
   :linenos:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.beta_h
   :linenos:

Are used in these lines in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 29-32

Channel Gating Kinetics for Potassium (K) channel n
---------------------------------------------------

n is the activation variable for the Potassium (Na) Channel.  The potassium channel does not inactivate, so there is no inactivation variable.

The function that governs the activation of this channel is based on the overall
membrane voltage, because the channel opens and closes based on detecting the membrane potential.

You can `read more about these variables <https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model#Voltage-gated_ion_channels>`_.

These methods from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.alpha_n
   :linenos:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :pyobject: HodgkinHuxley.beta_n
   :linenos:

Are used in these lines in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 39-42

Initial Values
--------------

This line from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 124

Is used to define the initial values for the model in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 72

The values for m, h, n at t=0 in LEMS/NML2 are worked out as the steady state values (inf)
of each activation variable for the given initial membrane potential.
See [here](http://www.neuroml.org/NeuroML2CoreTypes/Channels.html#gateHHrates)
for the nml2 implementation (see On Start).

You could refactor the script to do this too by introducing tau_m() and inf_m()
and using alpha_m etc., change the expressions for dmdt etc. (e.g. dm/dt = (inf_m - m) / tau_m) etc. and::

  V_init = -65
  X = odeint(self.dALLdt, [V_init, m_inf(V_init), h_inf(V_init), n_inf(V_init)], self.t, args=(self,))



Plots
-----

This line in HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 135-138

Is used in these lines in LEMS_NML2_Ex5_DetCell.xml:

.. literalinclude:: ../Source/LEMS_NML2_Ex5_DetCell.xml
   :language: XML
   :lines: 26-28

This line in HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 140-145

Is used in these lines in LEMS_NML2_Ex5_DetCell.xml:

.. literalinclude:: ../Source/LEMS_NML2_Ex5_DetCell.xml
   :language: XML
   :lines: 36-40

This line in HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 147-152

Is used in these lines in LEMS_NML2_Ex5_DetCell.xml:

.. literalinclude:: ../Source/LEMS_NML2_Ex5_DetCell.xml
   :language: XML
   :lines: 30-34

This line in HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 154-158

Is used in these lines in LEMS_NML2_Ex5_DetCell.xml:

.. literalinclude:: ../Source/LEMS_NML2_Ex5_DetCell.xml
   :language: XML
   :lines: 42-45
