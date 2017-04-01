import re


class Replacer:
    def __init__(self, input_string: str, formattings: list) -> None:
        self.input_string: str = input_string
        self.formattings: list = formattings
        self.output_string: str = ''
        self.queues = {}
        self.delays = {}

    def replace_all(self) -> str:
        # create an list of queues which will hold the tags which have to be closed after each index

        # for each index, check if there are any closing tags in the queue, if so, apply them
        # keep going till the end of the world(or the string, at least)

        # iterate over each character in the input
        for current_position in range(0, len(self.input_string)):
            # close all tags
            if current_position in self.queues:

                if len(self.queues[current_position]) > 1:
                    pass

                for tag in self.queues[current_position]:
                    self.output_string += tag.closing

            # get match for all regexes(in the order in the given rules)
            for formatting_tuple in self.formattings:
                if not self.is_delayed(formatting_tuple):
                    # print(formatting_tuple[0].python_regex)
                    match = re.match(formatting_tuple[0].python_regex, self.input_string[current_position:], flags=re.DOTALL)
                    if match:
                        match_size = match.regs[0][1]
                        # print(match, match_size, match.re)

                        # remove empty string matches
                        if match_size != 0:
                            self.set_delay(formatting_tuple, match_size)
                            # add tags
                            for tag in formatting_tuple[1]:
                                self.output_string += tag.opening

                                if current_position + match_size in self.queues:
                                    # print('COLLISION ON QUEUES!', current_position, tag)

                                    self.queues[current_position + match_size].insert(0, tag)  # add tags to close
                                    # self.queues[current_position + match_size].append(tag)  # add tags to close
                                else:
                                    self.queues[current_position + match_size] = [tag]

            self.decrement_delays()
            self.output_string += self.input_string[current_position:current_position + 1]

        # close all remaining tags
        if len(self.input_string) in self.queues:
            self.queues[len(self.input_string)].reverse()
            for tag in self.queues[len(self.input_string)]:
                # print("CLOSING TAG:", tag.closing)
                self.output_string += tag.closing

        # print(self.output_string)
        return self.output_string

    def decrement_delays(self):
        for value in self.delays:
            self.delays[value] -= 1

    def is_delayed(self, formatting_tuple: tuple):
        if formatting_tuple[2] in self.delays and self.delays[formatting_tuple[2]] > 0:  # maybe 1 ?
            return True

    def set_delay(self, formatting_tuple: tuple, delay: int):
        self.delays[formatting_tuple[2]] = delay
