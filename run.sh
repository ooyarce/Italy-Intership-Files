#!/bin/bash
#SBATCH --job-name=Omarcito69    # Job name
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --output=Omarson.log   # Standard output and error log
pwd; hostname; date

export OMP_NUM_THREADS=1
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/nfshare/lib
mpirun /mnt/nfshare/bin/openseesmp main.tcl
date
