########################
# Brain Recorder Class #
########################

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from func import update


class brainy:
    
    def __init__(self, board, COM_Num, file=""):
        
        """ Logic: """
        
        params = BrainFlowInputParams()                                             # Params I guess       
        
        if (board == "cyton"):
            params.serial_port = f"COM{COM_Num}"                                    # Only Param needed          
            board_input = BoardShim(BoardIds.CYTON_DAISY_BOARD, params)
        elif (board == "virtual"):
            params.master_board = BoardIds.SYNTHETIC_BOARD
            params.file = file                                                      # Path to recording file
            board_input = BoardShim(BoardIds.PLAYBACK_FILE_BOARD, params)
        elif (board == "ganglion"):
            params.serial_port = f"COM{COM_Num}"                                    # Only Param needed          
            board_input = BoardShim(BoardIds.GANGLION_BOARD, params)
        
        """ Variables: """ 
        
        self.board = board_input
        self.COM = f"COM{COM_Num}"
        
        """ Start """
        
        board.prepare_session()
        board.start_stream()

    """ Functions: """

    def update(self):   # FIXME
        update.refresh(self.board)
        