from sys import argv
from os.path import exists

script, from_file, to_file = argv
infile = open(from_file )
indata = infile.read()
outfile = open(to_file, 'w')
outfile.write(indata)
outfile.close()
infile.close()      
print(f'Copying from {from_file} to {to_file}')



print(f'There is {len(indata)} bytes stored in this file')
print(f'Does this file exist? {exists(to_file)}')
print('READY, hit RETURN to continue, and CTRL-C to abort the program.')
input()

print('Finished')
