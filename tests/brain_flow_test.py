import argparse
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets

def update(self):
    data = self.get_current_board_data(1)
    
    channel_16 = data[16]
    
    print(channel_16)
    
    

def main():
    BoardShim.enable_dev_board_logger()

    # Params 

    params = BrainFlowInputParams()

    params.serial_port = "COM5"
    board = BoardShim(BoardIds.CYTON_DAISY_BOARD, params)
    
    board.prepare_session()
    board.start_stream()
    
    
    
    while True:
        update(board)
    
    """
    time.sleep(10)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    board.stop_stream()
    board.release_session()

    print(data)
    """


if __name__ == "__main__":
    main()