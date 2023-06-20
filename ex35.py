from sys import exit

def gold_room():
    print('This room is full of gold.\n How much do you take?')

    choice = input('> ')
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print('Nice, you\'re not greedy, you win!')
        exit(0)
    else:
        dead('too greedy')

def bear_room():
    print('''
    There is a bear here.
    The bear has a lot of honey.
    The bear is in front of another door.
    How do you move the bear?
    1. Take honey
    2. Taunt Bear
    3. Open door
    ''')
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == 'take honey':
            dead('The bear looks at you and slaps your face off.')
        elif choice == 'taunt bear' and not bear_moved:
            print('The bear moves away from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('The bear attacks and chews your legs off.')
        elif choice == 'open door':
            gold_room()
        else:
            print("I got no idea what that means")

def cthulu_room():
    print('Here you see the great evil Cthulu')
    print('He stares at you causing you to go insane')
    print('Do you flee or eat your head?')

    choice = input('> ')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('Well that was tasty!')
    else:
        cthulu_room()

def dead(why):
    print(why, 'Good job!')        
    exit(0)

def start():
    print('''
    You are in a dark room.
    There is a door to your left and right.
    Which one do you take?

    ''')

    choice = input('> ')

    if choice == 'left':
        bear_room()

    if choice == 'right':
        cthulu_room()
    else:
        dead('You stumble around the room until you starve.')

start()