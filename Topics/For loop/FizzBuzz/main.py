def function(number):
    for numbers in number:
        if numbers % 15 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)
function(range(1, 101))
