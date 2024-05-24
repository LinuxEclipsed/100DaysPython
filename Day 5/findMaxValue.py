#Find the max value without using max()

value = input("Input numbers seperated by space: ").split()

maxValue = 0
for n in value:
    n = int(n)
    if n > maxValue:
        maxValue = n

print(f"The max value is: {maxValue}")