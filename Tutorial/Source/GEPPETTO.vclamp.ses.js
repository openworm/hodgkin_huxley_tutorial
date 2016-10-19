/*****

A file to create info widgets, plots, save variables etc. in OSB

*****/

G.addWidget(Widgets.POPUP);
Popup1.setMessage("The <b>Hodgkin-Huxley model</b> is a mathematical model that describes how action potentials in neurons are initiated and propagated. It is a set of nonlinear     differential equations that approximates the electrical characteristics of excitable cells such as neurons. <br/><br/>You can run your own simulations of this model by signing up to OSB and logging in. <br/><br/>There is also <a target='_blank' href='http://hodgkin-huxley-tutorial.readthedocs.io/en/latest/'>a tutorial for the HH model</a>, which has been developed as part of the <a target='_blank' href='http://www.openworm.org/'>OpenWorm project</a>.");
Popup1.setName("Description");
Popup1.setPosition(1074,142)
Popup1.setSize(391.8,454.8)


var Plot1 = G.addWidget(Widgets.PLOT);
Plot1.setName("Hodgkin-Huxley Spiking Neuron");

Plot1.setPosition(120, 90);
Plot1.setSize(230,465);
Plot1.plotData(HHCellVClamp.hhpop[0].v);

var Plot2 = G.addWidget(Widgets.PLOT);

Plot2.setName("Gating Variables");
Plot2.setPosition(120,350);
Plot2.setSize(285,465)
Plot2.plotData(HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.naChans.naChan.h.q);
Plot2.plotData(HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.naChans.naChan.m.q);
Plot2.plotData(HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.kChans.kChan.n.q);

Plot2.setLegend(HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.naChans.naChan.h.q,"Sodium h.q");
Plot2.setLegend(HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.naChans.naChan.m.q,"Sodium m.q");
Plot2.setLegend(HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.kChans.kChan.n.q,"Potassium n.q");

HHCellVClamp.hhpop[0].v.setWatched(true);
HHCellVClamp.hhpop[0].bioPhys1.membraneProperties.naChans.naChan.m.q.setWatched(true);
