## write a file from a list with each name on a new line
 
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

output = open('names.txt', 'w')

for name in people:
    output.write(name + '\n')

output.close()

##################################################################

try:
    error = open('names.txt', 'r')

except FileNotFoundError:
    print('That file is in another castle')

finally:
    error.close()

###################################################################

## write a file from a list with a random name on a new line

from itertools import count
from random import shuffle
from typing import Counter

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

output = open('randnames.txt', 'w')

for name in people:
    shuffle(people)
    output.write(name + '\n')

output.close()

##################################################################

#Create a Python file that reads the file in. Create a dictionary where the key is the name and the value is the
#number of times the name appears in the text file.

with open('randnames.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

counts = Counter(lines)
print(counts)

##################################################################