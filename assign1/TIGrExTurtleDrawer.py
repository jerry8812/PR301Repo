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


    Begin doctest - Written with Jonathan Holdaway and Sean Ryan 23/08/2019

    End doctest
    """
    def __init__(self):
        super().__init__()
        print('Now using Turtle Drawer')
        self.turtle = turtle.Turtle()

    def shutdown(self):
        print('No longer using Turtle Drawer')
        turtle.bye()

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')
        if pen_num == 1:
            turtle.pen(fillcolor='white', pencolor='black', pensize=10)
        elif pen_num == 2:
            turtle.pen(fillcolor='white', pencolor='red', pensize=10)
        elif pen_num == 3:
            turtle.pen(fillcolor='white', pencolor='blue', pensize=10)
        else:
            print('Please choose a valid pen number.')

    def pen_down(self):
        print('Pen down')
        turtle.pendown()

    def pen_up(self):
        print('Pen lifted')
        turtle.penup()

    def go_along(self, along):
        print(f'Gone to X={along}')
        turtle.setx(along)

    def go_down(self, down):
        print(f'Gone to Y={down}')
        turtle.sety(down)

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')
        turtle.setheading(direction)
        turtle.forward(distance)

    def clear(self):
        print('Cleared drawing')
        turtle.clear()
