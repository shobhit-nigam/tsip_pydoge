income = int(input())

if income < 0:
    tax = 0
elif income > 0 and income < 9950:
    tax = income * 0.1
elif income >= 9950 and income < 40525:
    tax = income * 0.12
else:
    tax = 0
    print("something has gone wrong")

print("tax to be paid =", tax)
