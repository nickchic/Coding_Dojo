tableString = "x"
for x in range(1,13):
    tableString += "  " + str(x)
print tableString
for j in range(1,13):
    tableString = str(j)
    for i in range(1,13):
        tableString += "  " + str(i*j)
    print tableString
