# -*- coding: utf-8 -*-
"""
Created on Thu July 15 11:45:22 2019
@author: katrennada
"""
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import math

def get_spectral_efficiency(snr):
    """
    Parameters
    ----------
    snr : Signal/Noise Ratio in dB (float)
    Returns
    -------
    spectral_efficiency : Spectral efficiency in bps/Hz
    """
    #Maximum spectral efficiency in bps/Hz
    rho_max = 4.8
    #Loss factor in dB
    delta = 3
    #Spectral efficiency in bps/Hz
    rho = np.minimum(np.log2(1+10**(0.1*(snr-delta))),rho_max)
    return(rho)


if __name__ == "__main__":

    snr = np.linspace(-15,20,10000)

    #plt.hist( ,normed=1, bins = [0,2,4,6])
    rho= get_spectral_efficiency(snr)

    plt.plot(snr,rho)
    plt.title("Spectral efficiency = f(SNR)")
    plt.legend()
    plt.xlabel("SNR in dB")
    plt.ylabel("Spectral efficiency in bps/Hz")
    plt.show()
