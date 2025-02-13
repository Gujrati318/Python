string = input("Enter a string: ")
upper_count = sum(1 for char in string if char.isupper())
lower_count = sum(1 for char in string if char.islower())

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
