# Snakegame
import turtle
import random
import time

delay = 0.2
score = 0
high_score = 0
bodies = []

# Create screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("Black")
s.setup(width=600, height=600)

# Create head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("White")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.fillcolor("white")
food.penup()
food.goto(150, 200)
food.showturtle()

# Create scoreboard
sb = turtle.Turtle()
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(-250, 250)
sb.write("Score: 0 | Highest Score: 0", align="left", font=("Arial", 12, "normal"))

# Movement functions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Main game loop
try:
    while True:
        s.update()

        # Border wrapping
        if head.xcor() > 290:
            head.setx(-290)
        if head.xcor() < -290:
            head.setx(290)
        if head.ycor() > 290:
            head.sety(-290)
        if head.ycor() < -290:
            head.sety(290)

        # Collision with food
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add body segment
            body = turtle.Turtle()
            body.speed(0)
            body.shape("square")
            body.color("red")
            body.penup()
            bodies.append(body)

            # Increase score and speed
            score += 100
            delay = max(0.05, delay - 0.001)

            if score > high_score:
                high_score = score

            sb.clear()
            sb.write(f"Score: {score} | Highest Score: {high_score}", align="left", font=("Arial", 12, "normal"))

        # Move the body segments
        for i in range(len(bodies) - 1, 0, -1):
            x = bodies[i - 1].xcor()
            y = bodies[i - 1].ycor()
            bodies[i].goto(x, y)

        if len(bodies) > 0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x, y)

        move()

        # Collision with self
        for body in bodies:
            if body.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide and clear bodies
                for b in bodies:
                    b.hideturtle()
                bodies.clear()

                score = 0
                delay = 0.2
                sb.clear()
                sb.write(f"Score: {score} | Highest Score: {high_score}", align="left", font=("Arial", 12, "normal"))
                break

        time.sleep(delay)

except turtle.Terminator:
    print("Window closed. Exiting game safely.")

s.mainloop()
