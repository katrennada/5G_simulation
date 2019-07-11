# -*- coding: utf-8 -*-
"""
Created on Thu July 11 10:52:39 2019
@author: katrennada
"""
def get_numerology_configuration(mu):
    """
    Parameters
    ----------
    mu : int
    Returns
    -------
    numerology_configuration : list
    """
    numerology_configuration = []
    #subcarrier_spacing in KHz
    subcarrier_spacing = (2**mu)*15
    numerology_configuration.append(subcarrier_spacing)
    #nb_slots_per_subframe
    nb_slots_per_subframe = 2**mu
    numerology_configuration.append(nb_slots_per_subframe)
    #nb_slots_per_frame
    nb_subframe_per_frame = 10
    nb_slots_per_frame = nb_slots_per_subframe*nb_subframe_per_frame
    numerology_configuration.append(nb_slots_per_frame)
    #nb_symbols_per_subframe
    nb_symbols_per_slot = 14
    nb_symbols_per_subframe = (2**mu)*nb_symbols_per_slot
    numerology_configuration.append(nb_symbols_per_subframe)
    #nb_max_RB_DL_UL
    if (0 <= mu <=3):
        nb_max_RB_DL_UL = 275
    elif mu == 4:
        nb_max_RB_DL_UL = 138
    numerology_configuration.append(nb_max_RB_DL_UL)
    #list numerology_configuration
    return numerology_configuration


if __name__ == "__main__":
        mu = int(input("Enter numerology "))
        while not(0 <= mu <= 5):
                mu = int(input("Enter numerology (int between 0 and 5) "))
        print(get_numerology_configuration(mu))
