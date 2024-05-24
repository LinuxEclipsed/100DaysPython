#1-100; When a number is divisible by 3 print fizz. When a number is divisiable by 5 print buzz if divisable by 3 and 5 print fizzbuzz
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)