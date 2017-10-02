from datetime import datetime
import operator

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(self.calls)
    def add(self, new_call):
        self.calls.append(new_call)
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def remove_from_number(self, number):
        found = False
        for index, call in enumerate(self.calls):
            if call.caller_number == number:
                self.calls.pop(index)
                found = True
        if not found:
            print "No Matching Number Found"
        return self
    def info(self):
        print "Current Queue ", self.queue_size
        idx = 0
        for call in self.calls:
            print "-- Call {} ---".format(idx)
            idx += 1
            print "Caller Name: ", call.caller_name, " Caller Number: ", call.caller_number
        return self
    def sortCalls(self):
        self.calls.sort(key=operator.attrgetter('time_of_call'))
        return self
    def __repr__(self):
        return "Queue Size: {}, Calls: {}".format(self.queue_size, self.calls)
