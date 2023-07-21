import dearpygui.dearpygui as dpg

def main():
    
    dpg.create_context()
    dpg.create_viewport(title='Brainy Computer Interface', width=500, height=500)

    with dpg.window(label="main", tag="Primary Window", no_title_bar=True, no_collapse=True, no_move=True):
        
        dpg.add_text("Settings:")
        
        dpg.add_input_text(label="Input String", default_value="Quick brown fox")
        dpg.add_slider_float(label="Volume", default_value=50, max_value=100)
        
        dpg.add_button(label="Run!")



    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
    
    
    
    """ Debug """
    
    # createMP3("Test", 200, 1.0, 1)

if __name__ == "__main__":
    main()