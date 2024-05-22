row1 = ['😶', '😶', '😶']
row2 = ['😶', '😶', '😶']
row3 = ['😶', '😶', '😶']
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the X?: ")

position1 = int(position[0]) - 1
position2 = int(position[1]) - 1

map[position1][position2] = "x"

print(f"{map[0]}\n{map[1]}\n{map[2]}")