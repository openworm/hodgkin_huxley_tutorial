import sys
import os

# allow importing a module from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from HodgkinHuxley import HodgkinHuxley

runner = HodgkinHuxley(runMode='iclamp', t_n=50, delta_t=0.0125, 
        I_inj_amplitude=66, I_inj_duration=.1, I_inj_delay=30)

runner.simulate()





