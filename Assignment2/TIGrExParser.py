"""TIGrEx
Parsing Engine

By Sean Ryan
"""
from TIGr import AbstractParser
import re


class Parser(AbstractParser):
    """Parse commands from source or input to drawer.

    Inherits:
    drawer, source, command, data, parse(raw_source)


    Begin doctest - Written with Jonathan Holdaway and Sean Ryan 23/08/2019

    >>> from TIGrExTurtleDrawer import TurtleDrawer
    >>> parser = Parser(TurtleDrawer())
    Now using Turtle Drawer
    >>> source = ['p 3']
    >>> parser.parse(source)
    Selected pen 3.0
    >>> source = ['x 5']
    >>> parser.parse(source)
    Gone to X=5.0
    >>> source = ['y 5']
    >>> parser.parse(source)
    Gone to Y=5.0
    >>> source = ['d']
    >>> parser.parse(source)
    Pen down
    >>> source = ['w 5']
    >>> parser.parse(source)
    drawing line of length 5.0 at 180 degrees
    >>> source = ['n 5']
    >>> parser.parse(source)
    drawing line of length 5.0 at 90 degrees
    >>> source = ['e 5']
    >>> parser.parse(source)
    drawing line of length 5.0 at 0 degrees
    >>> source = ['s 5']
    >>> parser.parse(source)
    drawing line of length 5.0 at 270 degrees
    >>> source = ['u']
    >>> parser.parse(source)
    Pen lifted

    End doctest
    """

    def __init__(self, drawer):
        super().__init__(drawer)
        self.direction_table = {'n|north': 90,
                                'e|east': 0,
                                'w|west': 180,
                                's|south': 270}
        self.commands = {'p|pen': self.drawer.select_pen,
                         'u|up': self.drawer.pen_up,
                         'd|down': self.drawer.pen_down,
                         'n|north': self.drawer.draw_line,
                         'e|east': self.drawer.draw_line,
                         's|south': self.drawer.draw_line,
                         'w|west': self.drawer.draw_line,
                         'x': self.drawer.go_along,
                         'y': self.drawer.go_down,
                         'clear': self.drawer.clear}

    # delete the methods that perform only one action and delegating work to Drawer class. Middle man bad smell
    def parse(self, raw_source):
        for source_line in raw_source:
            self.command = source_line.split(' ', 1)[0].lower()
            # extract data error check and move it here
            if ' ' in source_line:
                try:
                    self.data = float(source_line.split(' ')[1])
                except ValueError:
                    print('This command only takes numbers')
                    return
            else:
                self.data = None
            for alias in self.commands:
                # changed regx,resolved that alias 'p|pen' can match command 'up'
                if re.match(r'(' + alias + r')', self.command, re.M | re.I):
                    if self.data is None:
                        self.commands[alias]()
                    elif alias in self.direction_table:
                        self.commands[alias](self.direction_table[alias], self.data)
                    else:
                        self.commands[alias](self.data)
                    break


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=3)
