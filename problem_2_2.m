% Brooke Livingston
% SPCE 5085 OL1 (Summer 2021)    
% 27 June 2021    
% Module 1 Homework  - Problem 2.2

%=========================================================================%
% Clear the workspace and command window
%=========================================================================%
clc
clear

%=========================================================================%
% Calculations
%=========================================================================%
keplers_const = 3.986004418 * 10^5; % km^3 / s^2 
earth_radius = 6378.137; % km
satellite_altitude = 350; % km

% Part C - Oribital velocity in meters per second
orbit_radius = earth_radius + satellite_altitude; % km
% Equation 2.5: v = (u/r)^(1/2)
orbital_velocity_kps = sqrt(keplers_const / orbit_radius); % km/s
oribital_velocity_mps = orbital_velocity_kps * 1000; % m/s

% Part B - Orbital period in minutes
% Equation 2.6: T = (2*pi*r^(3/2)) / (u^(1/2))
orbital_period_secs = (2*pi*orbit_radius^(3/2)) / (keplers_const^(1/2));
orbital_period_mins = orbital_period_secs / 60;

% Part A - Orbital angular velocity in radians per second
orbital_ang_velocity_rps = (2*pi)/(orbital_period_secs);

%=========================================================================%
% Print Results
%=========================================================================%
fprintf('a. The orbital angular velocity is %.6f rad/s\n', orbital_ang_velocity_rps)
fprintf('b. The orbital period is %.2f minutes\n', orbital_period_mins)
fprintf('c. The orbital velocity is %.3f m/s\n', oribital_velocity_mps)




