import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'cyan', 'brown']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric... Try again!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try again!")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racers = turtle.Turtle()
        racers.color(color)
        racers.shape('turtle')
        racers.left(90)
        racers.penup()
        racers.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racers.pendown()
        turtles.append(racers)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"Winner is {winner}!")

# Checking GitKraken is working or not
# Checking another push
# Checking a push git-cola
# Checking again in git-cola
# Testing GitKraken
<<<<<<< HEAD

=======
# Creating branch and pushing...
# Creating conflict and resolve
>>>>>>> origin/check
