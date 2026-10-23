numbers = [10, 20, 30, 40, 50, 60, 70]

# 1. First number -> index 0
print(numbers[0])

# 2. Last number -> negative indexing, -1 is the last element
print(numbers[-1])

# 3. First three numbers -> from start up to (but not including) index 3
print(numbers[:3])

# 4. Numbers from 30 through 50 -> 30 is at index 2, stop at index 5 (exclusive)
print(numbers[2:5])

# 5. Every second number starting from 10 -> step of 2 (indices 0, 2, 4, 6)
print(numbers[::2])

# 6. List in reverse order -> step of -1 walks backwards
print(numbers[::-1])