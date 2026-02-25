import numpy as np
import time

def git_sin_wave_amplitude(freq, time = 0.0):
    s = np.sin(2 * np.pi * freq * time)
    time += 1/freq
    n_ampl = (s + 1) / 2
    return n_ampl

def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1 / sampling_frequency
    time.sleep(sampling_period)

