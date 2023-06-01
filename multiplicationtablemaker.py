#! python3
import os

# cleans the file from previous times
multTable = open('multTable.txt','w')
multTable.write('')
multTable.close()

print('Welcome to the multiplication table maker \nPlease enter a number')

def tableMaker():


    # get input from user / check if the input is a number
    userNum = input()
    try: userNum != int(userNum) # checks if numeber is valid
    except ValueError:
        print('Please enter a number\nex. 5,10,9')

    print('How many times would you like this number to be multiplied?')
    userNumMult = input()
    try: userNumMult != int(userNumMult) # checks if numeber is valid
    except ValueError:
        print('Please enter a number\nex. 5,10,9')

    actualuserNumMult = int(userNumMult) + 1

    # calculate the table until 10 and store data
    for i in range(1,int(actualuserNumMult)):
        multTable = open('multTable.txt','a')
        data = int(userNum) * i
        equation = str(userNum) +' x '+str(i)+' = '+str(data)
        multTable.write(equation+'\n')

    # check if they want to enter another number
    print('Would you like to add another number to the table?\nType yes or no')
    repeat = input()
    if repeat.capitalize() == 'Yes':
        multTable = open('multTable.txt','a')
        multTable.write('\n\n')
        multTable.close()
        print('Please enter a number')
        tableMaker()
        
    else:
        print('Thank you for using MultTableMaker\nTo find your data go to '+os.getcwd()+' and open the multTable file')

tableMaker()
