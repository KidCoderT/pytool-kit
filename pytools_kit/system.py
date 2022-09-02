import os
import sys
import platform
import ctypes
from .utils import AdminPrivilegesNotReceived

system_information = platform.uname()
ASADMIN = "asadmin"


class System:
    """Set of system commands that can be used
    # waits for developer to call variables, then provides the details to the developer
    # When called the variables run a functions by using the platform library, which then fetches the values and stores them in the variable.

    """

    OS = system_information.system
    COMPUTER_NAME = system_information.node
    OS_VERSION = system_information.release
    OS_BUILD = system_information.version
    CPU_ARCHITECTURE = system_information.machine
    PROCESSOR = system_information.processor

    def get_admin_privileges(self):
        """Get Admin Privileges"""
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )

    @staticmethod
    def has_admin_privileges() -> bool:
        """Returns whether or not the program is running with admin privileges"""
        return sys.argv[-1] == ASADMIN


def install_package(library_name: str):
    """Installs a python package from code

    Args:
        library_name (str): the library to install

    Raises:
        AdminPrivilegesNotReceived: when the previliges
            are not granted
    """
    if System.has_admin_privileges():
        os.system(f"pip install {library_name}")

    raise AdminPrivilegesNotReceived()


def create_file(filepath, encoding="utf-8"):
    """Creates a file with the given name

    Args:
        filepath (str): the path to the file including name
        encoding (str, optional): the encoding to open the file as.
            Defaults to "utf-8".

    Returns:
        _type_: _description_
    """
    try:
        with open(f"{filepath}", "x", encoding=encoding) as f:
            return True
    except FileExistsError:
        return False


def move_file(current_file_path: str, new_file_path: str):
    """Moves a file from one location to another

    Args:
        current_file_path (str): the current location of the file
        new_file_path (str): the new location of the file
    """
    os.rename(current_file_path, new_file_path)


def remove_file(file: str):
    """Removes a file from the system

    Args:
        filename (str): the file to remove
    """
    os.remove(file)


def exec_file(file: str):
    """Executes a file

    Args:
        file (str): the file to execute
    """
    os.startfile(file)


def exec_shell(command: str):
    """Execute commands on the python shell

    Args:
        cmd (str): the command to execute
    """
    os.system(command)


def exec_cmd(command: str):
    """Execute commands on the command line

    Args:
        cmd (str): the command to execute
    """
    os.system("cmd /k " + command)
