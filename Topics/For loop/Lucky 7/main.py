n = int(input())
number_pad = []

for i in range(n):
    number_pad.append(int(input()))
    i -= 1

for i in range(n):
    n -= 1
    use_number = number_pad.pop(0)
    if use_number % 7 == 0:
        print(use_number ** 2)
    i -= 1
