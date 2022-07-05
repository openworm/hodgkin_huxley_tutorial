import scipy as sp
import numpy as np
import pylab as plt
from scipy.integrate import odeint

class HodgkinHuxley():
    """Full Hodgkin-Huxley Model implemented in Python"""

    """ __init__ uses optional arguments """
    """ when no argument is passed default values are used """
    
    def __init__(self, C_m=1, g_Na=120, g_K=36, g_L=0.3, E_Na=50, E_K=-77, E_L=-54.387, t_0=0, t_n=450, delta_t=0.01, I_inj_max=0, I_inj_width=0, I_inj_trans=0):
        
        self.C_m  = C_m                              
        """ membrane capacitance, in uF/cm^2 """
        
        self.g_Na = g_Na                             
        """ Sodium (Na) maximum conductances, in mS/cm^2 """
        
        self.g_K  = g_K                              
        """ Postassium (K) maximum conductances, in mS/cm^2 """
        
        self.g_L  = g_L                              
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

    def I_Na(self, V, m, h):
        """
        Membrane current (in uA/cm^2)
        Sodium (Na = element name)

        |  :param V:
        |  :param m:
        |  :param h:
        |  :return:
        """
        return self.g_Na * m**3 * h * (V - self.E_Na)

    def I_K(self, V, n):
        """
        Membrane current (in uA/cm^2)
        Potassium (K = element name)

        |  :param V:
        |  :param h:
        |  :return:
        """
        return self.g_K  * n**4 * (V - self.E_K)
    #  Leak
    def I_L(self, V):
        """
        Membrane current (in uA/cm^2)
        Leak

        |  :param V:
        |  :param h:
        |  :return:
        """
        return self.g_L * (V - self.E_L)

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
        #advanced input (if checkbox selected)
        elif self.I_inj_width>0:              
            return self.I_inj_max*(t>self.I_inj_trans) - self.I_inj_max*(t>self.I_inj_trans+self.I_inj_width)
        
        #basic input
        else:
            return 10*(t>100) - 10*(t>200) + 35*(t>300) - 35*(t>400)

    @staticmethod
    def dALLdt(X, t, self):
        """
        Integrate

        |  :param X:
        |  :param t:
        |  :return: calculate membrane potential & activation variables
        """
        V, m, h, n = X

        dVdt = (self.I_inj(t) - self.I_Na(V, m, h) - self.I_K(V, n) - self.I_L(V)) / self.C_m
        dmdt = self.alpha_m(V)*(1.0-m) - self.beta_m(V)*m
        dhdt = self.alpha_h(V)*(1.0-h) - self.beta_h(V)*h
        dndt = self.alpha_n(V)*(1.0-n) - self.beta_n(V)*n
        return dVdt, dmdt, dhdt, dndt

    def Main(self):
        """
        Main demo for the Hodgkin Huxley neuron model
        """

        X = odeint(self.dALLdt, [-65, 0.05, 0.6, 0.32], self.t, args=(self,))
        V = X[:,0]
        m = X[:,1]
        h = X[:,2]
        n = X[:,3]
        ina = self.I_Na(V, m, h)
        ik = self.I_K(V, n)
        il = self.I_L(V)

        plt.figure(figsize=[15,10])
        
        ax1 = plt.subplot(4,1,1)
        plt.xlim([np.min(self.t),np.max(self.t)])  #for all subplots
        plt.title('Hodgkin-Huxley Neuron', fontsize = 20)
        plt.plot(self.t, V, 'k')
        plt.ylabel('V (mV)', fontsize = 15)
        

        plt.subplot(4,1,2, sharex = ax1)
        plt.plot(self.t, ina, 'c', label='$I_{Na}$')
        plt.plot(self.t, ik, 'y', label='$I_{K}$')
        plt.plot(self.t, il, 'm', label='$I_{L}$')
        plt.ylabel('Current', fontsize = 15)
        plt.legend(bbox_to_anchor=(1.1, 0.5),loc='center right', fontsize = 15, borderaxespad=0)

        plt.subplot(4,1,3, sharex = ax1)
        plt.plot(self.t, m, 'r', label='m')
        plt.plot(self.t, h, 'g', label='h')
        plt.plot(self.t, n, 'b', label='n')
        plt.ylabel('Gating Value', fontsize = 15)
        plt.legend(bbox_to_anchor=(1.1, 0.5),loc='center right', fontsize = 15, borderaxespad=0)

        plt.subplot(4,1,4, sharex = ax1)
        i_inj_values = [self.I_inj(t) for t in self.t]
        plt.plot(self.t, i_inj_values, 'k')
        plt.xlabel('t (ms)', fontsize = 15)
        plt.ylabel('$I_{inj}$ ($\\mu{A}/cm^2$)', fontsize = 15)
        plt.ylim(-1, 40)

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    runner = HodgkinHuxley()
    runner.Main()
