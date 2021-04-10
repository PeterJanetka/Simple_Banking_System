word = input()
new_string = ''
for char in word:
    if char.isupper():
        new_string += "_"
        new_string += char
    else:
        new_string += char

if new_string[0] == "_":
    new_string = new_string[1:]
    print(new_string.lower())
else:
    print(new_string.lower())
