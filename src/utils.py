class AdminPrivilegesNotReceived(Exception):
    def __init__(self):
        super().__init__("Admin Privileges not received")
