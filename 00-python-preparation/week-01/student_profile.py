#Exercise 2

name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your university: ")
degree = input("Enter your degree: ")
mark1 = float(input("Enter Mark 1: "))
mark2 = float(input("Enter Mark 2: "))
mark3 = float(input("Enter Mark 3: "))

average = (mark1 + mark2 + mark3) / 3

print("\n----- Student Profile -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"University: {university}")
print(f"Degree: {degree}")
print()
print(f"Mark 1: {mark1}")
print(f"Mark 2: {mark2}")
print(f"Mark 3: {mark3}")
print()
print(f"Average Mark: {average:.2f}")