.. Hodgkin Huxley LEMS Tutorial documentation master file, created by
   sphinx-quickstart on Sat Dec 20 13:20:26 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Hodgkin Huxley NeuroML/LEMS Tutorial
===============================================

This tutorial demonstrates a side-by-side comparison of Python code that runs the `Hodgkin-Huxley equations <https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model>`_ and generates plots with a `NeuroML2 implementation <http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00079/abstract>`_ of the same equations.

This was originally created by `@joebowen <https://github.com/joebowen>`_ on behalf of the `OpenWorm project <http://www.openworm.org>`_.

What is the Hodgkin-Huxley model?
=================================

`From Wikipedia <https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model>`_: 
The Hodgkin–Huxley model is a mathematical model that describes how action potentials in neurons 
are initiated and propagated.

The model describes represents the electrical properties of
excitable membranes as typical electrical circuit components. For instance,
the cell's membrane is modeled as a capacitor, and voltage-dependent 
conductances stand in for what are now known to be voltage-gated ion
channels.

For a detailed run through of the Hodgkin-Huxley model's electronics, math and 
biology, take a look at the `Electrophysiology page <_static/electrophysiology.html>`_. 

After you understand the electronic model there, check out the 
`code walkthrough <_static/Tutorial.html>`_ to see an example
implementation of the Hodgkin-Huxley model in Python, using a cell
modeled in `NeuroML2 <https://www.neuroml.org/neuromlv2>`_.

Finally, you can look at the `current-voltage characteristic page <_static/iv_curve.html>`_
to get an understanding of another biological-electronic equivalence
that is useful in describing ion channel and cell models.

Table of Contents:

.. toctree::
   :maxdepth: 4

   _static/Tutorial
   _static/Electrophysiology
   _static/iv_curve
   _static/Source

