from stanfordkarel import *

def main():
    for i in range(2):
        move()
    turn_left()
    for i in range(5):
        move()
    put_beeper()
    turn_left()
    for i in range(3):
        loop()
    
def loop():
    for i in range(7):
        move()
    put_beeper()
    turn_left()

if __name__ =="__main__":
    run_karel_program()