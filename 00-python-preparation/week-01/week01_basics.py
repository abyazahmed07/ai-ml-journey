#Exercise 

name = input("Enter your name: ")
age = int(input("Enter your age: "))
language = input("Enter your favourite programming language: ")
hours = float(input("Enter hours studied today: "))
exercises = int(input("Enter number of exercises completed: "))

exercises_per_hour = exercises / hours

print("\n----- Study Summary -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favourite Language: {language}")
print(f"Hours Studied: {hours}")
print(f"Exercises Completed: {exercises}")
print(f"Exercises Per Hour: {exercises_per_hour}")