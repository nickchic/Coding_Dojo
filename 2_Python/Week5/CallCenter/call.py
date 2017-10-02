from datetime import datetime

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
    def __repr__(self):
        return "-- Call ID: {}, Name: {}, Numer: {}, Time: {}, Reason: {} --".format(self.call_id, self.caller_name, self.caller_number, self.time_of_call, self.reason_for_call)
