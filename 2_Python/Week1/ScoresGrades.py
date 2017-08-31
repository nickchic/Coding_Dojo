import random

def scores():
    for i in range(10):
        x = random.randint(60,100)
        print "Score:", x, "; Your grade is", grade(x);


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores()
