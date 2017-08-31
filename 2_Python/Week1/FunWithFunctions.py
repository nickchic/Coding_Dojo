def odd_even():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is", i, ". This is and even number"
        else:
            print "Number is", i, ". This is and odd number"

def multiply(arr, value):
    returnArr = []
    for i in arr:
        returnArr.append(i*value)
    return returnArr

a = [2,4,10,16]
b = multiply(a, 5)
print b

def hacker(arr):
    returnArr = []
    for i in arr:
        newValue = []
        for j in range(i):
            newValue.append(1)
        returnArr.append(newValue)
    return returnArr


x = hacker(multiply([2,4,5],3))
print x
