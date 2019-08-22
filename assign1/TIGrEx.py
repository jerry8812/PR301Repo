"""TIGrEx
Extended Tiny Interpreted Graphics
"""
from TIGrExSourceReader import SourceReader
from TIGrExParser import Parser
from TIGrExTextDrawer import TextDrawer
from TIGrExTurtleDrawer import TurtleDrawer
import cmd
import re


class TIGrEx(cmd.Cmd):
    """Main application controller for TIGrEx

    Begin doctest

    >>> print('hello')
    hello
    """
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
text, turtle, TKinter
-----"""
        if self.drawer:
            self.drawer.shutdown()
        if arg.lower() == 'text':
            self.setup(TextDrawer())
        elif arg.lower() == 'turtle':
            self.setup(TurtleDrawer())
        elif arg.lower() == 'tkinter':
            self.setup(TextDrawer())
        else:
            print('Please select a valid drawer.')

    def do_clear(self, arg):
        try:
            self.parser.draw_clear()
        except AttributeError as exception:
            if self.drawer is None:
                # If no drawer is set then don't allow a command to run
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_up(self, arg):
        """Stop drawing.
-----"""
        try:
            self.parser.draw_pen_up()
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_down(self, arg):
        """Start drawing.
-----"""
        try:
            self.parser.draw_pen_down()
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_north(self, arg):
        """Draw north by a specified amount.
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.command = 'north'
            self.parser.draw_line_data(self.parser.data)
        except ValueError:
            print('This command only takes numbers')
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_south(self, arg):
        """Draw south by a specified amount.
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.command = 'south'
            self.parser.draw_line_data(self.parser.data)
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_east(self, arg):
        """Draw east by a specified amount.
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.command = 'east'
            self.parser.draw_line_data(self.parser.data)
        except ValueError:
            print('This command only takes numbers')
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_west(self, arg):
        """Draw west by a specified amount.
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.command = 'west'
            self.parser.draw_line_data(self.parser.data)
        except ValueError:
            print('This command only takes numbers')
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_x(self, arg):
        """Set X position of the pen.
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.draw_goto_x(self.parser.data)
        except ValueError:
            print('This command only takes numbers')
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_y(self, arg):
        """Set Y position of the pen.
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.draw_goto_y(self.parser.data)
        except ValueError:
            print('This command only takes numbers')
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_pen(self, arg):
        """Select preset pen.

Preset pens:
1 - colour black, size 10
2 - colour red, size 10
3 - colour blue, size 10
-----"""
        try:
            self.parser.data = int(arg)
            self.parser.draw_select_pen(self.parser.data)
        except ValueError:
            print('This command only takes numbers')
        except AttributeError as exception:
            # If no drawer is set then don't allow a command to run
            if self.drawer is None:
                print('Please select a drawer before trying to run drawer commands.')
            else:
                print(exception)

    def do_run(self, arg):
        """Load a script and run it.
-----"""
        try:
            # Search for file without extension, if the file isn't found try with extension
            # Using multi-line and case insensitive for regex search
            if re.search(r'^.*\.(' + self.source_reader.script_extension + r')$', arg, re.M | re.I):
                file = arg
            else:
                file = arg + self.source_reader.script_extension
            print('Running script:', file)
            self.source_reader.source = [line.rstrip('\n') for line in open(file)]
        except FileNotFoundError:
            # If file is found in search without the script extension alert that TIGr only reads .tigr scripts
            if not re.search(r'^.*\.(' + self.source_reader.script_extension + r')$', arg, re.M | re.I):
                print('Script not found. Enter a valid file name.')
            else:
                print(f'Script not found. TIGrEx only reads {self.source_reader.script_extension} files as scripts.')
        except AttributeError as exception:
            # If no drawer is set then don't allow a script to run
            if self.drawer is None:
                print('Please select a drawer before trying to run scripts.')
            else:
                print(exception)
        else:
            # Start parsing the script
            self.source_reader.file_name = arg
            self.source_reader.go()

    def do_quit(self, arg):
        """Closes the program.
-----"""
        exit()

    def do_exit(self, arg):
        """Closes the program
-----"""
        exit()

    def parse(self, arg):
        # Convert arg to a tuple
        return tuple(map(int, arg.split()))


if __name__ == '__main__':
    app = TIGrEx()

    # Run specified tests
    if False:
        import doctest
        doctest.testmod(verbose=3)

    app.cmdloop()
