def checkPrime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True

def checkPerfectSq(num):
    for i in range(2,num-1):
        if i*i == num:
            return True
    return False

for i in range(100,100000):
    if checkPerfectSq(i):
        print "Bar", i
    elif checkPrime(i):
        print "Foo", i
    else:
        print "Foobar", i
