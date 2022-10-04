import scipy as sp
import numpy as np
import pylab as plt
from scipy.integrate import odeint
import sys

class HodgkinHuxley():
    """Full Hodgkin-Huxley Model implemented in Python"""

    """ __init__ uses optional arguments """
    """ when no argument is passed default values are used """

    def __init__(self, C_m=1, gmax_Na=120, gmax_K=36, gmax_L=0.3, E_Na=50, E_K=-77, E_L=-54.387, t_0=0, t_n=450, delta_t=0.01, I_inj_max=0, I_inj_width=0, I_inj_trans=0, vc_delay=10, vc_duration=30, vc_condVoltage=-65, vc_testVoltage=10, vc_returnVoltage=-65, runMode='iclamp'):

        self.C_m  = C_m
        """ membrane capacitance, in uF/cm^2 """

        self.gmax_Na = gmax_Na
        """ Sodium (Na) maximum conductances, in mS/cm^2 """

        self.gmax_K  = gmax_K
        """ Postassium (K) maximum conductances, in mS/cm^2 """

        self.gmax_L  = gmax_L
        """ Leak maximum conductances, in mS/cm^2 """

        self.E_Na = E_Na
        """ Sodium (Na) Nernst reversal potentials, in mV """

        self.E_K  = E_K
        """ Postassium (K) Nernst reversal potentials, in mV """

        self.E_L  = E_L
        """ Leak Nernst reversal potentials, in mV """

        self.t    = np.arange(t_0, t_n, delta_t)
        """ The time to integrate over """

        """ Advanced input - injection current (single rectangular pulse only) """

        self.I_inj_max   = I_inj_max
        """ maximum value or amplitude of injection pulse """

        self.I_inj_width = I_inj_width
        """ duration or width of injection pulse """

        self.I_inj_trans = I_inj_trans
        """ strart time of injection pulse or tranlation about time axis """

        #vclamp parameters
        self.run_mode = runMode
        """default is current clamp"""

        self.delay = vc_delay
        """Delay before switching from conditioningVoltage to testingVoltage, in ms"""

        self.duration = vc_duration
        """Duration to hold at testingVoltage, in ms"""

        self.conditioningVoltage = vc_condVoltage
        """Target voltage before time delay, in mV"""

        self.testingVoltage = vc_testVoltage
        """Target voltage between times delay and delay + duration, in mV"""

        self.returnVoltage = vc_returnVoltage
        """Target voltage after time duration, in mV"""

        self.simpleSeriesResistance = 1e7
        """Current will be calculated by the difference in voltage between the target and parent, divided by this value, in mOhm"""

    def alpha_m(self, V):
        """Channel gating kinetics. Functions of membrane voltage"""
        return 0.1*(V+40.0)/(1.0 - np.exp(-(V+40.0) / 10.0))

    def beta_m(self, V):
        """Channel gating kinetics. Functions of membrane voltage"""
        return 4.0*np.exp(-(V+65.0) / 18.0)

    def alpha_h(self, V):
        """Channel gating kinetics. Functions of membrane voltage"""
        return 0.07*np.exp(-(V+65.0) / 20.0)

    def beta_h(self, V):
        """Channel gating kinetics. Functions of membrane voltage"""
        return 1.0/(1.0 + np.exp(-(V+35.0) / 10.0))

    def alpha_n(self, V):
        """Channel gating kinetics. Functions of membrane voltage"""
        return 0.01*(V+55.0)/(1.0 - np.exp(-(V+55.0) / 10.0))

    def beta_n(self, V):
        """Channel gating kinetics. Functions of membrane voltage"""
        return 0.125*np.exp(-(V+65) / 80.0)

    def g_Na(self, m, h):
        """
        Conductance density (in mS/cm^2)
        Sodium (Na = element name)

        |  :param m:
        |  :param h:
        |  :return:
        """
        return self.gmax_Na * m**3 * h

    def I_Na(self, V, m, h):
        """
        Membrane current (in uA/cm^2)
        Sodium (Na = element name)

        |  :param V:
        |  :param m:
        |  :param h:
        |  :return:
        """
        return self.g_Na(m, h) * (V - self.E_Na)


    def g_K(self, n):
        """
        Conductance density (in mS/cm^2)
        Potassium (K = element name)

        |  :param n:
        |  :return:
        """
        return self.gmax_K  * n**4

    def I_K(self, V, n):
        """
        Membrane current (in uA/cm^2)
        Potassium (K = element name)

        |  :param V:
        |  :param n:
        |  :return:
        """
        return self.g_K(n) * (V - self.E_K)

    #  Leak
    def I_L(self, V):
        """
        Membrane current (in uA/cm^2)
        Leak

        |  :param V:
        |  :param h:
        |  :return:
        """
        return self.gmax_L * (V - self.E_L)

    def I_inj(self, t):
        """
        External Current

        |  :param t: time
        |  :return: step up to 10 uA/cm^2 at t>100
        |           step down to 0 uA/cm^2 at t>200
        |           step up to 35 uA/cm^2 at t>300
        |           step down to 0 uA/cm^2 at t>400
        """

        """ running standalone python script """
        if __name__ == '__main__':
            return 10*(t>100) - 10*(t>200) + 35*(t>300) - 35*(t>400)

        #""" running jupyterLab notebook """
        else:
            return self.I_inj_max*(t>self.I_inj_trans) - self.I_inj_max*(t>self.I_inj_trans+self.I_inj_width)

    def I_inj_vclamp(self,t,v):
        """
        External Current (vclamp)

        |  :param t: time
        |  :return: injector current for voltage clamp
        |
        """
        if   t > (self.delay + self.duration):
            current_A = (self.returnVoltage - v) / self.simpleSeriesResistance
        elif t >= self.delay:
            current_A = (self.testingVoltage - v) / self.simpleSeriesResistance
        elif t < self.delay:
            current_A = (self.conditioningVoltage - v) / self.simpleSeriesResistance
        else:
            print('Problem in injection current calculation for voltage clamp...')
            return 0

        #convert current to current density (uA/cm^2)
        current_uA = current_A*10**6        #convert ampere to micro ampere
        surface_area = 1000*10**-8          #surface area of 1000 um^2 converted to cm^2
        current_density = current_uA/surface_area

        return current_density

    @staticmethod
    def dALLdt(X, t, self):
        """
        Integrate

        |  :param X:
        |  :param t:
        |  :return: calculate membrane potential & activation variables
        """
        V, m, h, n = X
        if self.run_mode=='vclamp':
            dVdt = (self.I_inj_vclamp(t,V) - self.I_Na(V, m, h) - self.I_K(V, n) - self.I_L(V)) / self.C_m
        else:
            dVdt = (self.I_inj(t) - self.I_Na(V, m, h) - self.I_K(V, n) - self.I_L(V)) / self.C_m

        dmdt = self.alpha_m(V)*(1.0-m) - self.beta_m(V)*m
        dhdt = self.alpha_h(V)*(1.0-h) - self.beta_h(V)*h
        dndt = self.alpha_n(V)*(1.0-n) - self.beta_n(V)*n
        return dVdt, dmdt, dhdt, dndt

    def Main(self):
        """
        Main demo for the Hodgkin Huxley neuron model
        """
        if __name__ == '__main__':

            self.run_mode='iclamp'

            if '-iclamp' in sys.argv:     #default mode
                self.run_mode='iclamp'
            elif '-vclamp' in sys.argv:
                self.run_mode='vclamp'
                self.t = np.arange(0, 50, 0.0001)           #update default time array for python script (notebook can be controlled through widgets)


        X = odeint(self.dALLdt, [-64.99584, 0.05296, 0.59590, 0.31773], self.t, args=(self,))
        V = X[:,0]
        m = X[:,1]
        h = X[:,2]
        n = X[:,3]
        ina = self.I_Na(V, m, h)
        ik = self.I_K(V, n)
        il = self.I_L(V)
        gna = self.g_Na(m, h)
        gk = self.g_K(n)

        # Save some of the data to file
        with open('hh_py_v.dat','w') as f:
            for ti in range(len(self.t)):
                f.write('%s\t%s\n'%(self.t[ti],V[ti]))

        if not '-nogui' in sys.argv:
            #increase figure and font size for display in jupyter notebook

            fig=plt.figure()

            if __name__ != '__main__':
                plt.rcParams['figure.figsize'] = [8, 6]
                #plt.rcParams['font.size'] = 15
                #plt.rcParams['legend.fontsize'] = 12
                plt.rcParams['legend.loc'] = "upper right"
                fig.canvas.header_visible = False

            ax1 = plt.subplot(5,1,1)
            plt.xlim([np.min(self.t),np.max(self.t)])  #for all subplots
            plt.title('Hodgkin-Huxley Neuron')

            if (self.run_mode=='vclamp'):
                i_inj_values = [self.I_inj_vclamp(t,v) for t,v in zip(self.t,V)]
            else:
                i_inj_values = [self.I_inj(t) for t in self.t]

            plt.plot(self.t, i_inj_values, 'k')
            plt.ylabel('$I_{inj}$ ($\\mu{A}/cm^2$)')
            if (self.run_mode=='vclamp'): plt.ylim(-2000,3000)


            plt.subplot(5,1,2, sharex = ax1)
            plt.plot(self.t, m, 'r', label='m')
            plt.plot(self.t, h, 'g', label='h')
            plt.plot(self.t, n, 'b', label='n')
            plt.ylabel('Gating Variable')
            plt.legend()

            plt.subplot(5,1,3, sharex = ax1)
            plt.plot(self.t, gna, 'c', label='$g_{Na}$')
            plt.plot(self.t, gk, 'y', label='$g_{K}$')
            plt.ylabel('Cond dens')
            plt.legend()

            plt.subplot(5,1,4, sharex = ax1)
            plt.plot(self.t, ina, 'c', label='$I_{Na}$')
            plt.plot(self.t, ik, 'y', label='$I_{K}$')
            plt.plot(self.t, il, 'm', label='$I_{L}$')
            plt.ylabel('Currents')
            plt.legend()

            plt.subplot(5,1,5, sharex = ax1)
            plt.plot(self.t, V, 'k')
            plt.ylabel('V (mV)')
            plt.xlabel('t (ms)')
            #plt.ylim(-1, 40)

            plt.tight_layout()
            plt.show()

if __name__ == '__main__':
    runner = HodgkinHuxley()
    runner.Main()
