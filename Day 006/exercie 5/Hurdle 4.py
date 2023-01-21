def move_right():
    while at_goal() != True and right_is_clear() != True:
        move()
    turn_left()
    turn_left()
    turn_left()
    if at_goal() != True:
        move()
 
def move_left():
    while front_is_clear() == True and at_goal() != True:
        move()
    turn_left()

def jump():
    move_left()
    move_right()
    move_right()
    move_left()
    
while at_goal() == 0:
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
