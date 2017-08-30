words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day", "month")
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y) - 1]
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
idx = 0
sub =[]
while idx < len(z)/2:
    sub.append(z[0])
    z.pop(z[0])
    idx += 1
print [sub] + z
