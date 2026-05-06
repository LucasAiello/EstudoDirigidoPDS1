# Atividade 4
# 3 - Modifique a entrada para x[n] = {1, 1, 1, 1} e interprete o novo resultado.
clc;
clear ;
close all ;
x = [1 1 1 1];
h = [1 1];
y = conv (x , h) ;
disp ('Sequencia x[n]: ');
disp (x) ;
disp ('Sequencia h[n]: ');
disp (h) ;
disp ('Convolucao y[n] = x[n] * h[n]: ') ;
disp (y) ;
n = 0: length ( y) -1;
stem (n ,y ,'filled');
grid on ;
xlabel ('n');
ylabel ('y[n]') ;
title ('Resultado da convolucao discreta');