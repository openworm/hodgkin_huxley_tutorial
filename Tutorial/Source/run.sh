#!/bin/bash

#################################################
# LEMS Hodgkin Huxley Neuron Model
#
# Command to run LEMS_HH_Simulation.xml script on Linux/Mac
#
# Usage: ./run.sh
#
#################################################

set -e
java -jar jNeuroML-0.7.2-jar-with-dependencies.jar LEMS_HH_Simulation.xml