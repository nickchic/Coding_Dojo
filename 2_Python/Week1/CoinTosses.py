import random

def flips():
    heads = 0
    tails = 0
    for i in range(1,5001):
        message = "Attept #" + str(i) + ": It's "
        x = round(random.random())
        if x == 1:
            heads += 1
            message += "heads!"
        elif x == 0:
            tails += 1
            message += "tails!"
        message += " Got " + str(heads) + " heads and " + str(tails) + " tails so far."
        print message


flips()
