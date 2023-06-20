from sys import argv

script, user_name = argv
prompt = '> '

print(f'Hi {user_name}, im the {script} script.')
print('i ask questions')
print(f'do you like me {user_name}')
likes = input(prompt)

print(f'Where do you live {user_name}')
lives = input(prompt)

print('what kind of computer do you have?')
computer = input(prompt)

print(f''' 
      Alright {user_name}, you said 
      {likes} about liking me and 
      you live at {lives}. I am 
      coming. Also, you have a 
      {computer}. Its okay i guess.
        ''')