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
        elif command.startswith("edu log in -"):
            self.process_log_in(command)
        else:
            print("invalid command")
        return False

    def process_sign_up(self, command):
        pattern = re.compile(r'^edu sign up -(.+?) -i (.+?) -n (.+?) -p (.+?) edu$')
        match = pattern.match(command)
        if match:
            user_type, user_id, name, password = match.groups()
            self.sign_up(user_type, user_id, name, password)
        else:
            print("invalid command")

    def process_log_in(self, command):
        pattern = re.compile(r'^edu log in -i (.+?) -p (.+?) edu$')
        match = pattern.match(command)
        if match:
            user_id, password = match.groups()
            self.log_in(user_id, password)
        else:
            print("invalid command")

    def sign_up(self, user_type, user_id, name, password):
        # Validation and sign-up logic here
        pass

    def log_in(self, user_id, password):
        # Validation and log-in logic here
        pass

    def main(self):
        while True:
            try:
                line = input().strip()
                if self.process_command(line):
                    break
                self.commands.append(line)
            except EOFError:
                break

        while self.poin < len(self.commands):
            if self.process_command(self.commands[self.poin]):
                break
            self.poin += 1


if __name__ == "__main__":
    app = MainApp()
    app.main()

