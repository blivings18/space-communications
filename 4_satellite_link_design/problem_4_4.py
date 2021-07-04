#!/usr/bin/env python3

import math

######################################################
# Brooke Livingston
# SPCE 5085 OL1 (Summer 2021)    
# 27 June 2021    
# Module 2 Homework  - Problem 4.4
######################################################

# Part A
antenna_gain = 34 #dB
system_noise_temp = 10 * math.log10(80) # dBK
antenna_gain_to_noise_temp = round(antenna_gain - system_noise_temp, 3)
print(f'A. G/T is {antenna_gain_to_noise_temp} dB/K')

# Part B
antenna_gain = 34 #dB
system_noise_temp = 10 * math.log10(200) # dBK
antenna_gain_to_noise_temp = round(antenna_gain - system_noise_temp, 3)
print(f'B. G/T is {antenna_gain_to_noise_temp} dB/K')
