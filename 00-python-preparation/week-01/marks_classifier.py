marks = [72, 91, 66, 88, 95, 79]

# Initialize a counter for excellent students
excellent_count = 0

# Loop through each mark in the list
for mark in marks:
    if mark >= 80:
        print(f"{mark} - Excellent")
        excellent_count += 1
    else:
        print(f"{mark} - Needs Improvement")

# Print the final total after the loop
print(f"\nTotal excellent students: {excellent_count}")