print('''You enter a dark room with two doors. 
Do you go through door #1 or door #2
''')

door = input('> ')

if door == '1':
    print("""
    Theres a giant bear here eating a cheesecake.
    What do you do?
    1. Take the cake.
    2. Scream at the bear.
    3. Befriend the bear
    """)

    bear = input('> ')

    if bear == "1":
        print('The bear eats your face off.')
    elif bear == '2':
        print('The bear eats your legs off.')
    elif bear == "3":
        print('The bear shakes your hand and hands over the cake.')
    else:
        print(f"Well doing {bear} is probably better")
        print('Bear runs away')

elif door == '2':
    print('''You stare into the endless abyss of Cthulu\'s retina
    1. Blueberries
    2. Yellowjacket clothespins
    3. Understanding revolvers singing melodies
    ''')

    insanity = input('> ')

    if insanity == '1' or '2':
        print('Your body barely survives\nGood job')
        print('You come across two other doors\nWhich one do you pick? 1 or 2?')
        doorTwo = input('> ')
        if doorTwo == '1':
            print()






    else:
        print('The insanity rots your eyes into a pool of muck\nGood job!!!')

else:
    print('You slip on a banana peel and fall onto a knife.')


