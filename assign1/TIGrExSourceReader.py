"""TIGrEx
Source Reader

By Sean Ryan
"""

from TIGr import AbstractSourceReader


class SourceReader(AbstractSourceReader):
    """Load source and store for parsing.

    Inherits:
    parser, file_name, source, init(parser, optional_file_name), go()


    Begin doctest - Written with Jonathan Holdaway and Sean Ryan 24/08/2019

    >>> source_reader.source = ['p 3', 'x 5', 'y 5', 'd' ,'e 5' ,'n 5' ,'w 5' ,'s 5' ,'u']
    >>> source_reader.go()
    Selected pen 3.0
    Gone to X=5.0
    Gone to Y=5.0
    Pen down
    drawing line of length 5.0 at 0 degrees
    drawing line of length 5.0 at 90 degrees
    drawing line of length 5.0 at 180 degrees
    drawing line of length 5.0 at 270 degrees
    Pen lifted

    End doctest
    """

    def __init__(self, parser):
        super().__init__(parser)
        self.script_extension = '.tigr'

    def go(self):
        self.parser.parse(self.source)


if __name__ == '__main__':
    import doctest
    from TIGrExParser import Parser
    from TIGrExTurtleDrawer import TurtleDrawer

    source_reader = SourceReader(Parser(TurtleDrawer()))
    doctest.testmod(verbose=3)
