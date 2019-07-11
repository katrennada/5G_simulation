# -*- coding: utf-8 -*-
"""
Created on Thu July 11 14:29:33 2019
@author: katrennada
"""
from numerology_configuration import get_numerology_configuration
from bandwidth import get_bandwidth

def get_throughput(mu,nc,mimo,modulation):
    """
    Parameters
    ----------
    mu :int (numerology)
    nc: N carrier aggregation
    mimo : MIMO configuration
    modulation : BPSK, QPSK, 16QAM, 64QAM, 256QAM
    Returns
    -------
    throughput : float
    """
    #throughput in Gbps
    nb_frame_per_sec=100
    nb_subcarrier_per_rb=12
    nb_symbols_per_slot=14
    max_symbols_per_sec = nc*nb_frame_per_sec*get_numerology_configuration(mu)[2]*get_numerology_configuration(mu)[4]*nb_subcarrier_per_rb*nb_symbols_per_slot
    if (modulation == "BPSK"):
        nb_bits_per_symbol=1
    elif (modulation == "QPSK"):
        nb_bits_per_symbol=2
    elif (modulation == "16QAM"):
        nb_bits_per_symbol=4
    elif (modulation == "64QAM"):
        nb_bits_per_symbol=6
    elif (modulation == "256QAM"):
        nb_bits_per_symbol=8
    throughput = (max_symbols_per_sec*mimo*nb_bits_per_symbol)*(10**(-9))
    return round (throughput,2)


if __name__ == "__main__":
    mu = int(input("Enter numerology "))
    while not(0 <= mu <= 5):
        mu = int(input("Enter numerology (int between 0 and 5) "))

    nc = int(input("Enter N Carrier Aggregation "))
    while not(1 <= nc <= 16):
        mu = int(input("Enter numerology (int between 1 and 16) "))

    mimo = int(input("Enter MIMO configuration "))
    while not((mimo==2) or (mimo==4) or (mimo==8) or (mimo==24)):
        mimo = int(input("Enter MIMO configuration "))

    modulation = input("Enter modulation ")
    while not((modulation=="BPSK") or (modulation=="QPSK") or (modulation=="16QAM") or (modulation=="64QAM") or (modulation=="256QAM")):
        modulation = input("Enter modulation ")

    print("The theoretical throughput is ",get_throughput(mu,nc,mimo,modulation)," Gbps")
