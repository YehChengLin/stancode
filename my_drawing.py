"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect , GLine , GArc
from campy.graphics.gwindow import GWindow
window = GWindow()


def main():
    """
    TODO:
    """
    background = GRect(window.width, window.height, x=0, y=0)
    background.filled = True
    background.fill_color = 'black'
    window.add(background)

    c = GArc(100, 100, 20, 315)
    c.y = 150
    c.x = 50
    c.filled = True
    c.fill_color = 'yellow'
    c.color = 'yellow'
    window.add(c)

    eye = GOval(20, 20, x=c.x+20, y=c.y+20)
    eye.filled = True
    eye.fill_color = 'black'
    window.add(eye)

    point = GOval(10, 10, x=c.x + c.width/2+50, y=c.y + c.height/2)
    point.filled = True
    point.fill_color = 'red'
    point.color = 'red'
    window.add(point)

    point1 = GOval(10, 10, x=c.x + c.width / 2 + 100, y=c.y + c.height / 2)
    point1.filled = True
    point1.fill_color = 'red'
    point1.color = 'red'
    window.add(point1)

    point2 = GOval(10, 10, x=c.x + c.width / 2 + 150, y=c.y + c.height / 2)
    point2.filled = True
    point2.fill_color = 'red'
    point2.color = 'red'
    window.add(point2)

    point3 = GOval(10, 10, x=c.x + c.width / 2 + 200, y=c.y + c.height / 2)
    point3.filled = True
    point3.fill_color = 'red'
    point3.color = 'red'
    window.add(point3)

    point4 = GOval(10, 10, x=c.x + c.width / 2 + 250, y=c.y + c.height / 2)
    point4.filled = True
    point4.fill_color = 'red'
    point4.color = 'red'
    window.add(point4)

    point5 = GOval(10, 10, x=c.x + c.width / 2 + 300, y=c.y + c.height / 2)
    point5.filled = True
    point5.fill_color = 'red'
    point5.color = 'red'
    window.add(point5)

    point6 = GOval(10, 10, x=c.x + c.width / 2 + 350, y=c.y + c.height / 2)
    point6.filled = True
    point6.fill_color = 'red'
    point6.color = 'red'
    window.add(point6)

    point7 = GOval(10, 10, x=c.x + c.width / 2, y=c.y + c.height / 2 + 80)
    point7.filled = True
    point7.fill_color = 'red'
    point7.color = 'red'
    window.add(point7)

    point8 = GOval(10, 10, x=c.x + c.width / 2 + 50, y=c.y + c.height / 2+80)
    point8.filled = True
    point8.fill_color = 'red'
    point8.color = 'red'
    window.add(point8)

    point9 = GOval(10, 10, x=c.x + c.width / 2 + 100, y=c.y + c.height / 2+80)
    point9.filled = True
    point9.fill_color = 'red'
    point9.color = 'red'
    window.add(point9)

    point10 = GOval(10, 10, x=c.x + c.width / 2 + 150, y=c.y + c.height / 2 + 80)
    point10.filled = True
    point10.fill_color = 'red'
    point10.color = 'red'
    window.add(point10)

    point11 = GOval(10, 10, x=c.x + c.width / 2 + 200, y=c.y + c.height / 2 + 80)
    point11.filled = True
    point11.fill_color = 'red'
    point11.color = 'red'
    window.add(point11)

    point12 = GOval(10, 10, x=c.x + c.width / 2 + 250, y=c.y + c.height / 2 + 80)
    point12.filled = True
    point12.fill_color = 'red'
    point12.color = 'red'
    window.add(point12)

    point13 = GOval(10, 10, x=c.x + c.width / 2 + 300, y=c.y + c.height / 2 + 80)
    point13.filled = True
    point13.fill_color = 'red'
    point13.color = 'red'
    window.add(point13)

    point14 = GOval(10, 10, x=c.x + c.width / 2 + 350, y=c.y + c.height / 2 + 80)
    point14.filled = True
    point14.fill_color = 'red'
    point14.color = 'red'
    window.add(point14)

    point15 = GOval(10, 10, x=c.x + c.width / 2 + 400, y=c.y + c.height / 2 + 80)
    point15.filled = True
    point15.fill_color = 'red'
    point15.color = 'red'
    window.add(point9)

    point16 = GOval(10, 10, x=c.x + c.width / 2 + 450, y=c.y + c.height / 2 + 80)
    point16.filled = True
    point16.fill_color = 'red'
    point16.color = 'red'
    window.add(point16)


















if __name__ == '__main__':
    main()
