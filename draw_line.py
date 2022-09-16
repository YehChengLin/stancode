"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 30
d = False
x = 0
y = 0
z = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(function)


def function(a):
    global d, x, y, z
    if not d:
        c = GOval(SIZE, SIZE, x=a.x-SIZE/2, y=a.y-SIZE/2)
        window.add(c)
        x = c.x
        y = c.y
        d = True
        z = c
    else:
        window.remove(z)
        c2 = GLine(x+SIZE/2, y+SIZE/2, a.x, a.y)
        window.add(c2)
        d = False




























if __name__ == "__main__":
    main()
