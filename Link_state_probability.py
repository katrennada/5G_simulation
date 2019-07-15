# -*- coding: utf-8 -*-
"""
Created on Thu July 15 09:40:54 2019
@author: katrennada
"""
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import math

def get_link_state_probability(aout,bout,alos):
    """
    Parameters
    ----------
    aout : float
    bout: float
    alos: float
    Returns
    -------
    p_out : Outage probability
    p_los: LOS probability
    p_nlos: NLOS probability
    """
    #Outage probability
    p_out = np.maximum(0,1-np.exp(-aout*d+bout))
    #LOS probability
    p_los = (1-p_out)* np.exp(-alos*d)
    #NLOS probability
    p_nlos = 1-p_out-p_los
    return(p_out,p_los,p_nlos)


if __name__ == "__main__":
    aout = float(input("Enter a_out "))
    bout = float(input("Enter b_out "))
    alos = float(input("Enter a_los "))


    d = np.linspace(0,400,10000)

    #plt.hist( ,normed=1, bins = [0,2,4,6])
    p_out= get_link_state_probability(aout,bout,alos)[0]
    p_los= get_link_state_probability(aout,bout,alos)[1]
    p_nlos= get_link_state_probability(aout,bout,alos)[2]

    plt.plot(d,p_out,label="outage probability")
    plt.plot(d,p_los,label="LOS probability")
    plt.plot(d,p_nlos, label="NLOS probability")
    plt.title("Link state probability = f(d)")
    plt.legend()
    plt.xlabel("Tx-Rx separation (d in m)")
    plt.ylabel("Link state probability")
    plt.show()
