import re

class MainApp:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.commands = []
        self.poin = 0

    def process_command(self, command):
        if command == "edu exit edu":
            return True
        elif command == "edu current menu edu":
            print("log in/sign up menu")
        elif command.startswith("edu sign up -"):
            self.process_sign_up(command)
        elif command.startsw
