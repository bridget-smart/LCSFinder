#!/bin/bash
#SBATCH -p batch # Partition (this is the queue your job will be added to)
#SBATCH -N 1 # Number of nodes
#SBATCH -n 1 # Number of CPU cores
#SBATCH --time=0-01:00:00 # Approx. time to run (1 day in this case)
#SBATCH --mem=20GB # Total memory required (this is a big one)
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-user=$USER@adelaide.edu.au
# This stuff is going to activate your python environment
# module load arch/skylake
# module load Python/3.8.6 
# source /hpcfs/users/a1742577/local/virtualenvs/hack/bin/activate


# #libraries
pip install -U datetime pandas numpy warnings numba seaborn matplotlib tqdm

# here is where we are compiling the swig module

swig -c++ -python LCSFinder.i 
python setup.py build_ext --inplace

# # Then we run the code. You can also use arguments here.
python testing_p.py

# deactivate # Closes the python environment.