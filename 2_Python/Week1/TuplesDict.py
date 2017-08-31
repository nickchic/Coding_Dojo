my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makeTuple(d):
    newTuple = []
    for key,data in d.iteritems():
        newTuple.append((key,data))
    return newTuple

print makeTuple(my_dict)
