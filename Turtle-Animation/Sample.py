import turtle

trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing

screen.setup(400,300)    #choosing the screen size

screen.bgcolor('black')    #making canvas black

trtl.pencolor('red')    #making colour of the pen red

trtl.pensize(5)    #choosing the size of pen nib

trtl.speed(1)    #choosing the speed of drawing

trtl.shape('turtle')   #choosing the shape of pen nib

trtl.forward(100)    #top line
trtl.right(90)
trtl.forward(100)    # right vertical line
trtl.right(90)
trtl.forward(100)   # bottom line
trtl.right(90)
trtl.forward(100)   # left vertical line
# change position
trtl.penup()
trtl.setpos(-120,100)
trtl.pendown()
# clear screen
trtl.clearscreen()