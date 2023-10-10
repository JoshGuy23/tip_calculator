print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = 1 + (float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100)

num_people = int(input("How many people to split the bill? "))

payment_per_person = round(bill / num_people * tip, 5)
print(f"Each person should pay: ${payment_per_person:.2f}")
