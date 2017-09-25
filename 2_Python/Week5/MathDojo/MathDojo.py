class MathDojo(object):
    def __init__(self):
        self.value = 0
    #adds the total of the parameters to the value
    def add(self, addon, *addons):
        result = 0
        result += addToResult(addon)
        for num in addons:
            result += addToResult(num)
        self.value += result
        return self
    #subtracts the total of the parameters to the value
    def subtract(self, sub, *subs):
        result = 0
        result += addToResult(sub)
        for num in subs:
            result += addToResult(num)
        self.value -= result
        return self
    #prints and returns the current value
    def result(self):
        print self.value
        return self.value

#adds together variables based on their type and returns their value
def addToResult(num):
    result = 0
    if type(num) is list or type(num) is dict or type(num) is tuple:
        for i in num:
            result += i
    else:
        result += num
    return result

md = MathDojo()


md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
