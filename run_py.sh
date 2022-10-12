#!/bin/bash
#SBATCH --job-name=Omarcito69    # Job name
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --output=Omerson.log   # Standard output and error log
pwd; hostname; date

export PYTHONPATH=mnt/nfshare/lib 
python perfomance.py
