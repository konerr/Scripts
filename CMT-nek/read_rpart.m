%%
% In the rpart* files, each particle has 42 entries each of size 'prec'
% with the very first entry being the total no.of particles.
% DATA LAYOUT
% Particle Position [ x  y  z] = rows 2 3 4 , 5-13 history values
% Particle Velocity [vx vy vz] = rows 14 15 16, 17-25 history values
% Fluid Velocity    [ux uy uz] = rows 26 27 28, 29-37 history values
% Diameter = row 38
% Super-particle loading = row 39
% Temperature = row 40
% Particle id = rows 41 42 43

prec = 'real*4'; % Prescision
fid2 = fopen('rpart00001');

f = fread(fid2,prec);  % Binary read
npcls = f(1);          % No.of pcls
x = f(2:42:length(f)); % x-coords
y = f(3:42:length(f)); % y-coords
z = f(4:42:length(f)); % z-coords
xyz = [x y z];

fclose('all');