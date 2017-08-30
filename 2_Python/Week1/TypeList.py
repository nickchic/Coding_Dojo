ls = ['magical unicorns',19,'hello',98.98,'world']
strLs = ['john','sue','wendy']
intLs = [19,5,13,15]

def typeList(value):
    stringNum = 0
    intNum = 0
    stringList = []
    intList = []
    for idx in range(0,len(value)):
        if type(value[idx]) is int or type(value[idx]) is float:
            intNum += 1
            intList.append(value[idx])
        elif type(value[idx]) is str:
            stringNum += 1
            stringList.append(value[idx])

    if intNum == len(value):
        print "The list is all Int Type"
        toPrint = 0
        for idx in range(0,len(value)):
            toPrint += value[idx]
        print "Sum =", toPrint

    elif stringNum == len(value):
        print "The list is all String Type"
        toPrint = ""
        for idx in range(0,len(value)):
            toPrint += value[idx] + " "
        print "String =",toPrint

    else:
        print "The list is mixed"

        toPrintStr = ""
        for idx in range(0,len(stringList)):
            toPrintStr += stringList[idx] + " "
        print "String =",toPrintStr

        toPrintInt = 0
        for idx in range(0,len(intList)):
            toPrintInt += intList[idx]
        print "Sum =",toPrintInt


typeList(ls)
typeList(strLs)
typeList(intLs)
