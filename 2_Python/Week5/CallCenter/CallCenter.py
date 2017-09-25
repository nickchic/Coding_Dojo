from datetime import datetime
import operator

class Call(object):
    def __init__(self, call_id, caller_name, caller_number, time_of_call, reason_for_call):
        self.call_id =  call_id
        self.caller_name =  caller_name
        self.caller_number =  caller_number
        self.time_of_call =  time_of_call
        self.reason_for_call =  reason_for_call
    def display(self):
        print "Call_ID: ", self.call_id, " Caller Name: ", self.caller_name, " Caller Number ", self.caller_number, " Time: ", self.time_of_call, " Reason: ", self.reason_for_call
        return self

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

call_1 = Call(1, "Nick", "215-870-4025", datetime(2017, 9, 25, 7, 16, 0), "Needs Help")
call_2 = Call(2, "Linds", "215-551-1306", datetime(2017, 9, 25, 7, 17, 0), "Is Mad")
call_3 = Call(3, "John", "215-333-4182", datetime(2017, 9, 25, 7, 18, 0), "Is Confused")
philly_calls = [call_1, call_2, call_3]

philly_call_center = CallCenter(philly_calls)

call_4 = Call(4, "Tom", "215-331-4299", datetime(2017, 9, 25, 7, 14, 0), "Is Dumb")

philly_call_center.info().add(call_4).info().sortCalls().info()
