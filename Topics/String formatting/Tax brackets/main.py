income = int(input())
percent = 0
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
elif income >= 132406:
    percent = 28
calculated_tax = int(income) * (percent / 100)
print(f'The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!')
