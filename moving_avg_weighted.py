#! /usr/bin/env python
''' 
Data smoothing using WEIGHTED Moving Average

[weights that decrease in arithmetical progression]

inp[0] = somthing.csv
inp[1] = window size
inp[2] = output name [as csv] [optional]

AS 
'''

import sys
import os
import csv

import numpy as np
import os.path
import math

#------------------------------------

inp      = sys.argv[1:]

if len(inp) < 2:
    W = 3
else:
    W = int(inp[1])


if os.path.isfile(inp[0]):
    file = csv.reader(open(inp[0],'r'))
    x    = []
    for row in file:
        x = np.array([float(i) for i in row])

S = np.std(x)
for n, i in enumerate(x):
    if n < math.floor(W*.5):
        ind  = np.arange(n,W)
        
    elif n >= len(x)-math.ceil(W*.5):
        ind = np.arange(W)+len(x)-W
          
    else:
        ind  = np.arange(W)+n-1
    
    # linear weights that decrease
    r = np.arange(len(x))
    r = r[::-1]
    r = r / r.max() # normalise so we don't inflate amplitudes
    
    win  = x[ind]*r[ind]
    x[n] = win.mean()

if len(inp) < 3:
    print(x)
else:
    fO = inp[2]
    x.tofile(fO,sep=',',format='%10.5f')