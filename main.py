from programs import gui
import dearpygui.dearpygui as dpg


""" INITIALIZE GUI """
dpg.create_context()
dpg.create_viewport(title='Brainy Computer Interface', width=500, height=500)



""" MAIN """

with dpg.window(label="main", tag="Primary Window", no_title_bar=True, no_collapse=True, no_move=True):
    
    dpg.add_text("Settings:")
    
    """ Settings """
    
    # Selecting Board
    dpg.add_listbox(label="Select Board", items=gui.boardList, width=80, callback=gui.getBoard)
    dpg.add_listbox(label="Select COM Num", items=[0,1,2,3,4,5], width=80, callback=gui.getBoard)
    dpg.add_listbox(label="Select File", items=gui.boardList, width=80, callback=gui.getFile)
    dpg.add_input_text(label="Input File path", width=200, callback=gui.getFile)
    
        
    



""" RUN GUI """

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()



""" Debug """

# createMP3("Test", 200, 1.0, 1)

