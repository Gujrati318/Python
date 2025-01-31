def create_tuple():
    n = int(input("Enter number of elements in tuple: "))
    return tuple(input(f"Enter element {i+1}: ") for i in range(n))

def display_menu():
    print("\nTuple Operations Menu:")
    print("1. Length of Tuple")
    print("2. Count occurrences of an element")
    print("3. Find index of an element")
    print("4. Find max and min (only for numeric tuples)")
    print("5. Convert tuple to list")
    print("6. Check if element exists")
    print("7. Concatenate two tuples")
    print("8. Slice the tuple")
    print("9. Iterate through tuple")
    print("10. Exit")

def main():
    my_tuple = create_tuple()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Length of tuple:", len(my_tuple))

        elif choice == '2':
            elem = input("Enter element to count: ")
            print(f"Count of {elem}: {my_tuple.count(elem)}")

        elif choice == '3':
            elem = input("Enter element to find index: ")
            if elem in my_tuple:
                print(f"Index of {elem}: {my_tuple.index(elem)}")
            else:
                print("Element not found.")

        elif choice == '4':
            try:
                num_tuple = tuple(map(float, my_tuple))
                print("Maximum element:", max(num_tuple))
                print("Minimum element:", min(num_tuple))
            except ValueError:
                print("Error: Tuple contains non-numeric elements.")

        elif choice == '5':
            print("Tuple converted to list:", list(my_tuple))

        elif choice == '6':
            elem = input("Enter element to check existence: ")
            print(f"{elem} exists?", elem in my_tuple)

        elif choice == '7':
            new_tuple = create_tuple()
            print("Concatenated Tuple:", my_tuple + new_tuple)

        elif choice == '8':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced Tuple:", my_tuple[start:end])

        elif choice == '9':
            print("Iterating through tuple:")
            for item in my_tuple:
                print(item)

        elif choice == '10':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()
