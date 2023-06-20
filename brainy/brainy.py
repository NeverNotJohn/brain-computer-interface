########################
# Brain Recorder Class #
########################

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets

class brainy:
    
    def __init__(self, board, COM_Num):
        
        """ Logic: """
        
        params = BrainFlowInputParams()                                             # Params I guess 
        params.serial_port = f"COM{COM_Num}"                                        # Only Param needed                
        
        if (board == "cyton"):
            board_input = BoardShim(BoardIds.CYTON_DAISY_BOARD, params)
        elif (board == "virtual"):
            board_input = BoardShim(BoardIds.PLAYBACK_FILE_BOARD, params)
        elif (board == "ganglion"):
            board_input = BoardShim(BoardIds.GANGLION_BOARD, params)
        
        """ Variables: """ 
        
        self.board = board_input
        self.COM = f"COM{COM_Num}"
        
        """ Functions """
        
        
        
        # Functions: