class Replacer:
    def __init__(self, input_string: str) -> None:
        self.input_string: str = input_string
        self.output_string: str = ''
        self.queues = []

    def replace_all(self) -> str:
        pass
        # create an list of queues which will hold the tags which have to be closed after each index
        # iterate over each character in the input
        # get match for all regexes(in the order in the given rules)
        # for each index, check if there are any closing tags in the queue, if so, apply them
        # keep going till the end of the world(or the string, at least)

        for char in self.input_string:
            pass
            # print(letter)

        return self.output_string
