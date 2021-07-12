#!/usr/bin/env python3

import math

######################################################
# Brooke Livingston
# SPCE 5085 OL1 (Summer 2021)    
# 11 July 2021    
# Module 2 Homework  - Problem 4.2
######################################################

# Flux Density 
pt_gt = 1.0 * 35.0 # dBW
r = 500 * 1000 # m
# Equation 4.3
f = (10 * math.log10(pt_gt)) - (20 * math.log10(r) - (10 * math.log10(4 * math.pi)))
f_rounded = round(f, 3)
print(f'The flux density is {f_rounded} dB/m^2')

# Power received by tracking antenna
# Equation 4.7
# Gain = (4 * pi * antenna_effective_area) / wavelength ^ 2
# antenna_effective_area = (Gain * wavelength ^ 2) / (4 * pi)
g = 30.0 # dB
wavelength = 0.1 # m
a_e = (g * (wavelength ** 2) / (4 * math.pi))
a_e_rounded = round(a_e, 3) # m^2
print(f'The antenna effective area is {a_e_rounded} m^2')
# Equation 4.6
p_r = f + a_e
p_r_rounded = round(p_r, 3) # dbW
print(f'The power received is {p_r_rounded} dbW')
