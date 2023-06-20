#####################
#   VIRTUAL BOARD   #
#####################

# Inserting paths
import sys
sys.path.append('..')

# Import Modules
from brainy.brainy import *

def main():
    
    recorder = brainy("virtual", 0, "data/OpenBCI-RAW-2023-04-26_00-24-00.txt")
    
    while True:
        recorder.update()
        
if __name__ == "__main__":
    main()


