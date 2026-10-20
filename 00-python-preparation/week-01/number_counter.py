# Ask the user for a positive integer
number = int(input("Enter a number: "))

# Start our counter at 1
current = 1

# Keep looping until we reach the user's number
while current <= number:
    print(current)
    current += 1

# Print the final message after the loop ends
print("Counting complete!")