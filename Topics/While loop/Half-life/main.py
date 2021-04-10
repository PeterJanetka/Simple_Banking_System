initial_quantity = int(input())
final_quantity = int(input())
period = 0

while initial_quantity > final_quantity:
    initial_quantity = initial_quantity / 2
    period = int(period) + 1

print(period * 12)
