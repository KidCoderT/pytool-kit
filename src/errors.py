from tkinter import messagebox


def asci_warn():
    """shows a large asci warning"""
    print(
        r"""\033[93m
                          (_)            
 __      ____ _ _ __ _ __  _ _ __   __ _ 
 \ \ /\ / / _` | '__| '_ \| | '_ \ / _` |
  \ V  V / (_| | |  | | | | | | | | (_| |
   \_/\_/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                    __/ |
                                   |___/
        \x1b[0m"""
    )


def asci_error():
    """shows a large asci erro"""
    print(
        r"""\033[91m
   ___ _ __ _ __ ___  _ __
  / _ \ '__| '__/ _ \| '__|
 |  __/ |  | | | (_) | |
  \___|_|  |_|  \___/|_|
        \x1b[0m"""
    )


def give_info(title: str, description: str):
    """A method that can display error
    to a user through a gui

    Args:
        title (str): the title of the error
        description (str): the description of the error
    """
    messagebox.showinfo(title, description)


def give_warning(title: str, description: str):
    """A method that can display error
    to a user through a gui

    Args:
        title (str): the title of the error
        description (str): the description of the error
    """
    messagebox.showwarning(title, description)


def give_error(title: str, description: str):
    """A method that can display error
    to a user through a gui

    Args:
        title (str): the title of the error
        description (str): the description of the error
    """
    messagebox.showerror(title, description)
