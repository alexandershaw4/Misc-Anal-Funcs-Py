#! /usr/bin/env python
''' 
Amplitude scaling tool for timeseries | vector, x

First input is a CSV file
Second argument is method [optional]:

 1 = scale between 0-1. [default]
 2 = divide by maximum.
 3 = mean correct and divide by std. 
 4 = mean correct.
 5 = scale approx [-1 1]
 6 = scale between [-n and n]*
 7 = scale by unit length (./norm(x))

AS 
'''

import sys
import os
import csv

import numpy as np
import os.path


#------------------------------------

inp      = sys.argv[1:]

if len(inp) == 3:
    n = inp[2]
else:
    n = 1
    
if len(inp) > 1:
    mth = int(inp[1])
else: 
    mth = 1

def T(x):
    return {
    1 : 'Def',
    2 : 'Max',
    3 : 'Std',
    4 : 'Mean',
    5 : 'minusone',
    6 : 'between',
    7 : 'norm',
    }[x]


if os.path.isfile(inp[0]):
    file = csv.reader(open(inp[0],'r'))
    x    = []
    for row in file:
        x = np.array([float(i) for i in row])

def f(t):
    return {
    'Def'      :  (x-x.min())/(x.max()-x.min()),
    'Max'      :  x / x.max(),
    'Std'      :  (x - x.mean()) / x.std(),
    'Mean'     :  x - x.mean(),
    'minusone' :  (x - x.mean()) / x.max(),
    'between'  :  -n + (abs(n)*2)*(x - x.min())/(x.max()-x.min()),
    'norm'     :  x / np.linalg.norm(x),        
        }[t]

print(f(T(int(mth))))
