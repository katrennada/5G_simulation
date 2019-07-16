# -*- coding: utf-8 -*-
"""
Created on Thu July 16 09:50:08 2019
@author: katrennada
"""
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import math
from number_of_clusters import get_number_of_clusters

def get_cluster_power_fraction(r,sigma):
    """
    Parameters
    ----------
    r : float
    sigma : float
    Returns
    -------
    gamma: power fraction
    """
    #z variable aléatoire suit une loi normale de moyenne 0 et variance sigma^2
    z = np.random.normal(0,sigma**2)
    #u suit une loi uniforme sur [0,1]
    u = np.random.uniform(0, 1)
    #fraction de puissance
    gamma = (u**(r-1))*(10**(0.1*z))
    return(float(gamma))

def get_normalized_cluster_power_fraction(t,k):
    """
    Parameters
    ----------
    t : list containing power fractions of all clusters
    k : number of clusters
    Returns
    -------
    normalized_t: list containing normalized power fractions of all clusters
    """
    #somme des fractions de puissance
    s=0
    for i in range (0,k):
        s=s+t[i]
    #fractions de puissance normalisées
    normalized_t=[]
    for i in range (0,k):
        normalized_t.append(t[i]/s)
    return(normalized_t)



if __name__ == "__main__":
    r = float(input("Enter r "))
    sigma = float(input("Enter sigma "))
    l = float(input("Enter l "))

    k = get_number_of_clusters(l)
    t=[]
    for i in range (0,k):
        p=get_cluster_power_fraction(r,sigma)
        t.append(p)
    normalized_t = get_normalized_cluster_power_fraction(t,k)

    print("Number of clusters: ", k)
    print("Normalized fractions of power are: ", normalized_t)
