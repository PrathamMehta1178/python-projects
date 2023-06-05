print(r'''Please type the full directry of the file you would like to be read
ex. C:\Users\prath\MyPythonScripts\demofile.txt
Make sure the file is in .txt format.''')
fileRead = input()
f = open(fileRead)
f1 = str(f.read())

count = {}

for charecter in str(f1).upper():
    count.setdefault(charecter, 0)
    count[charecter] = count[charecter]+1
print(count)
f.close()