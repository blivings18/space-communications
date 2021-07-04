#!/usr/bin/env python3

######################################################
# Brooke Livingston
# SPCE 5085 OL1 (Summer 2021)    
# 27 June 2021    
# Module 2 Homework  - Problem 4.1
######################################################

import math

def calculate_wavelength(frequency_ghz):
    speed_of_light = 3.0 * 10**8 # m/s
    frequency_hz = frequency_ghz * 10**9 # hz
    return speed_of_light / frequency_hz # m

def calculate_path_loss(distance_km, frequency_ghz):
    wavelength = calculate_wavelength(frequency_ghz)
    print(f'The wavelength at {frequency_ghz} GHz is {wavelength} m')
    distance_m = distance_km * 1000
    # Equation 4.11
    return 20 * math.log10((4 * math.pi * distance_m) / wavelength)

distance = 38500.0 # km
path_loss_four_ghz = round(calculate_path_loss(distance, 4.0), 3)
print(f'The path loss at 4.0 GHz frequency is {path_loss_four_ghz} dB')
path_loss_six_ghz_1 = round(calculate_path_loss(distance, 6.0), 3)
print(f'The path loss at 6.0 GHz frequency is {path_loss_six_ghz_1} dB')
# Since we have already calculated decibels for 4 GHz we can add 20 log (6/4) 
# to find the path loss at 6 GHz 
path_loss_six_ghz_2 = round(path_loss_four_ghz + (20 * math.log10(6/4)), 3)
print(f'The path loss at 6.0 GHz frequency is {path_loss_six_ghz_2} dB')
