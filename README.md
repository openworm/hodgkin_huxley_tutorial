## Hodgkin Huxley Tutorials

This repository contains the code for a number of related tutorials on the Hodgkin Huxley model

### Tutorial 1A: HH model in Python and NeuroML

*Target audience: those who want to learn how to implement the HH model*

This tutorial contains a side-by-side comparison of Python code that runs the [Hodgkin-Huxley equations](https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model) and generates plots with a [NeuroML2 implementation](http://journal.frontiersin.org/Journal/10.3389/fninf.2014.00079/abstract) of the same equations.  

This was originally created by [@joebowen](https://github.com/joebowen) on behalf of the [OpenWorm project](http://www.openworm.org).  

The latest version of the tutorial is visible [online at ReadTheDocs](http://hodgkin-huxley-tutorial.readthedocs.org/en/latest/).

### Tutorial 1B: Interactive introduction to the HH model in a Jupyter notebook

*Target audience: those who want to simulate the HH model using an interactive Python based web notebook*

This interactive [Jupyter notebook](https://jupyter.org/) can be used to run the Python version of the HH model from above, change the parameters of the model and display the dynamical properties of variables, without the need to write any code.

<p align="center"><kbd><a href="https://github.com/openworm/hodgkin_huxley_tutorial/blob/master/notebooks/Python_HH_version/README.md"><img src="https://raw.githubusercontent.com/openworm/hodgkin_huxley_tutorial/master/notebooks/HH_Jupyter.png" width="600"/></kbd></p>

Full details can be found [here](https://github.com/openworm/hodgkin_huxley_tutorial/blob/master/notebooks/Python_HH_version/README.md). This work was carried out as part of [Google Summer of Code 2022 by Rahul Sonkar](notebooks/GSoC_2022_Submission/GSoC_Documentation.md).

### Tutorial 2: Interactive introduction to the HH model on Open Source Brain

*Target audience: those who want to learn the basics of the HH model through running in-browser simulations*

This tutorial also uses the NeuroML model from above, but provides a high level introduction to the concepts of the model (as well as computational modelling in neuroscience).

It can be accessed on the Open Source Brain site at this location: http://www.opensourcebrain.org/tutorials. It is built on the [Geppetto platform](http://www.geppetto.org/), which was also initially developed in the OpenWorm project.

![HH](https://raw.githubusercontent.com/openworm/hodgkin_huxley_tutorial/master/Tutorial2/NeuroML2/images/HH_OSB.png)

See also http://www.opensourcebrain.org/projects/hodgkin-huxley-tutorial.

[![Continuous build using OMV](https://github.com/openworm/hodgkin_huxley_tutorial/actions/workflows/main.yml/badge.svg)](https://github.com/openworm/hodgkin_huxley_tutorial/actions/workflows/main.yml) [![Non OMV tests](https://github.com/openworm/hodgkin_huxley_tutorial/actions/workflows/non-omv.yml/badge.svg)](https://github.com/openworm/hodgkin_huxley_tutorial/actions/workflows/non-omv.yml)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1493456.svg)](https://doi.org/10.5281/zenodo.1493456)



### Reusing this model

The code in this repository is provided under the terms of the [software license](LICENSE) included with it. If you use this model in your research, we respectfully ask you to cite the references outlined in the [CITATION](CITATION.md) file.
