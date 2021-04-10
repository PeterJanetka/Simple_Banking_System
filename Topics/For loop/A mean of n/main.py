n = int(input())
counter = 0
delitel = n
for _ in range(n):
    counter = int(counter) + int(input())
    n -= 1

print(int(counter) / int(delitel))
