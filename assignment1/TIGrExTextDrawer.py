from TIGr import AbstractDrawer


class TextDrawer(AbstractDrawer):
    """Text Drawer

    Inherits:
    select_pen(pen_num), pen_down(), pen_up(), go_along(along), go_down(down), draw_line(direction, distance)
    """
    def __init__(self):
        super().__init__()
        print('Now using Text Drawer')

    def shutdown(self):
        print('No longer using Text Drawer.')

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        print('Pen down')

    def pen_up(self):
        print('Pen lifted')

    def go_along(self, along):
        print(f'Gone to X={along}')

    def go_down(self, down):
        print(f'Gone to Y={down}')

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')

    def clear(self):
        print('Cleared drawing')
