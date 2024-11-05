#!/bin/bash
#SBATCH --ntasks=48
##SBATCH --ntasks-per-node=
#SBATCH --time=24:0:0
#SBATCH --account=scanlodo-wide-gap-oxides
#SBATCH --qos=bbdefault
##SBATCH --mail-type=ALL
#SBATCH --mem-per-cpu=4096
#SBATCH --nodes=1
#SBATCH --job-name=relax

set -e

module purge
module load bluebear
module load bear-apps/2022a
module load VASP/6.4.2-intel-2022a

ulimit -s unlimited

mpirun vasp_std