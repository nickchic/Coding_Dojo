# Prints all the odd numbers from 1 to 1000
for num in range(0,1000):
    if not num % 2 == 0:
        print num

# Prints all the multiples of 5 from 5 to 1,000,000
for num in range(0,1000000):
    if num % 5 == 0:
        print num

a = [1, 2, 5, 10, 255, 3]

# prints the sum of all the values in the list
print sum(a)

# prints the sum of all the values in the list, without pre written function
total = 0
for idx in range(0,len(a)):
    total += a[idx]
print total

# Prints the average of the values in the list
print float(total)/len(a)
