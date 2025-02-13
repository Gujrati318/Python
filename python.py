s = "this is a simple string"

while True:
    print("\nMenu:")
    print("1. Display length of the string")
    print("2. Display character count")
    print("3. Split the string")
    print("4. Convert to uppercase (if lowercase letters exist)")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Length of the string:", len(s))
    elif choice == "2":
        print("Character count:", {char: s.count(char) for char in set(s)})
    elif choice == "3":
        print("Split string:", s.split())
    elif choice == "4":
        print("String in :", s.upper())
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
