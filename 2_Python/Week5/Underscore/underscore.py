class Underscore(object):
    def map(self, ls, func):
        returnList = []
        for x in ls:
            returnList.append(func(x))
        return returnList
    def reduce(self, ls, func, idx):
        returnValue = 0
        for x in range(idx+1, len(ls)+1):
            returnValue = func(returnValue, x)
        return returnValue
    def find(self, ls, func):
        for x in ls:
            if func(x):
                return x
        return None
    def filter(self, ls, func):
        returnList = []
        for x in ls:
            if func(x):
                returnList.append(x)
        return returnList
        # your code
    def reject(self, ls, func):
        returnList = []
        for x in ls:
            if not func(x):
                returnList.append(x)
        return returnList
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "Evens = ", evens
# should return [2, 4, 6] after you finish implementing the code above

map_test = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 2)
print "Map = ",map_test

def reduce_func(memo, num):
    return memo + num

reduce_test = _.reduce([1, 2, 3, 4, 5, 6], reduce_func, 0)
print "Reduce = ",reduce_test

find_test = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0)
print "Find = ",find_test

reject_test = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print "Reject = ",reject_test
