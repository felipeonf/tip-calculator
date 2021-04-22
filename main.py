print("Welcome to the tip calculator!")
bill = float(input("What´s the total bill? $ "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tax = (100 + percentage) / 100
division = int(input("How many people to split the bill? "))
payment_per_people = (bill * tax) / division
print(f'Each person should pay : $ {payment_per_people:.2f}')
