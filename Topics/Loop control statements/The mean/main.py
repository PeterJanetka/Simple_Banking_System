number_list = ['0']
total = 0
while number_list[-1] != ".":
    number_list.append(input())
else:
    for element in number_list[1:(len(number_list) - 1)]:
        total = total + int(element)
    print(total / (len(number_list) - 2))
