def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while at_goal() != True and right_is_clear() != True and front_is_clear() == True:
        move()
    if right_is_clear() == True and at_goal() != True:
        turn_right()
        move()
    elif at_goal() != True:
        turn_left()
        if front_is_clear() == True:
            move()
    
while at_goal() == 0:
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
