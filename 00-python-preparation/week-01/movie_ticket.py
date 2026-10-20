# Ask the user for their age
age = int(input("Enter your age: "))

# Determine the ticket price based on age brackets
if age < 5:
    print("Your ticket price is Free")
elif age <= 12:
    print("Your ticket price is BDT 200")
elif age <= 59:
    print("Your ticket price is BDT 500")
else:
    print("Your ticket price is BDT 300")