#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    if right_is_clear():
        turnRight()
        move()
    if not right_is_clear():
        while not right_is_clear():
            move()
        turnRight()
    if not wall_in_front():
        move()
        turnRight()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if front_is_clear() and not is_facing_north():
        move()
    elif wall_in_front():
        jump()

# Course Version
def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turnRight()
    move()
    turnRight()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()