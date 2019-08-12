"""
TIGrEx
Tiny Interpreted Graphic Extended
"""
from TIGrExSourceReader import SourceReader
from TIGrExParser import Parser
from TIGrExTextDrawer import TextDrawer


class TIGrEx:
    def __init__(self, source_reader):
        self.source_reader = source_reader

    def go(self):
        self.source_reader.go()


if __name__ == "__main__":
    app = TIGrEx(SourceReader(Parser(TextDrawer())))
    app.go()
