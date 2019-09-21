"""
Turtle Drawer

By Sean Ryan
"""

from TIGr import AbstractDrawer
import turtle


class TurtleDrawer(AbstractDrawer):
    """Turtle Drawer

    Inherits:
    select_pen(pen_num), pen_down(), pen_up(), go_along(along), go_down(down), draw_line(direction, distance)

    Preset Pens:
    1 - colour black, size 10
    2 - colour red, size 10
    3 - colour blue, size 10


    Begin doctest - Written with Jonathan Holdaway and Sean Ryan 24/08/2019

    >>> drawer.select_pen(2)
    Selected pen 2
    >>> drawer.go_along(5)
    Gone to X=5
    >>> drawer.go_down(5)
    Gone to Y=5
    >>> drawer.pen_down()
    Pen down
    >>> drawer.draw_line(0, 5)
    drawing line of length 5 at 0 degrees
    >>> drawer.draw_line(90, 5)
    drawing line of length 5 at 90 degrees
    >>> drawer.draw_line(180, 5)
    drawing line of length 5 at 180 degrees
    >>> drawer.draw_line(270, 5)
    drawing line of length 5 at 270 degrees
    >>> drawer.pen_up()
    Pen lifted

    >>> drawer.clear()
    Cleared drawing

    End doctest
    """

    def __init__(self):
        super().__init__()
        print('Now using Turtle Drawer')
        self.turtle = turtle.Turtle()
        turtle.Screen().title('TIGrEx')
        # look up table for pen colour
        self.pen_colour = {1: 'black', 2: 'red', 3: 'blue'}

    @staticmethod
    def shutdown():
        print('No longer using Turtle Drawer')
        turtle.Screen().bye()

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')
        if pen_num in self.pen_colour:
            self.turtle.pen(fillcolor='white', pencolor=self.pen_colour[pen_num], pensize=10)
        else:
            print('Please choose a valid pen number.')

    def pen_down(self):
        print('Pen down')
        self.turtle.pendown()

    def pen_up(self):
        print('Pen lifted')
        self.turtle.penup()

    def go_along(self, along):
        print(f'Gone to X={along}')
        self.turtle.setx(along)

    def go_down(self, down):
        print(f'Gone to Y={down}')
        self.turtle.sety(down)

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')
        self.turtle.setheading(direction)
        self.turtle.forward(distance)

    def clear(self):
        print('Cleared drawing')
        self.turtle.clear()


if __name__ == '__main__':
    import doctest

    drawer = TurtleDrawer()
    doctest.testmod(verbose=3)
