"""TIGrEx
Extended Tiny Interpreted Graphics

By Sean Ryan

Features:
Interactive frontend
    - Increases functionality by providing another way of interaction with the program
    - Tested by doctests
Supports piping and scripting
    - Increases flexibility by allowing images to be drawn through automatic scripts
    - Clever by using regex and aliases to allow for flexible syntax
    - Tested by doctests
Parsed from configurable lookup tables
    - Increases flexibility by allowing for commands to be added easily and dynamically
    - Clever by using regex for aliases for more flexibility
    - Tested by unit tests and doctests
Uses regular expressions in parser
    - Increases flexibility by allowing for aliases to be used in scripts
    - Tested by unit tests and doctests
Uses generic parsing engine
    - Increases functionality by providing an interface that can be used by any drawer
    - Tested by unit tests and doctests
Outputs with turtle.py
    - Increases functionality by using an alternative form of drawing to the screen
    - Tested by unit tests and doctests
Provide doctests
    - Improves robustness by testing features and functions for if they are valid and working
Provide unit tests
    - Improves robustness by testing features and functions for if they are valid and working
    - Clever by dynamically loading tests from a Test Case class in to a test suite
Breadth of test coverage
    - Improves robustness by ensuring every feature works as expected
    - Every function has been covered
    - Tests done through both unit tests and doctests
Amount of error trapping & handling
    - Improves robustness by keeping the program running even when errors are found
    - Most functions have error handling to alert the user of issues with input
    - Also used for ensuring data gets handled correctly
"""
from TIGrExSourceReader import SourceReader
from TIGrExParser import Parser
from TIGrExTextDrawer import TextDrawer
from TIGrExTurtleDrawer import TurtleDrawer
import cmd
import re


class TIGrEx(cmd.Cmd):
    """Main application controller for TIGrEx


    Begin doctest - Written with Jonathan Holdaway and Sean Ryan 24/08/2019

    >>> app.do_drawer('turtle')
    Now using Turtle Drawer
    >>> app.do_pen(2)
    Selected pen 2
    >>> app.do_x(5)
    Gone to X=5
    >>> app.do_y(5)
    Gone to Y=5
    >>> app.do_down()
    Pen down
    >>> app.do_east(50)
    drawing line of length 50 at 0 degrees
    >>> app.do_north(50)
    drawing line of length 50 at 90 degrees
    >>> app.do_west(50)
    drawing line of length 50 at 180 degrees
    >>> app.do_south(50)
    drawing line of length 50 at 270 degrees
    >>> app.do_up()
    Pen lifted

    Test script running
    >>> app.do_clear()
    Cleared drawing
    >>> app.do_run('script')
    Running script: script.tigr
    Selected pen 2.0
    Gone to X=5.0
    Gone to Y=15.0
    Pen down
    drawing line of length 2.0 at 180 degrees
    drawing line of length 1.0 at 90 degrees
    drawing line of length 2.0 at 0 degrees
    drawing line of length 12.7 at 270 degrees
    Pen lifted

    End doctest
    # """
    intro = 'Welcome to Extended Tiny Interpreted Graphics.\n' \
            'Use "drawer" command to choose graphics library.\n' \
            'Enter ? for help.'
    prompt = 'TIGrEx >: '

    def __init__(self):
        super().__init__()
        self.drawer = None
        self.parser = None
        self.source_reader = None

    def setup(self, drawer):
        # Generic setup for classes
        self.drawer = drawer
        self.parser = Parser(self.drawer)
        self.source_reader = SourceReader(self.parser)

    def do_drawer(self, arg):
        """Select graphics library to draw with.
Available drawers:
text, turtle
-----"""
        if self.drawer:
            self.drawer.shutdown()
        if arg.lower() == 'text':
            self.setup(TextDrawer())
        elif arg.lower() == 'turtle':
            self.setup(TurtleDrawer())
        else:
            print('Please select a valid drawer.')

    def do_clear(self, arg=None):
        del arg
        if self.drawer_check():
            self.parser.draw_clear()

    def do_up(self, arg=None):
        """Stop drawing.
-----"""
        del arg
        if self.drawer_check():
            self.parser.draw_pen_up()

    def do_down(self, arg=None):
        """Start drawing.
-----"""
        del arg
        if self.drawer_check():
            self.parser.draw_pen_down()

    def do_north(self, arg):
        """Draw north by a specified amount.
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.command = 'north'
            self.parser.draw_line_data(self.parser.data)

    def do_south(self, arg):
        """Draw south by a specified amount.
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.command = 'south'
            self.parser.draw_line_data(self.parser.data)

    def do_east(self, arg):
        """Draw east by a specified amount.
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.command = 'east'
            self.parser.draw_line_data(self.parser.data)

    def do_west(self, arg):
        """Draw west by a specified amount.
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.command = 'west'
            self.parser.draw_line_data(self.parser.data)

    def do_x(self, arg):
        """Set X position of the pen.
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.draw_goto_x(self.parser.data)

    def do_y(self, arg):
        """Set Y position of the pen.
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.draw_goto_y(self.parser.data)

    def do_pen(self, arg):
        """Select preset pen.
Preset pens:
1 - colour black, size 10
2 - colour red, size 10
3 - colour blue, size 10
-----"""
        if self.drawer_check() and self.data_check(arg):
            self.parser.data = int(arg)
            self.parser.draw_select_pen(self.parser.data)

    def do_run(self, arg):
        """Load a script and run it.
-----"""
        if self.drawer_check():
            # Search for file without extension, if the file isn't found try with extension
            # Using multi-line and case insensitive for regex search
            # modified by Jerry Wang, this regx can not match a file name end with .tigr
            extension_check = re.search(r'^.*(' + self.source_reader.script_extension + r')$', arg, re.M | re.I)
            if extension_check:
                file = arg
            else:
                file = arg + self.source_reader.script_extension
            print('Running script:', file)
            try:
                self.source_reader.source = [line.rstrip('\n') for line in open(file)]
            except FileNotFoundError:
                # If file is found in search without the script extension alert that TIGr only reads .tigr scripts
                if not re.search(r'^.*\.(' + self.source_reader.script_extension + r')$', arg, re.M | re.I):
                    print('Script not found. Enter a valid file name.')
                else:
                    print(f'Script not found.TIGrEx only reads {self.source_reader.script_extension} files as scripts.')
            else:
                # Start parsing the script
                self.source_reader.file_name = arg
                self.source_reader.go()

    # extract error check into two new methods  ---- Duplicated Code
    def drawer_check(self):
        if self.drawer is None:
            try:
                raise AttributeError
            except AttributeError:
                print("Please select a drawer before trying to run drawer commands.")
        else:
            return True

    @staticmethod
    def data_check(arg):
        if arg == '' or re.search(r'[^0-9]', str(arg), re.M | re.I):
            try:
                raise ValueError
            except ValueError:
                print('This command only takes numbers')
        else:
            return True

    @staticmethod
    def do_quit(arg):
        """Closes the program.
-----"""
        del arg
        exit()

    @staticmethod
    def do_exit(arg):
        """Closes the program.
-----"""
        del arg
        exit()

    @staticmethod
    def parse(arg):
        # Convert arg to a tuple
        return tuple(map(int, arg.split()))


if __name__ == '__main__':
    app = TIGrEx()
    # Run specified tests
    # noinspection PyUnreachableCode
    if True:
        import doctest

        doctest.testmod(verbose=3)
    app.cmdloop()
