# try this either as a .py file or in the python shell
import turtle

def makeCircle():
    # the distance we want the pointer to travel each time
    DIST = 10
    for x in range(0,18):
        print "x", x
        for y in range(1,5):
            print "y", y
            # turn the pointer 90 degrees to the right
            turtle.right(5)
            # advance according to set distance
            turtle.forward(DIST)

for i in range(0,4):
    makeCircle()
    turtle.right(90)
    turtle.forward(100)
