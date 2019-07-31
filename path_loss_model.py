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
    #ksi = np.random.normal(0, sigma**2)
    mu = 0
    x = np.random.randn(10000) * sigma + mu
    ksi = np.mean(x)
    #Omnidirectiona path loss in dB
    path_loss= beta+10*alpha*np.log10(d)+float(ksi)
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

def get_path_loss_ci_model(d,f,n,sigma):
    """
    Parameters
    ----------
    d : distance in meters
    f : frequence in GHz
    n :
    sigma :
    Returns
    -------
    path_loss : Omnidirectional Path loss in dB
    """
    mu = 0
    x = np.random.randn(10000) * sigma + mu
    ksi = np.mean(x)
    #free space path loss in dB
    d0=1
    fspl= 20*np.log10(d0)+20*math.log10(f)+32.45
    path_loss= fspl+10*n*np.log10(d/d0)+float(ksi)
    return(path_loss)

if __name__ == "__main__":
    f = float(input("Enter frequency in GHz "))
    alpha_fi = float(input("Enter alpha_fi "))
    beta_fi = float(input("Enter beta_fi "))
    sigma_fi = float(input("Enter sigma_fi "))

    n_ci = float(input("Enter n_ci "))
    sigma_ci = float(input("Enter sigma_ci "))

    d = np.linspace(30,200,100)
    pl_fi= get_path_loss_fi_model(alpha_fi,beta_fi,sigma_fi)
    pl_ci= get_path_loss_ci_model(d,f,n_ci,sigma_ci)
    fspl= get_free_space_path_loss(d,f)

    plt.semilogx(d,fspl,"^",label="Free space path loss")
    plt.plot(d,pl_fi,label="FI model")
    plt.plot(d,pl_ci, label="CI model")
    plt.title("Path loss = f(d)")
    plt.legend()
    plt.xlabel("Distance (m)")
    plt.ylabel("Path loss (dB)")
    plt.show()
