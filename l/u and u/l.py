string = input("Enter a string: ")
result = "".join(
    char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(string)
)
print("Result:", result)
