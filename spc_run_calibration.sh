#!/bin/sh
#SBATCH --partition=t1standard
#SBATCH --ntasks=576
#SBATCH --tasks-per-node=24

# activate environment
module load lang/Anaconda3/2.5.0
source activate pygem_hpc

REGNO="15"
ADD_CAL_SWITCH=1

# split glaciers into batches for different nodes
python spc_split_glaciers.py -n_batches=$SLURM_JOB_NUM_NODES -add_cal=$ADD_CAL_SWITCH

# list rgi_glac_number batch filenames
CHECK_STR="Cal_R${REGNO}_rgi_glac_number_batch"
rgi_fns=$(find $CHECK_STR*)
echo rgi_glac_number filenames:$rgi_fns
# create list
list_rgi_fns=($rgi_fns)
echo first_batch:${list_rgi_fns[0]}

echo partition: $SLURM_JOB_PARTITION
echo num_nodes: $SLURM_JOB_NUM_NODES nodes: $SLURM_JOB_NODELIST
echo num_tasks: $SLURM_NTASKS tasks_node: $SLURM_NTASKS_PER_NODE

for i in $rgi_fns
do
  # print the filename
  echo $i
  # run the file on a separate node (& tells the command to move to the next loop for any empty nodes)
  srun -N 1 -n 1 python run_calibration.py -num_simultaneous_processes=$SLURM_NTASKS_PER_NODE -rgi_glac_number_fn=$i &
done
# wait tells the loop to not move on until all the srun commands are completed
wait
