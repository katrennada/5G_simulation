# -*- coding: utf-8 -*-
"""
Created on Thu July 16 14:38:40 2019
@author: katrennada
"""
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import math
from scipy.stats import expon

def get_angular_spread(l_1):
    """
    Parameters
    ----------
    l_1: float in degrees
    Returns
    -------
    rms: angular spread in degrees
    """
    #angular spread in degrees
    rms=expon.rvs(scale=l_1)
    print ("Angular spread in degrees is ", rms)
    #Distribution of the rms angular spreads
    abs=np.linspace(0,60,1000)
    plt.plot(abs,expon.cdf(abs,scale=l_1))
    plt.title("Distribution of the rms angular spreads")
    plt.xlabel("Angular std dev (deg)")
    plt.ylabel("Cumm prob")
    plt.grid()
    plt.show()
    return(rms)


if __name__ == "__main__":
    l_1 = float(input("Enter l_1 "))
    get_angular_spread(l_1)
