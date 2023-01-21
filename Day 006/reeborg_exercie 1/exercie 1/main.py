# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fselect_collection_en.json&name=Other%20worlds&url=%2Fworlds%2Fmenus%2Fselect_collection_en.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_right():
    move()
    turn_right()
    
turn_left()
move_right()
move_right()
move_right()
move()
