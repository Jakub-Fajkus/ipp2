from app.arguments.Config import Config
from app.Replacer import Replacer
from app.io.Input import Input
from app.io.Output import Output

class App:
    def __init__(self, config: Config):
        self._config = config

    def run(self):
        self._config.validate()

        if 'help' in self._config.values:
            self.print_help()
            return

        input = Input(config=self._config)
        output = Output(config=self._config)
        input_string = input.get_input()

        formating = input.get_format_table()
        if not formating:
            output.present_output(input_string)

            return

        replacer = Replacer(input_string)
        output_string = replacer.replace_all()

        output.present_output(output_string)

    @staticmethod
    def print_help():
        # todo: print help!
        print("Printing some help...\nHELP!!!!\nHELP MEEEE!\nI am drowning in a pool!\n...")
