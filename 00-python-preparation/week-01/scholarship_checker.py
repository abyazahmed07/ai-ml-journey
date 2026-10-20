# Ask the user for their information
cgpa = float(input("Enter your CGPA: "))
ielts = float(input("Enter your IELTS score: "))

# Convert text responses to booleans using ==
has_research = input("Do you have research experience? (yes/no): ") == "yes"
is_suspended = input("Are you currently suspended? (yes/no): ") == "yes"

# Check the scholarship conditions
if cgpa >= 3.50 and (ielts >= 7.0 or has_research) and not is_suspended:
    print("Congratulations! You are eligible for the scholarship.")
else:
    print("Unfortunately, you are not eligible for the scholarship.")