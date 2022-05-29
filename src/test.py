# First Party
from gui import window

with window(title="pyPost", width=640, height=400) as dpg:
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Request")
        dpg.add_input_text(label="URL", default_value="https://pokeapi.co/api/v2/pokemon/2")
        dpg.add_button(label="Make Request")
