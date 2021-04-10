deposit = int(input())
amount_without_protection = 700000
interest_rate = 0.071
years_safe = 0

while deposit < amount_without_protection:
    deposit = deposit * interest_rate + deposit
    years_safe += 1
    continue
print(years_safe)
