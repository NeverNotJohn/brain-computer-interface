#####################
#   VIRTUAL BOARD   #
#####################

# Inserting paths
import sys
sys.path.append('..')

# Import Modules
from brainy.brainy import *

def main():
    
    file_name = "BrainFlow-RAW_2023-04-26_00-18-28_0"
    
    recorder = brainy("virtual", 0, f"../data/{file_name}.csv")
    
    recorder.get_sample()
    recorder.stop()
        
if __name__ == "__main__":
    main()


