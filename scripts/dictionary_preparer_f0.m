% This program is to calculate the fundamental frequency using the ZFF
% method. The calculated F0 value is to be used in the unit selection based
% voice

% Clear the workspace
clc; clear all; close all;

% Set the paths to the folders
waves = dir('../wav');
f0path = '../f0';

% Loop through all the waves
for i = 3:length(waves)
    
       i
       % Loops through each file in speaker
        
        reffilename = waves(i).name;
        
        [refstr,tok] = strtok(reffilename,'.');
             
       % Read the wave and apply the diff operation
       
        [y,fs] = wavread(strcat('../wav/', reffilename));       
        y = diff(y);
        y(end+1) = y(end);
        
       % Defining the system parameters
        frSize = 20*(fs/1000);
        frShift = 5*(fs/1000);
        frOvlap = frSize - frShift;
        
        % Calculate the f0
        [f0_y,f0_hy,f0] = f0interp_zff(y,fs,frShift);
       % plot(f0)
        
        % Write in file
        destination = strcat(f0path, '/', refstr, '.f0');
        dlmwrite(destination, f0, 'delimiter', '\n');
        

    
end
