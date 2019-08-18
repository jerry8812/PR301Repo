from TIGr import AbstractParser


class Parser(AbstractParser):
    """Parse commands from source or input to drawer.

    Inherits:
    drawer, source, command, data, parse(raw_source)
    """

    def __init__(self, drawer):
        super().__init__(drawer)
        self.direction_table = {'north': 90,
                                'east': 0,
                                'west': 180,
                                'south': 270}
        self.commands = {'pen': self.draw_select_pen,
                         'up': self.draw_pen_up,
                         'down': self.draw_pen_down,
                         'north': self.draw_line_data,
                         'east': self.draw_line_data,
                         'south': self.draw_line_data,
                         'west': self.draw_line_data,
                         'x': self.draw_goto_x,
                         'y': self.draw_goto_x}
        self.command_aliases = {'p': 'pen',
                                'pen': 'pen',
                                'u': 'up',
                                'up': 'up',
                                'd': 'down',
                                'down': 'down',
                                'n': 'north',
                                'north': 'north',
                                'e': 'east',
                                'east': 'east',
                                's': 'south',
                                'south': 'south',
                                'w': 'west',
                                'west': 'west',
                                'x': 'x',
                                'y': 'y'}

    def draw_clear(self, data=None):
        self.drawer.clear()

    def draw_select_pen(self, data):
        self.drawer.select_pen(data)

    def draw_pen_down(self, data=None):
        self.drawer.pen_down()

    def draw_pen_up(self, data=None):
        self.drawer.pen_up()

    def draw_line_data(self, data):
        self.drawer.draw_line(self.direction_table[self.command_aliases[self.command]], self.data)

    def draw_goto_x(self, data):
        self.drawer.go_along(data)

    def draw_goto_y(self, data):
        self.drawer.go_down(data)

    def parse(self, raw_source):
        self.source = raw_source

        for source_index, source_line in enumerate(self.source):
            self.command = source_line.split(' ', 1)[0].lower()

            if ' ' in source_line:
                self.data = float(source_line.partition(' ')[2])
            self.commands[self.command_aliases[self.command]](self.data)
