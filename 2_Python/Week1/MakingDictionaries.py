nickDict = {'name':"Nick",'age':30,'country of birth':"USA",'favorite language':"C#"}

def printDict(d):
    for key,data in d.iteritems():
        print "My " + key + " is " + str(data)

printDict(nickDict)
