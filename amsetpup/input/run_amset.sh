#!/bin/bash
#SBATCH --ntasks=32
#SBATCH --time=0:30:0
#SBATCH --account=scanlodo-wide-gap-oxides
#SBATCH --qos=bbdefault
##SBATCH --mail-type=ALL
#SBATCH --mem-per-cpu=4096
#SBATCH --nodes=1
#SBATCH --output=queue.qout
#SBATCH --error=queue.qerr

ulimit -s unlimited
ulimit -m unlimited

export OMP_NUM_THREADS=1

module purge
module load bluebear

source ~/.bashrc
conda activate amset

for var in 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85; do
    amset run -s settings.yaml -i $var | tee amset-${var}.log
done

