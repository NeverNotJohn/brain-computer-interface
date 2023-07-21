from brainy import *
import dearpygui.dearpygui as dpg

""" STATIC """
boardList = ["cyton", "virtual", "ganglion"]

""" VARIABLES """
board = "virtual"
COM_Num = 0
file = ""


def getBoard(Sender):
    global board
    
    board = dpg.get_value(Sender)
    print(board)