.. Hodgkin Huxley LEMS Tutorial documentation master file, created by
   sphinx-quickstart on Sat Dec 20 13:20:26 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Hodgkin Huxley Tutorial
===============================================

This tutorial gives an introduction to the `Hodgkin-Huxley model <https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model>`_ by use of executable example implementations in Python and `NeuroML <http://www.neuroml.org>`_. 


**The aims of this tutorial are:**

1) Provide `a guide <_static/Tutorial.html>`_ to implementing the Hodgkin-Huxley model using both `Python <https://www.python.org/>`_ and a `NeuroML2 implementation <http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00079/abstract>`_ of the same equations.
2) Give some background information on the `electrophysiology <_static/Electrophysiology.html>`_ underlying the Hodgkin-Huxley model.

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
biology, take a look at the `Electrophysiology page <_static/Electrophysiology.html>`_. 

After you understand the electronic model there, check out the 
`code walkthrough <_static/Tutorial.html>`_ to see an example
implementation of the Hodgkin-Huxley model in Python, using a cell
modeled in `NeuroML2 <https://www.neuroml.org/neuromlv2>`_.

You can look at the `current-voltage characteristic page <_static/iv_curve.html>`_
to get an understanding of another biological-electronic equivalence
that is useful in describing ion channel and cell models.

There are also some `exercises <_static/Exercises.html>`_ you can complete to get a feel for the model. These 
can be completed using either the Python or NeuroML versions.

Table of Contents:

.. toctree::
   :maxdepth: 4

   _toc/Tutorial
   _toc/Electrophysiology
   _toc/iv_curve
   _toc/Exercises
   _toc/Source

