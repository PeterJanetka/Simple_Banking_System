# place `import` statement at top of the program
from string import capwords

# don't modify this code or the variable may not be available
input_string = input()

# use capwords() here
capitalized = []
for x in str.split(input_string):
    capitalized.append(str.capitalize(x))
print(' '.join(capitalized))
