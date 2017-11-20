from rational_gui.controller import CONTROLLER
def wait_for_thread(thread, callback):
    if thread.is_alive():
        CONTROLLER.after_idle(lambda: wait_for_thread(thread, callback))
    else:
        callback()