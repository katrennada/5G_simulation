# -*- coding: utf-8 -*-
"""
Created on Thu July 15 14:50:05 2019
@author: katrennada
"""
import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
import math

def get_number_of_clusters(l):
    """
    Parameters
    ----------
    l : float
    Returns
    -------
    number_of_clusters : Number of detected clusters
    """
    number_of_clusters = np.maximum(np.random.poisson(l),1)
    return(number_of_clusters)


if __name__ == "__main__":

    l = float(input("Enter l "))
    number_of_clusters = get_number_of_clusters(l)
    print ("Le nombre de clusters est: ", number_of_clusters)
