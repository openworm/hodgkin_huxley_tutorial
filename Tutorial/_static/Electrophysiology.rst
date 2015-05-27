.. role:: raw-html(raw)
   :format: html

Biological/Electronic Equivalence
=================================

This model relies on a basic equivalence between a biological membrane plus
embedded ion channels, and an electronic circuit.

The circuit can be described by the diagram below, which is an electronuic
diagram representing a patch of cellular membrane.

.. image:: http://upload.wikimedia.org/wikipedia/commons/9/98/Hodgkin-Huxley.svg


The Circuit
-----------

The **membrane capacitance** (*C:sub:`m`*) is taken to be a fixed property of the membrane.

Parallel to *C:sub:`m`* are two "battery-capacitor" series; one for each of
voltage-gated and leak ion channels.

Each of these ion pathways are modeled as the product of the ion's
**conductance** (*g*) and its driving electrochemical gradient (*E*), both of which may vary
over time (except in the case of *g:sub:`L`*; see below).

*I:sub:`p`* represents the active movement of ions provided by
**ion transporters**.

The net result of all of this activity in the cell membrane is a current across
the membrane (i.e. from intracellular medium to extracellular medium, or vice versa).

Modeling voltage-gating versus leak:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The conductances of voltage-gated and leak channels, *g:sub:`n`* and *g:sub:`L`*
respectively, are modeled differently. Since the gating of voltage-gated ion
channels depends on the membrane potential at a given moment, it is non-linear.
In contrast, leak ion channels are always in the same state, so their
conductance is modeled linearly.

The Math
--------

Lipid bilayer current
^^^^^^^^^^^^^^^^^^^^^

.. image:: http://upload.wikimedia.org/math/2/2/4/224f520989592dc0d3aa096313581e19.png

The current across the cell's lipid bilayer ( *I:sub:`c`* ) is the product of the
membrane's capacitance ( *C:sub:`m`* ) and the rate of change of membrane
potential ( *V:sub:`m`* ) with respect to time ( *t* ).

Ion channel current
^^^^^^^^^^^^^^^^^^^

.. image:: http://upload.wikimedia.org/math/6/1/7/617b32943eae50e0e9f34cc5d0f4faf4.png

The current through a given ion channel ( *I:sub:`i`* ) is the product of that
channel's conductance ( *g:sub:`i`* ) and the difference *V:sub:`m` - V:sub:`i`*

*V:sub:`i`* is the ion species' **reversal potential**. Notice that when *V:sub:`m`*
is equal to *V:sub:`i`* the product becomes zero, and there is no net flow
( *I:sub:`i`* ) for the ion, which is what defines reversal potential.

Combining these currents
^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: http://upload.wikimedia.org/math/0/a/4/0a40dd385ad9546d4722cccacd11120b.png

If we sum the lipid bilayer current with ion channel currents for each ion
species, we end up with a total current ( *I* ) for the patch of cellular
membrane.

In the equation above, voltage-gated potassium ( *K* ) and sodium ( *Na* ) channels,
as well as leak channels ( *L* ) are considered, leading to three instances of
the ion channel current calculations.

Adding in activation parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since the ion channels denoted in the equation above are in various states, some
new variables must be added to the equation. Namely, activation and inactivation
parameters are now included in each ion channel current calculation.

.. image:: https://upload.wikimedia.org/math/e/2/6/e26962e13109f3e6df273553a731f24b.png

The new notation for each conductance variable ( *:raw-html:`<span style="text-decoration:overline">g</span>`* )
is the *maximal* conductance for that ion channel type. This, combined with the
activation/inactivation parameters *n*, *m* and *h*, still represents the level
of conductance for an ion channel, but with parameters that modify this
conductance.

- *n* is the activation parameter for potassium ( K ) channels
- *m*  is the activation parameter for sodium ( Na ) channels
- *h* is the *in*activation parameter for sodium channels

Terms
=====

- `Ion channel <http://en.wikipedia.org/wiki/Ion_channel>`_
    - Protein embedded in cellular membrane allowing *passive* flow of ions, depending on its configuration.
- Ion channel conductance
    - The rate of flow of ions through an ion channel. Directly affects membrane conductance, and changes with gating behaviour of an ion channel.
- `Ion transporter <http://en.wikipedia.org/wiki/Ion_transporter>`_
    - Protein embedded in cellular membrane that moves ions *actively*
- `Membrane capacitance <http://www.scholarpedia.org/article/Electrical_properties_of_cell_membranes#Capacitance>`_
- `Membrane conductance <http://www.scholarpedia.org/article/Electrical_properties_of_cell_membranes#Conductance>`_
    - Total membrane conductance is the rate at which current (i.e. ions) can flow through the membrane, and is a result of the configuration of ion channels at a given moment.
- `Membrane potential <https://en.wikipedia.org/wiki/Membrane_potential>`_
    - The difference in electric potential between the exterior and interior of a cell.
- Nernst potential
    - See "Reversal potential".
- `Reversal potential <https://en.wikipedia.org/wiki/Reversal_potential>`_
    - The membrane potential at which a given ion species has no overall flow across the membrane (i.e. the ion flow direction "reverses").
