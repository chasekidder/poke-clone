# Main Application File - main.py
# 
# 
# 

import modules.game.game

class Application():
    def __init__(self):
        self.game = None
        self.settings = None

    def load_settings(self):
        self.settings = {
            "name":"PokeClone",
            "window_size":(480,480),
            "visible":False
        }

    def start(self):
        self.game = game.Game(self.settings("name"), self.settings("window_size"), self.settings("visible"))

    def run(self):
        self.game.visible = True
        self.game.run()

    def debug(self, parameter_list):
        pass

    def exit(self, parameter_list):
        pass

    def error(self, parameter_list):
        pass

if __name__ == "__main__":
    app = Application()
    app.start()
    app.run()
    app.exit()