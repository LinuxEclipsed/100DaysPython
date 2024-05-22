import random

people = input("Names:")
people = people.split(", ")

countPeople = len(people) -1

randomPerson = random.randint(0, countPeople)

print(f"{people[randomPerson]} pays the bill")