#! /usr/bin/env python
#
# Load up DCM.mat, extract features and parameters and save
#
# AS2017



import scipy.io as sio
import sys


inp = sys.argv[1:] # input dataset
D   = sio.loadmat(files,squeeze_me=True,struct_as_record=False)
DCM = D['DCM']

Ep  = DCM.Ep
Hc  = DCM.Hc
Rc  = DCM.Rc
Hz  = DCM.Hz







