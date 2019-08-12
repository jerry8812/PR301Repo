from TIGr import AbstractDrawer


class TextDrawer(AbstractDrawer):
    """
    Draws in Text

    Inherits:
    select_pen(pen_num), pen_down(), pen_up(), go_along(along), go_down(down), draw_line(direction, distance)
    """
    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        print('pen down')

    def pen_up(self):
        print('pen up')

    def go_along(self, along):
        print(f'GOTO X={along}')

    def go_down(self, down):
        print(f'GOTO Y={down}')

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')
