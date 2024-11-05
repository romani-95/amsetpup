import os
import shutil
import numpy as np
import netCDF4 as nc
import json
import glob

transportfile = sorted(glob.glob('transport_*'))
#print(transportfile)
#transportfile = "transport_31x29x21.json"
res = {}
mob = []
for i, grid in enumerate(transportfile):
    res[grid] = {}
    with open(grid,'r') as f:
        mob_file = json.load(f)
        carrierc = mob_file['doping']
        for i,cc in enumerate(carrierc):
            res[grid][cc] = {}
            mobx = mob_file['mobility']['overall'][i][0][0][0]
            moby = mob_file['mobility']['overall'][i][0][1][1]
            mobz = mob_file['mobility']['overall'][i][0][2][2]
            mob=((mobx+moby+mobz)/3) 
            eh = 'electron' if cc<0 else 'hole'
            res[grid][cc]={'mobx':mobx, 'moby':moby, 'mobz':mobz}

            print("Transport (avg)  after " + grid + " for a carrier concentration of " + str('{:.1E}'.format(cc)))
            print("Mobility results: mob_avg = " + str(np.round(mob,4)) )
