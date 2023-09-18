import sys
sys.path.append('..')

from brainy import *
import dearpygui.dearpygui as dpg

""" STATIC """
boardList = ["cyton", "virtual", "ganglion"]

""" VARIABLES """
board = ""
COM_Num = 0
file = ""
program = ""


def getBoard(Sender):
    global board
    
    board = dpg.get_value(Sender)
    print(type(board))
    print(board)
    
def getCOM(Sender):
    global COM_Num
    
    COM_Num = dpg.get_value(Sender)
    print(COM_Num)
    print(type(COM_Num))
    
def getFile(Sender):
    global file
    
    file = dpg.get_value(Sender)
    print(file)
    print(type(file))
    
def run(Sender):
    global board
    global COM_Num
    global file
    global program
    
    