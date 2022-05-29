# Standard Library
import contextlib

# Third Party
import dearpygui.dearpygui as dpg


@contextlib.contextmanager
def window(**kwargs):
    dpg.create_context()

    try:
        yield dpg
    finally:
        dpg.create_viewport(**kwargs)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
