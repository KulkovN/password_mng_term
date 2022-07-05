from sys import displayhook
from pathlib import Path
import dearpygui.dearpygui as dpg
import webbrowser

URL = 'https://github.com/KulkovN/password_mng_term/blob/main/README.md'


def print_me(sender):
    print(f"Menu Item: {sender}")


dpg.create_context()
dpg.create_viewport(title='Py Pass Simple', width=500, height=300, resizable=False, 
    small_icon=f'{Path.cwd()}/gui/padlock.png', decorated=True, x_pos=480, y_pos=280)

with dpg.viewport_menu_bar():
    with dpg.menu(label="Mode"):
        dpg.add_menu_item(label="Create", callback=print_me)
        dpg.add_menu_item(label="Read", callback=print_me)
        dpg.add_menu_item(label="Update", callback=print_me)
        dpg.add_menu_item(label="Delete", callback=print_me)

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
            dpg.add_menu_item(label="Setting 2", callback=print_me)

    dpg.add_menu_item(label="Help", callback=lambda: webbrowser.open(URL, new=0))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()