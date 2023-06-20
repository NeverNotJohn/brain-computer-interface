#####################
#   VIRTUAL BOARD   #
#####################

# Inserting paths
import sys
sys.path.append('..')

# Import Modules
from brainy.brainy import *

def main():
    
    recorder = brainy("virtual", 0, "data/BrainFlow-RAW_2023-04-26_00-18-28_0.csv")
    
    while True:
        recorder.update()
        
if __name__ == "__main__":
    main()


