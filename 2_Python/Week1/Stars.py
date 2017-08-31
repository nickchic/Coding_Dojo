mix = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(arr):
    for i in arr:
        newStr = ""
        for j in range(i):
            newStr += "*"
        print newStr

def draw_stars_letters(arr):
    for i in arr:
        newStr = ""
        if type(i) is int:
            for j in range(i):
                newStr += "*"
            print newStr
        elif type(i) is str:
            for j in range(len(i)):
                newStr += i[0].lower()
            print newStr


draw_stars(x)
draw_stars_letters(mix)
