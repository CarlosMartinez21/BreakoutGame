import turtle
from turtle import Screen, Turtle
from brick import Brick
from ball import Ball
from random import randint

# Paddle Movement Function
def move_left():
    new_x = paddle.xcor() - 20
    paddle.goto(new_x, paddle.ycor())


def move_right():
    new_x = paddle.xcor() + 20
    paddle.goto(new_x, paddle.ycor())


def wall_collision():
    global toggle_x
    toggle_x = not toggle_x


def brick_collision():
    global toggle_y
    toggle_y = not toggle_y

def update_lives_levels():
    global lives, level
    score_text.clear()
    score_text.penup()
    score_text.goto(-275, 275)
    score_text.color('white')
    score_text.write(f'lives: {lives}', move=False, font=('monaco', 20, 'bold'), align='left')
    level_text.clear()
    level_text.penup()
    level_text.goto(275, 275)
    level_text.color('white')
    level_text.write(f'level: {level}', move=False, font=('monaco', 20, 'bold'), align='left')

# Game Init
lives = 3
level = 1

# Screen Definition
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("Breakout")
screen.tracer(0)
score_text = Turtle()
score_text.hideturtle()
level_text = Turtle()
level_text.hideturtle()
update_lives_levels()



# Paddle Definition
paddle = Turtle()
paddle.penup()
paddle.sety(-300)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(.5, 8)

# Paddle Event Listeners
screen.listen()
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# Ball Definition
ball = Ball()
toggle_x = 1
toggle_y = 1



# Bricks Setup
bricks = []
init_x = -350
init_y = 0


def create_rows(startx, starty):
    brickx = startx
    bricky = starty
    for x in range(8):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        name = 'brick' + str(x)
        name = Brick(color=color, positionx=brickx, positiony=bricky)
        bricks.append(name)
        if brickx + 100 < 770:
            brickx += 100


def repeater(num):
    global init_x,init_y
    brickx = init_x
    bricky = init_y
    update_lives_levels()
    for i in range(num):
        create_rows(brickx, bricky)
        bricky += 50

def death():
    global lives, toggle_x, toggle_y, game_is_on
    lives -= 1
    if lives > 0:
        ball.goto(0, -285)
        toggle_x = 1
        toggle_y = 1
        update_lives_levels()
    else:
        lives = 0
        text = Turtle()
        text.penup()
        text.goto(-50, 0)
        text.color('white')
        text.write('Game Over!', move=False, font=('monaco', 30, 'bold'), align='left')
        ball.reset()
        update_lives_levels()
        game_is_on = False


create_rows(init_x, init_y)


# game initialization
game_is_on = True
while game_is_on:
    screen.update()
    ball.move(toggle_x, toggle_y)
    # Check for right,left, and top wall Collisions
    if ball.xcor() > 385 or ball.xcor() < -385:
        wall_collision()
        # Ball Collision with Brick
    if ball.ycor() > 335:
        brick_collision()
        # Ball Collision with Paddle left side
    if ball.ycor() < paddle.ycor() + 10 and paddle.xcor() - 70 < ball.xcor() < paddle.xcor():
        toggle_x = 0
        toggle_y = 1
    # Ball Collision with Paddle right side
    if ball.ycor() < paddle.ycor() + 10 and paddle.xcor() < ball.xcor() < paddle.xcor() + 70:
        toggle_x = 1
        toggle_y = 1
    #   Ball calls Death Logic
    if ball.ycor() < -325:
        death()
    # Bricks hit Detections
    for brick in bricks:
        if brick.ycor() - 5 < ball.ycor() < brick.ycor() + 5 and brick.xcor() - 50 < ball.xcor() < brick.xcor() + 50:
            brick.reset()
            bricks.remove(brick)
            brick_collision()
    if len(bricks) == 0:
        level += 1
        repeater(level)


screen.exitonclick()

