from ase import io
import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()

onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]

for file in onlyfiles:
    # Get the current format
    s = file.split(".")
    br = s[-1]

    if br == 'cif':
        atoms = io.read(file)
        atoms.write('POSCAR', format = 'vasp')
