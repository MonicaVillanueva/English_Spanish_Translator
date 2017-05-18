#!/bin/bash
# The name of the script is myjob
#SBATCH -J myjob2
# Only 1 hour wall-clock time will be given to this job
#SBATCH -t 8:00:00
# set the project to be charged for this
# The format should be edu<year>.DT2119
#SBATCH -A edu17.DT2119
# Use K80 GPUs (if not set, you might get nodes with Quadro K420 GPUs)
# SBATCH --gres=gpu:K80:2
# Standard error and standard output to files
#SBATCH -e error_file.txt
#SBATCH -o output_file.txt
# Run the executable (add possible additional dependencies here)
python translate.py  --data_dir ../data --train_dir ../temp  --size=512 --num_layers=4 --steps_per_checkpoint=1000

							