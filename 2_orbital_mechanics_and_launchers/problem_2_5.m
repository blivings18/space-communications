% Brooke Livingston
% SPCE 5085 OL1 (Summer 2021)    
% 27 June 2021    
% Module 1 Homework  - Problem 2.5

%=========================================================================%
% Clear the workspace and command window
%=========================================================================%
clc
clear

%=========================================================================%
% Calculations
%=========================================================================%
apogee_height = 5000; % km
perigee_height = 800; % km
earth_radius = 6378.137; % km

% From Example 2.5
% 2a = 2re + 2hp + 2ha
a = ((2*earth_radius) + apogee_height + perigee_height) / 2; % km
eccentricity = 1 - ((earth_radius + perigee_height) / a); 

%=========================================================================%
% Print Results
%=========================================================================%
fprintf('The eccentricity of the orbit is %.3f\n', eccentricity);
