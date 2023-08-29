########################
# Brain Recorder Class #
########################

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainy.func import update
import numpy as np
from matplotlib import pyplot as plt
import time


class brainy:
    
    def __init__(self, board, COM_Num, file=""):
        
        print("Initialized!") # DEBUG
        
        """ Logic: """
        
        params = BrainFlowInputParams()                                             # Params I guess       
        
        if (board == "cyton"):
            params.serial_port = f"COM{COM_Num}"                                    # Only Param needed          
            board_input = BoardShim(BoardIds.CYTON_DAISY_BOARD, params)
        elif (board == "virtual"):  
            params.master_board = BoardIds.CYTON_DAISY_BOARD                        # ASSUMES PLAYING BACK CYTON FILE
            params.file = file                                                      # Path to recording file
            board_input = BoardShim(BoardIds.PLAYBACK_FILE_BOARD, params)
        elif (board == "ganglion"):
            params.serial_port = f"COM{COM_Num}"                                    # Only Param needed          
            board_input = BoardShim(BoardIds.GANGLION_BOARD, params)
        
        """ Variables: """ 
        
        self.board = board_input
        self.COM = f"COM{COM_Num}"
        self.data = []
        
        """ Start """
        
        self.board.prepare_session()
        self.board.start_stream()
        time.sleep(3)   # let buffer

    """ Functions: """

    def update(self):   # FIXME
        update.refresh(self.board)
        
    # Gets 1 second sample from board
    # Apply filters here?
    
    def get_sample(self):
        time.sleep(1)
        raw_data = self.board.get_current_board_data(125)
        print(raw_data[1])
    
        
        # debug
        plt.title("test")
        plt.xlabel("time (ms)") 
        plt.ylabel("Voltage (uV)") 
        plt.plot(raw_data[1], label="Channel 1") 
        plt.show()
        
        
    def stop(self):
        self.board.stop_stream()
        self.board.release_session()
        