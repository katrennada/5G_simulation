# -*- coding: utf-8 -*-
"""
Created on Thu July 11 17:00:03 2019
@author: katrennada
"""
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import math

def get_path_loss_fi_model(alpha,beta,sigma):
    """
    Parameters
    ----------
    alpha : least square fit of floating intercept
    beta: least square fit of slope
    sigma: lognormal shadowing variance
    Returns
    -------
    path_loss : Omnidirectional Path loss in dB
    """
    #ksi variable aléatoire suit une loi normale de moyenne 0 et variance sigma^2
    ksi = np.random.normal(0, sigma**2)
    #Omnidirectiona path loss in dB
    path_loss= alpha+10*beta*np.log10(d)+float(ksi)
    return(path_loss)

def get_free_space_path_loss(d,f):
    """
    Parameters
    ----------
    d : distance in meters
    f : frequence in GHz
    Returns
    -------
    fspl : Free space path loss in dB
    """
    #free space path loss in dB
    fspl= 20*np.log10(d)+20*math.log10(f)+32.45
    return(fspl)


if __name__ == "__main__":
    f = float(input("Enter frequency in GHz "))
    alpha = float(input("Enter alpha "))
    beta = float(input("Enter beta "))
    sigma = float(input("Enter sigma "))

    alpha1 = float(input("Enter alpha1 "))
    beta1 = float(input("Enter beta1 "))
    sigma1 = float(input("Enter sigma1 "))

    d = np.linspace(30,200,10000)
    pl= get_path_loss_fi_model(alpha,beta,sigma)
    pl1= get_path_loss_fi_model(alpha1,beta1,sigma1)
    fspl= get_free_space_path_loss(d,f)

    plt.semilogx(d,fspl,label="Free space path loss")
    plt.plot(d,pl,label="LOS")
    plt.plot(d,pl1, label="NLOS")
    plt.title("Path loss = f(d)")
    plt.legend()
    plt.xlabel("Distance (m)")
    plt.ylabel("Path loss (dB)")
    plt.show()
