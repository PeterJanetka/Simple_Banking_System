string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

number_count2 = 0
for char in vowels:
    number_count2 += string.count(char)

print(number_count2)

# number_count = 0
# print(
#     int(string.count('a'))
#     + int(string.count('e'))
#     + int(string.count('i'))
#     + int(string.count('o'))
#     + int(string.count('u')))
