first_number = float(input())
second_number = float(input())
operation = input()

if operation == "+":
    print(float(first_number) + float(second_number))

elif operation == "-":
    print(float(first_number) - float(second_number))

elif operation == "/":
    if second_number == 0:
        print("Division by 0!")
    else:
        print(float(first_number) / float(second_number))

elif operation == "*":
    print(float(first_number) * float(second_number))

elif operation == "mod":
    if second_number == 0:
        print("Division by 0!")
    else:
        print(float(first_number) % float(second_number))

elif operation == "pow":
    print(float(first_number) ** float(second_number))

elif operation == "div":
    if second_number == 0:
        print("Division by 0!")
    else:
        print(float(first_number) // float(second_number))
