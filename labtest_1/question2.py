# Take input from user as a list of integers
user_input = input("Enter a list of integers separated by commas (e.g., 1,1,2,6,4,4,2,9,8,5,7,7): ")
nums = [int(x.strip()) for x in user_input.split(',')]

# Remove duplicates by converting to set, then sort the result
unique_sorted = sorted(set(nums))

# Print the result
print(unique_sorted)