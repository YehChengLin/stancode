"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
VY = 0
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
d = False
c = GOval(SIZE, SIZE, x=START_X, y=START_Y)
x = 1

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    c.filled = True
    c.fill_color = 'black'
    window.add(c)
    onmouseclicked(function)


def function(a):
    global d, VX, GRAVITY, VY, REDUCE, DELAY, START_X, START_Y, c, x
    if not d:
        while True:
            c.move(VX, VY)
            if c.y < window.height:
                VY += GRAVITY
            if c.y > window.height:
                VY = -VY
                VY = VY*REDUCE
            if c.x > window.width:
                c.x = START_X
                c.y = START_Y
                break
            pause(DELAY)
            d = True
        VX = 3
        VY = 0
        d = False
        x += 1
    if x > 3:
        d = True















if __name__ == "__main__":
    main()
