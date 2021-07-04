% Brooke Livingston
% SPCE 5085 OL1 (Summer 2021)    
% 27 June 2021    
% Module 1 Homework  - Problem 2.11

function azimuth_angle = problem_2_11(lat_s, lon_s, lat_e, lon_e)
% Clear the command window
clc

% Calculate central angle
central_angle = calc_central_angle(lat_s, lon_s, lat_e, lon_e);
fprintf('The central angle is %.3f\n', central_angle);
% Test that the satellite is visible
if (is_satellite_visible(central_angle))
    fprintf('The satellite is visible to the earth station\n');
else
    fprintf('The satellite is NOT visible to the earth station\n');
    fprintf('Will not continue calculating look angles\n');
    return; 
end
% Calculate elevation angle
elevation_angle = calc_elevation_angle(central_angle);
fprintf('The elevation angle is %.3f\n', elevation_angle);
% Calculate intermediate angle
intermediate_angle = calc_intermediate_angle(lon_s, lon_e, lat_e);
fprintf('The intermediate angle is %.3f\n', intermediate_angle);
% Calculate azimuth angle
azimuth_angle = calc_azimuth_angle(lat_s, lon_s, lat_e, lon_e, intermediate_angle);
fprintf('The azimuth angle is %.3f\n', azimuth_angle);

% Equation 2.31
function central_angle = calc_central_angle(lat_s, lon_s, lat_e, lon_e)
    cosd_y = cosd(lat_e) * cosd(lat_s) * cosd(lon_s - lon_e) + ...
             sind(lat_e) * sind(lat_s);
    central_angle = acosd(cosd_y);
end

% Section 2.8.5
function visible = is_satellite_visible(central_angle)
    % Per the book if the satellite is in a nominal GEO orbit than an earth
    % statation is visible to the satellite if the central angle is 
    % postive and less than or equal to 81.3 degrees
    if (central_angle > 0 && central_angle <= 81.3)
        visible = true;
    else
        visible = false;
    end
end

% Equation 2.39
function elevation_angle = calc_elevation_angle(central_angle)
    ratio = 6.6107345;
    a = ratio - cosd(central_angle);
    b = sind(central_angle);
    elevation_angle = atand(a/b) - central_angle;
end

% Equation 2.40
function intermediate_angle = calc_intermediate_angle(lon_s, lon_e, lat_e)
    a = tand(abs(lon_s - lon_e));
    b = sind(lat_e);
    intermediate_angle = atand(a/b);
end

% Equation 2.41a and 2.41b
% Note this problem set is all in the Northern hemisphere this would not
% work for Southern hemisphere calculations 
function azimuth_angle = calc_azimuth_angle(lat_s, lon_s, lat_e, lon_e, intermediate_angle)
    if lat_s < lat_e && lon_s < lon_e
        % satellite is SE of earth station (Eq 2.41a)
        azimuth_angle = 180 - intermediate_angle;
    elseif lat_s < lat_e && lon_s > lon_e
        % satellite is SW of earth station (Eq 2.41b)
        azimuth_angle = 180 + intermediate_angle;
    elseif lat_s < lat_e && lon_s == lon_e
        azimuth_angle = 180;
    else
        fprintf("I don't know what to do!\n");
        azimuth_angle = intermediate_angle;
    end
end

end
