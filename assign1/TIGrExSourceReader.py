from TIGr import AbstractSourceReader


class SourceReader(AbstractSourceReader):
    """Load source and store for parsing.

    Inherits:
    parser, file_name, source, init(parser, optional_file_name), go()


    Begin doctest - Written with Jonathan Holdaway and Sean Ryan 23/08/2019

    End doctest
    """
    def __init__(self, parser):
        super().__init__(parser)
        self.script_extension = '.tigr'

    def go(self):
        self.parser.parse(self.source)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=3)
