# Without looping into the string

checkerA = "* * * * "
checkerB = " * * * *"

for i in range(0,4):
    print checkerA
    print checkerB


# With looping into the string

checkerC = ""
checkerD = " "

for i in range(0,4):
    checkerC += "* "
    checkerD += "* "

for i in range(0,4):
    print checkerC
    print checkerD


# Using different chracters!

def makeChecker(char):
    checkerE = ""
    checkerF = " "

    for i in range(0,4):
        checkerE += char + " "
        checkerF += char + " "

    for i in range(0,4):
        print checkerE
        print checkerF

makeChecker("d")
makeChecker("x")
newChar = "N"
makeChecker(newChar)
