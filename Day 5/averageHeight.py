#Calculate average of numbers in a list without using len() or sum()

height = input("Enter heights seperated by a space: ").split()

length = 0
total = 0
for n in height:
    length+=1

for n in range(0, length):
    total += int(height[n])

total = total/length

print(total)