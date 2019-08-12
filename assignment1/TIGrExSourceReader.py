from TIGr import AbstractSourceReader


class SourceReader(AbstractSourceReader):
    """
    Load source

    Inherits:
    parser, file_name, source, init(parser, optional_file_name), go()
    """
    def go(self):
        self.source.append('P 2 # select pen 2')
        self.source.append('X 5 # go to 5 along')
        self.source.append('Y 15 # go to 15 down')
        self.source.append('D	# pen down')
        self.source.append('W 2	# draw west 2cm')
        self.source.append('N 1	# then north 1')
        self.source.append('E 2	# then east 2')
        self.source.append(' S  12.7 ')
        self.source.append(' U	# pen up')
        self.parser.parse(self.source)
