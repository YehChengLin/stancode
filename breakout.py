"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    while True:
        global NUM_LIVES
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.find()
        graphics.wall()
        if graphics.ball.y > graphics.window.height:
            graphics.set_v()
            graphics.ball.x = graphics.window.width/2-graphics.ball.width/2
            graphics.ball.y = graphics.window.height/2-graphics.ball.height/2
            NUM_LIVES += -1
        if NUM_LIVES == 0:
            break
        pause(10)






    # Add the animation loop here!


if __name__ == '__main__':
    main()
