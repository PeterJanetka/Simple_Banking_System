limit1 = int(input())
limit2 = int(input())
counter_found = 0
buffer = 0

for number in range(limit1, limit2 + 1):
    if number % 3 == 0:
        counter_found = counter_found + 1
        buffer = buffer + number

print(buffer / counter_found)
