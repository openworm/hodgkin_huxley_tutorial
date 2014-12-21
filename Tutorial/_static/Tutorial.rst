Hodgkin Huxley NeuroML/LEMS Neuron Model Tutorial
=================================================

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

Sodium (Na) Ion Channel Variables
---------------------------------

These variables from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 11-12

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 20-21

Is used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 67

Potassium (K) Ion Channel Variables
-----------------------------------

These variables from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 14-15

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 23-24

Is used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 68

Passive Leak Channel Variables
------------------------------

These variables from HodgkinHuxley.py:

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 17-18

.. literalinclude:: ../Source/HodgkinHuxley.py
   :language: python
   :lines: 26-27

Is used in this line in NML2_SingleCompHHCell.nml:

.. literalinclude:: ../Source/NML2_SingleCompHHCell.nml
   :language: XML
   :lines: 66

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
Functions of membrane voltage

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
Functions of membrane voltage

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
Functions of membrane voltage

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

**Where do the rest of these initial values from HodgkinHuxley.py fit into the NeuroML/LEMS Model?**

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