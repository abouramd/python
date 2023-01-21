def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    if front_is_clear() == True:
        move()
    if wall_in_front() == True:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

while at_goal() == 0:
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
