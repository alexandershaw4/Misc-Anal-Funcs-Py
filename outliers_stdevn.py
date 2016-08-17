#! /usr/bin/env python
''' 
Replace values i > ( n * standard deviation ) with i / sample mean

inp[0] = csv inp dataset
inp[1] = csv out dataset
inp[2] = n [optional: def = 3]

AS 
'''

import sys
import os
import csv

import numpy as np
import os.path

inp = sys.argv[1:]

if len(inp) == 2:
    N = inp[2]
else:
    N = 3

if os.path.isfile(inp[0]):
    file = csv.reader(open(inp[0],'r'))
    x    = []
    for row in file:
        x = np.array([float(i) for i in row])

ox = x.copy()

for n, i in enumerate(x):
    if i > (x.std()*N):
        #x[n] = x.mean()
        x[n] = i / x.mean()

fO = inp[1]
x.tofile(fO,sep=',',format='%10.5f')