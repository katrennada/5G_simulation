# -*- coding: utf-8 -*-
"""
Created on Thu July 11 14:03:52 2019
@author: katrennada
"""
from numerology_configuration import get_numerology_configuration

def get_bandwidth(mu,nc):
    """
    Parameters
    ----------
    mu : int
    nc : int carrier aggregation
    Returns
    -------
    bandwidth : int
    """
    #bandwidth in MHz
    nb_subcarrier_per_rb=12
    bandwidth = (10**(-3))*get_numerology_configuration(mu)[4]*nb_subcarrier_per_rb*nc*get_numerology_configuration(mu)[0]/0.9
    return int(bandwidth)


if __name__ == "__main__":
        mu = int(input("Enter numerology "))
        while not(0 <= mu <= 5):
                mu = int(input("Enter numerology (int between 0 and 5) "))
        nc = int(input("Enter N Carrier Aggregation "))
        while not(1 <= nc <= 16):
                mu = int(input("Enter numerology (int between 1 and 16) "))
        print("The bandwidth is ",get_bandwidth(mu,nc)," MHz")
