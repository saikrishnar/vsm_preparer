% This program concatenates the units based on Viterbi algorithm with
% duration as target cost and pitch as join cost.
% Source : Enhancements of Viterbi Search for Fast Unit Selection Synthesis INTERSPEECH 2010


% Clear the workspace
clc; clear all; close all;


% Load a test sentence
fid = fopen('../test/phones.phone');
phones = textscan(fid, '%s');
fclose(fid);
test_phones = phones{1};
durations_frame = load('../test/durations.phone');
start_frame = durations_frame(:,1);
end_frame = durations_frame(:,2);
duration_frame = end_frame - start_frame;
test_durations_time = duration_frame*80/16;

% Load the Mean Durations
fid = fopen('../mean/phones.dict');
phones_mean = textscan(fid, '%s');
fclose(fid);
mean_duration = load('../mean/durations.dict');

% Load the Dictionary
fid = fopen('../dictionary/phones.dict');
phones_dict = textscan(fid, '%s');
fclose(fid);
temp = phones_dict{1};
feats_dict = load('../dictionary/feats.dict');
start_frame = feats_dict(:,1);
end_frame = feats_dict(:,2);
duration_frame = end_frame - start_frame;
dict_durations_time = duration_frame*80/16;
dict_f0_start = feats_dict(:,7);
dict_f0_end = feats_dict(:,8);









% Start the Viterbi Algorithm
p = 0;
TC = {};
Cstar = {};
% Step 1:   Initiate the first unit
for i = 1:length(test_phones)
    
    unit = test_phones(i);
    if strmatch(unit, 'SIL')
        p = p + 1;
    else
        unit
        unit_examples =  temp(strmatch(unit,temp));
        unit_durations = dict_durations_time(strcmp(unit,temp));
        TC = [ TC (unit_durations - mean(unit_durations)) ] ;
        Cstar = TC;
        break;
        
    end
end

p = p  + 1;



%  Step 2:    Compute the cost for all the other units
for i = p+1 : length(test_phones) - 1
    % Concatenation Cost
    % Loop through all the k instants of the current unit and all the l units of the next unit
    current_unit = test_phones(i)
    currentunit_examples = temp(strcmp(current_unit,temp));
    currentunit_f0 = dict_f0_end(strcmp(current_unit,temp));
    currentunit_duration = dict_durations_time(strcmp(current_unit,temp));
    
    next_unit = test_phones(i+1);
    nextunit_examples = temp(strcmp(next_unit,temp));
    nextunit_f0 = dict_f0_start(strcmp(next_unit,temp));
    
    joincostmatrix = compute_joincostmatrix( currentunit_f0, nextunit_f0);
    
    % Calculate the TC
    
    TC = [ TC (currentunit_duration - mean(currentunit_duration))];
    
    
    pause; 
   

end


