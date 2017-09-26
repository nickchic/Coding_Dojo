from datetime import datetime
from call import Call
from CallCenter import CallCenter

call_1 = Call(1, "Nick", "215-870-4025", datetime(2017, 9, 25, 7, 16, 0), "Needs Help")
call_2 = Call(2, "Linds", "215-551-1306", datetime(2017, 9, 25, 7, 17, 0), "Is Mad")
call_3 = Call(3, "John", "215-333-4182", datetime(2017, 9, 25, 7, 18, 0), "Is Confused")
philly_calls = [call_1, call_2, call_3]

philly_call_center = CallCenter(philly_calls)

call_4 = Call(4, "Tom", "215-331-4299", datetime(2017, 9, 25, 7, 14, 0), "Is Dumb")

philly_call_center.info().add(call_4).info().sortCalls().info()

print philly_call_center
