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

def get_path_loss_atm_model(alpha,beta,sigma,mu, ksi,k,r_i):
    """
    Parameters
    ----------
    alpha : least square fit of floating intercept
    beta: least square fit of slope
    sigma: lognormal shadowing variance
    mu : rain attenuation factor
    ksi :
    k : oxygen absorption
    r_i:rain fall intensity in mm/h
    Returns
    -------
    path_loss_atm : Omnidirectional Path loss in dB
    """
    #path loss without taking atmosphere conditions in consideration
    pl_fi= get_path_loss_fi_model(alpha,beta,sigma)
    #
    path_loss_atm= pl_fi+mu*(r_i**ksi)*d*0.001+ k*d*0.001
    return(path_loss_atm)

if __name__ == "__main__":
    f = float(input("Enter frequency in GHz "))
    alpha = float(input("Enter alpha "))
    beta = float(input("Enter beta "))
    sigma = float(input("Enter sigma "))

    mu = float(input("Enter mu "))
    ksi = float(input("Enter ksi "))
    k = float(input("Enter k "))
    r_i = float(input("Enter rain fall intensity "))

    d = np.linspace(30,200,100)
    pl_fi= get_path_loss_fi_model(alpha,beta,sigma)
    pl_atm= get_path_loss_atm_model(alpha,beta,sigma,mu,ksi,k,r_i)
    fspl= get_free_space_path_loss(d,f)

    plt.semilogx(d,fspl,"^",label="Free space path loss")
    plt.plot(d,pl_fi,label="FI model")
    plt.plot(d,pl_atm, label="atm model")
    plt.title("Path loss = f(d)")
    plt.legend()
    plt.xlabel("Distance (m)")
    plt.ylabel("Path loss (dB)")
    plt.show()
