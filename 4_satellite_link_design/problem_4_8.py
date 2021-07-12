#!/usr/bin/env python3

import math

######################################################
# Brooke Livingston
# SPCE 5085 OL1 (Summer 2021)    
# 11 July 2021
# Module 2 Homework  - Problem 4.8
######################################################

def cnr_overall_dB_estimate(cnr_up, cnr_down):
    # Based on section 4.7.1
    cnr_up_down_diff = abs(cnr_up - cnr_down) # dB
    if cnr_up_down_diff == 0:
        return cnr_up - 3.0
    elif cnr_up_down_diff == 10:
        return min(cnr_up, cnr_down) - 0.4 # dB
    elif cnr_up_down_diff >= 20:
        return min(cnr_up, cnr_down)
    else:
        print('No known rules apply to estimating the overall CNR ' \
             f'when the difference is {cnr_up_down_diff} dB')
        return -1

def cnr_overall_dB(cnr_up, cnr_down):
    cnr_ratio_up = (10 ** (cnr_up/10))
    cnr_ratio_down = (10 ** (cnr_down/10))
    # Equation 4.42
    cnr_ratio_overall = round(( 1 / ((1/cnr_ratio_up) + (1/cnr_ratio_down))), 3)
    print(f'The overall CNR ratio is {cnr_ratio_overall}')
    return 10 * math.log10(cnr_ratio_overall) # dB


# Part A - Calculate CNR overall in clear sky Conditions
cnr_up_ca = 24.0
cnr_down_ca = 14.0
print('=== Part A ====================================================')
cnr_o_estimate = cnr_overall_dB_estimate(cnr_up_ca, cnr_down_ca)
print(f'The CNR overall in clear sky conditions estimate is {cnr_o_estimate} dB')
cnr_o = round(cnr_overall_dB(cnr_up_ca, cnr_down_ca), 3)
print(f'The CNR overall in clear sky conditions is {cnr_o} dB')

# Part B - Rain affects the uplink causing 4 dB of attenuation. 
# Calculate the overall (CNR)o at the receiving earth station
print('=== Part B ====================================================')
# Assuming a linear transponder 
cnr_o_up_rain = cnr_o - 4.0 # Equation 4.46 (dB)
cnr_o_up_att = round(cnr_overall_dB(cnr_o_up_rain, cnr_down_ca), 3)
print(f'The CNR overall when rain affects the uplink is {cnr_o_up_att} dB')

# Part C - Rain affects the downlink causing 4 dB of attenuation. 
# Calculate the overall (CNR)o at the receiving earth station
# May need to incorporate atmosphere attenuation (Example 4.9)
print('=== Part C ====================================================')
# Assuming a linear transponder 
k = 1.39 * 10 ** -23 # Boltzmann's contant (J/K)
t_p = 290 # Physical temperature (K)
b_n = 36 * 10 ** 5 # noise bandwith (Hz)
p_n = k * t_p * b_n # Noise Power - Equation 4.12  (W)
print(f'The calculated noise power is {p_n} W')
cnr_o_down_rain = cnr_down_ca - 4.0 - p_n # Equation 4.49 (dB)
cnr_o_down_att = round(cnr_overall_dB(cnr_up_ca, cnr_o_down_rain), 3)
print(f'The CNR overall in when rain affects the downlink is {cnr_o_down_att} dB')
