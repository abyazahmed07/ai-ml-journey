# 1. Create the list
subjects = ["Math", "English", "Physics", "Math", "Biology"]

# 2. Print the original list
print("Original subjects:", subjects)

# 3. Add "Chemistry" using a list method
subjects.append("Chemistry")

# 4. Remove "English" using a list method
subjects.remove("English")

# 5. Print the updated list
print("Updated subjects:", subjects)

# 6. Convert the updated list into a set to remove duplicates
unique_subjects = set(subjects)

# 7. Print the unique subjects and the total number of unique subjects
print("Unique subjects:", unique_subjects)
print("Total unique subjects:", len(unique_subjects))