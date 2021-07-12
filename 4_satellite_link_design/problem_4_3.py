#!/usr/bin/env python3

######################################################
# Brooke Livingston
# SPCE 5085 OL1 (Summer 2021)    
# 11 July 2021
# Module 2 Homework  - Problem 4.3
######################################################

# noise_figure = 16.0 dB
# 16.0 = 10 * math.log10(noise_factor)
noise_factor = round(10 ** 1.6, 3)
print(f'The noise factor is {noise_factor}')
# Reference Temperature (K)
t_o = 290 
# Equation 4.24
noise_temperature = round(t_o * (noise_factor - 1), 3)
print(f'The noise temperature is {noise_temperature} K')
