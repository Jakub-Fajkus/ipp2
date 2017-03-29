from app.arguments.Config import Config


class App:
    def __init__(self, config: Config):
        self._config = config

    def run(self):
        self._config.validate()

        if 'help' in self._config.values:
            self.print_help()
            return

    @staticmethod
    def print_help():
        # todo: print help!
        print("Printing some help...\nHELP!!!!\nHELP MEEEE!\nI am drowning in a pool!\n...")
