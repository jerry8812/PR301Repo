from TIGr import AbstractParser
import re


class Parser(AbstractParser):
    """Parse commands from source or input to drawer.

    Inherits:
    drawer, source, command, data, parse(raw_source)
    """

    def __init__(self, drawer):
        super().__init__(drawer)
        self.direction_table = {'n|north': 90,
                                'e|east': 0,
                                'w|west': 180,
                                's|south': 270}
        self.commands = {'p|pen': self.draw_select_pen,
                         'u|up': self.draw_pen_up,
                         'd|down': self.draw_pen_down,
                         'n|north': self.draw_line_data,
                         'e|east': self.draw_line_data,
                         's|south': self.draw_line_data,
                         'w|west': self.draw_line_data,
                         'x': self.draw_goto_x,
                         'y': self.draw_goto_x}

    def draw_clear(self, data=None):
        self.drawer.clear()

    def draw_select_pen(self, data):
        self.drawer.select_pen(data)

    def draw_pen_down(self, data=None):
        self.drawer.pen_down()

    def draw_pen_up(self, data=None):
        self.drawer.pen_up()

    def draw_line_data(self, data):
        # Parse drawer specific command through alias and command tables
        # Multi-line case insensitive regex
        for alias in self.commands:
            if re.search(r'^.*(' + alias + r')$', self.command, re.M | re.I):
                self.drawer.draw_line(self.direction_table[alias], self.data)
                break

    def draw_goto_x(self, data):
        self.drawer.go_along(data)

    def draw_goto_y(self, data):
        self.drawer.go_down(data)

    def parse(self, raw_source):
        self.source = raw_source

        # Loop through each line in source and separate the command form the arguments
        # Lookup command through alias and command tables and execute
        # Multi-line case insensitive regex
        for source_line in self.source:
            self.command = source_line.split(' ', 1)[0].lower()

            if ' ' in source_line:
                self.data = float(source_line.split(' ')[1])

            for alias in self.commands:
                if re.search(r'^.*(' + alias + r')$', self.command, re.M | re.I):
                    self.commands[alias](self.data)
                    break
