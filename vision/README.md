

# To get this code running install Anaconda from
# https://www.continuum.io/downloads
# Choose the Python3.6 version

# Next cd into this directory and run
conda env create -f vision.yml
# This command will set up and install all necessary environment items

# Next type:
source activate vision
#This will activate the current python environment

#Finally type
python MainGui.py
#This should initiate the measurement tool
