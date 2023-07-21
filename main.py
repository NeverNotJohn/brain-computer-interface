import dearpygui.dearpygui as dpg
from brainy import gui

def main():
    
    """ INITIALIZE GUI """
    
    dpg.create_context()
    dpg.create_viewport(title='Brainy Computer Interface', width=500, height=500)

    with dpg.window(label="main", tag="Primary Window", no_title_bar=True, no_collapse=True, no_move=True):
        
        dpg.add_text("Settings:")
        
        """ Settings """
        
            # Create the dropdown
        with dpg.combo(label="Select Board", width=200, callback=dropdown_callback):

            #Drop down options
            
            dpg.add_selectable(label="Option 1", callback=dropdown_callback)
            dpg.add_selectable(label="Option 2", callback=dropdown_callback)
            dpg.add_selectable(label="Option 3", callback=dropdown_callback)

        
        



    """ RUN GUI """

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
    
    
    
    """ Debug """
    
    # createMP3("Test", 200, 1.0, 1)

if __name__ == "__main__":
    main()