import turtle
import random
import math
import time
import winsound

# Setting up the Screen
ms = turtle.Screen()
ms.bgcolor("red")
ms.title("Space Rocket Minigame @Rafa94")
ms.bgpic("C:/Users/Rafael Perez/PycharmProjects/hello/venv/spacebg.gif")
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/hello/venv/r7.gif")
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/hello/venv/star3.gif")
ms.register_shape("C:/Users/Rafael Perez/PycharmProjects/hello/venv/bad_guy.gif")


# Subclass
class Game(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial",14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self):
        winsound.PlaySound("collision.wav")
        #winsound.PlaySound("bounce.wav")

    def play_sound2(self):
        winsound.PlaySound("collision2.wav")



# Using class functions/Methods

# subclass
class Border(turtle.Turtle):
    def __init__(self):  # class constrcutor
        turtle.Turtle.__init__(self)  # adding our Objects attributes all starting with "self"
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("silver")
        self.pensize(5)

    def draw_border(self):
        self.penup()# getting our pen to start drawing
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

class Player(turtle.Turtle):  # since it got inherited this class becomes a Superclass/SUPER CLASS

    def __init__(self):  # self is our only argument here but it will have multiple attributes
        turtle.Turtle.__init__(self)  # since we are using the Turtle module, we are able to use it's built in functions
        self.penup()# our attributes
        self.speed(0)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/hello/venv/r7.gif")
        self.color("black")
        self.velocity = 0.1

    def move(self):
        self.forward(self.velocity)

        # Border Checking
        if self.xcor() > 290 or self.xcor() < -290:  # Left side is -290 Right side is 290 we also want the coordinates x and y to be below 300 to not go over our border
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def down(self):
        self.forward(30)

    def increasespeed(self):
        self.velocity += 1


class Goal(turtle.Turtle):  # Sub Class

    def __init__(self):
        # since we are using the Turtle module we are able to use it's built in functions
        turtle.Turtle.__init__(self)
        self.penup()  # our attributes
        self.speed(0)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/hello/venv/star3.gif")
        self.color("green")
        self.velocity = 3  #xcor                    #ycor
        self.goto(random.randint(-250, 250), random.randint(-250, 250))  # we are making our turtle "go to" X & Y coordinates by -250 and 250 only randomly. We also have our random module here aswell
        self.setheading(random.randint(0, 360))  # setting the heading to see in which direction i want it to go

    def jump(self):  # Jump = Collidee
        self.goto(random.randint(-250, 250), random.randint(-250, 250))  # "jump" stands for Collidee so if the circle "jumps" with player it will move to random postion by 250 and -25
        self.setheading(random.randint(0, 360))  # from where it collidee's it goes 360 moves location 360 Right

    def move(self): # we copyed the same method cause it will be doing the same movements as the player we want it to go "forward" with our set "speed" & also check for our borders we set
        self.forward(self.velocity)


        # Border Checking
        if self.xcor() > 290 or self.xcor() < -290:  # Left side is -290 Right side is 290 we also want the coordinates x and y to be below 300 to not go over our border
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)
            #winsound.PlaySound("C:/Users/Rafael Perez/PycharmProjects/hellovenv/bounce.wav", winsound.SND_ASYNC)

# Collision checking function/Method
# Uses the Pythgorean Theorem to measure the distance between two objects

def isCollision(t1, t2):  # t1 = turtle1 t2 = turtle also when a function starts with  "is" isCollision most likely it will be a Boolean of True or False
    a = t1.xcor()-t2.xcor()  # xcor = Right -xcor = Left/ when they collide the xcor is 0
    b = t1.ycor()-t2.ycor()# ycor = Right -ycor = Left/ when they collide the ycor is 0

    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 30:
        return True
    else:
        return False

class Bad_guys(turtle.Turtle):
    def __init__(self):
        # since we are using the Turtle module we are able to use it's built in functions
        turtle.Turtle.__init__(self)
        self.penup()  # our attributes
        self.speed(0)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/hello/venv/bad_guy.gif")
        self.color("red")
        self.velocity = 3  # xcor                    #ycor
        self.goto(random.randint(-150, 250), random.randint(-150, 250))
        self.setheading(random.randint(0,160))

    def jump(self):  # Jump = Collidee
        self.goto(random.randint(-250, 250), random.randint(-250, 250))  # "jump" stands for Collidee so if the circle "jumps" with player it will move to random postion by 250 and -25
        self.setheading(random.randint(0, 360))  # from where it collidee's it goes 360 moves location 360 Right

    def move(self): # we copyed the same method cause it will be doing the same movements as the player we want it to go "forward" with our set "speed" & also check for our borders we set
        self.forward(self.velocity)


        # Border Checking
        if self.xcor() > 290 or self.xcor() < -290:  # Left side is -290 Right side is 290 we also want the coordinates x and y to be below 300 to not go over our border
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

def isCollision2(t1, t2):  # t1 = turtle1 t2 = turtle also when a function starts with  "is" isCollision most likely it will be a Boolean of True or False
    a = t1.xcor()-t2.xcor()  # xcor = Right -xcor = Left/ when they collide the xcor is 0
    b = t1.ycor()-t2.ycor()# ycor = Right -ycor = Left/ when they collide the ycor is 0

    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 30:
        return True
    else:
        return False



# Create class instances
player = Player()  # after creating a class must make instances to call it in other words make an Object of the class
border = Border()  # sub class
bad_guy = Bad_guys()
#goal = Goal()  #sub class
game = Game()
#TIP - every time you make a class you must make object/instance for it ^


# Draw our border
border.draw_border()

#create multiple goals
goals = []  # Creating a list of goals
for count in range(4):  # We are making the code repeat 6 times
    goals.append(Goal()) # each time the code runs it puts a goal the end 6 times

bad_goals = []  # Creating a list of goals
for count in range(4):  # We are making the code repeat 6 times
    bad_goals.append(Bad_guys())



# Set keyboard bindings
ms.listen()
ms.onkey(player.turnleft, "Left")
ms.onkey(player.turnleft, "Right")
ms.onkey(player.increasespeed, "Up")




# speed game up
ms.tracer(0.1)

# main loop
while True:
    ms.update()
    bad_guy.move()
    player.move() # these two are class methods
    # the reason we copyed like we said is cause it's gunna have the exact same movements as our player!
    for goal in goals:
        goal.move()# Basically saying If there is a collision between the player and goal we the want the goal to "jump" / Function in our while True loop
        if isCollision(player, goal):
            goal.jump()
            game.change_score(10) # if there is collision score will give me 10 point
            #TIP - Turtle module package only uses .wav sound files
            winsound.PlaySound("C:/Users/Rafael Perez/PycharmProjects/hello/venv/collision.wav", winsound.SND_ASYNC)

    for bad_goal in bad_goals:
        bad_goal.move()#Basically describing how the movement of our bad_guys will be exact as the player
        if isCollision2(player, bad_goal):#Had to make another  iscollision to put our bad_guys in
            bad_goal.jump()
            game.change_score(-10)
            winsound.PlaySound("C:/Users/Rafael Perez/PycharmProjects/hello/venv/collision2.wav", winsound.SND_ASYNC)

        #We Basically did everything we the bad guys as we did with the good guys we just used the while True loop and put all the methods
        # And parameters underneath our good guys for loop







                              
            #goal.jump()














    time.sleep(0.005)




ms.mainloop()
