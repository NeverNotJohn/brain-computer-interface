def refresh(self):
    data = self.get_current_board_data(1)
    
    channel_16 = data[16]
    
    print(channel_16)