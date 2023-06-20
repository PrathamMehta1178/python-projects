from sys import argv

script, filename = argv # takes variables from user through terminal

txt = open(filename) # opens a fileobject in variable txt

print(f'Here is the file {filename}')
print(txt.read()) # reads content of the txt file object

print('Type the filename again') 
file_again = input('> ') # takes another file 

txt_again = open(file_again) # opens another file object in a new variable

print(txt_again.read()) # prints file obj 