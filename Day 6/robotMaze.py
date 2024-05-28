#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turnRight():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front()and not wall_on_right():
        turnRight()
    else:
        move()  