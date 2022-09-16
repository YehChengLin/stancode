"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball




class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.start = False
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2-paddle_width/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(20, 20, x=window_width/2-ball_radius/2, y=window_height/2-ball_radius/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        self.__dx = 0
        self.__dy = 0
        onmousemoved(self.function1)
        onmouseclicked(self.function2)

       # Draw bricks
        self.brick = GRect(brick_width, brick_height, x=0, y=brick_offset)
        self.brick.filled = True
        self.brick.fill_color = 'red'
        self.brick.color = 'red'
        self.window.add(self.brick)
        for i in range(brick_rows):
            self.brick.y = brick_offset
            if i > 0:
                self.brick.x += (brick_spacing + brick_width)
            for j in range(brick_cols):
                self.brick.y += (brick_spacing+brick_height)
                self.brick = GRect(brick_width, brick_height, x=self.brick.x, y=self.brick.y)
                self.brick.filled = True
                if j == 1:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j == 2:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j == 3:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j == 4:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j == 5:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif j == 6:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif j == 7:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                elif j == 8:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                elif self.brick.x == window_width-brick_width:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                    if self.brick.y == brick_offset+((brick_spacing+brick_height)):
                        self.brick.fill_color = 'red'
                        self.brick.color = 'red'
                else:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                self.window.add(self.brick)

    def set_v(self):
        self.__dx = 0
        self.__dy = 0
        self.start = False

    def function1(self, a):
        self.paddle.x = a.x - PADDLE_WIDTH / 2
        if a.x > self.window.width - PADDLE_WIDTH:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        elif self.paddle.x < 0:
            self.paddle.x = 0

    def function2(self, b):
        if not self.start:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.start = True
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def wall(self):
        if self.ball.x > self.window.width:
            self.__dx = -self.__dx
        elif self.ball.x < 0:
            self.__dx = -self.__dx
        elif self.ball.y < 0:
            self.__dy = -self.__dy

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def find(self):
        for i in range(0, 3, 2):
            for j in range(0, 3, 2):
                y = self.window.get_object_at(self.ball.x + BALL_RADIUS * i, self.ball.y + BALL_RADIUS * j)
                if y is self.paddle:
                    self.__dy = -INITIAL_Y_SPEED
                    break
                if y is not None and y is not self.paddle:
                    self.__dy = -self.__dy
                    self.window.remove(y)
                    break





































