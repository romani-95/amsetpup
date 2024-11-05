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
    
            eh = 'electron' if cc<0 else 'hole'
            res[grid][cc]={'mobx':mobx, 'moby':moby, 'mobz':mobz}

for cc in res[grid]:
    mob_x = []
    mob_y = []
    mob_z = []
    mob = []
    for grid in res:
        mob_x.append(res[grid][cc]['mobx'])
        mob_y.append(res[grid][cc]['moby'])
        mob_z.append(res[grid][cc]['mobz'])
        mob.append((res[grid][cc]['mobx']+res[grid][cc]['moby']+res[grid][cc]['mobz'])/3)
    converged = False
    i_converged = 1000
    #print(mob)
    if len(mob) >= 3:
        for i, mu in enumerate(mob[2:]):
            i = i + 2
            mu_1 = mob[i-1]
            mu_2 = mob[i-2]
            diff1 = np.abs((mu_2 - mu_1)/mu_1) # entre points -2 et -1
            diff2 = np.abs((mu_1 - mu)/mu) # entre points -1 et 0
            diff3 = np.abs((mu_2 - mu)/mu) # entre points -2 et 0
            max_error = max([diff1, diff2, diff3])
            soft_tol = 0.05
            hard_tol = 0.05
            soft = diff1 <= soft_tol and diff2 <= soft_tol and diff3 <= soft_tol
            hard = diff1 <= hard_tol and diff2 <= hard_tol and diff3 <= hard_tol
            if hard or (soft and diff2 < diff1):
                converged = True
                if i < i_converged:
                    i_converged = i
                    diffmax = max_error
            if converged:
                break
        conv = "converged (5%)" if converged else "not converged yet (5%)"
        sc_cc = '{:.1E}'.format(cc)
        w = transportfile[i_converged] if converged else grid
        if converged:
            print("Transport (avg) " + conv + " after " + w + " for a carrier concentration of " + sc_cc)
            print("Mobility results: mob_avg = " + str(np.round(mob[i_converged],4)) + " mob_x = " + str(np.round(mob_x[i_converged],4))+ " mob_y = " + str(np.round(mob_y[i_converged],4)) + " mob_z = " + str(np.round(mob_z[i_converged],4)))
        else:
            print("No results to show for " + sc_cc + ": Transport (avg) " + conv + " after " + w)
    else:
        print("not converged yet because there are not enough points to decide")
