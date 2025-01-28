def display_list(lst):
    print("Current List:", lst)

def add_element(lst):
    element = input("Enter element to add: ")
    lst.append(element)
    print(f"{element} added.")

def remove_element(lst):
    element = input("Enter element to remove: ")
    if element in lst:
        lst.remove(element)
        print(f"{element} removed.")
    else:
        print(f"{element} not found.")

def pop_element(lst):
    index = int(input("Enter index to pop: "))
    if index < len(lst):
        removed = lst.pop(index)
        print(f"Element {removed} popped.")
    else:
        print("Invalid index.")

def sort_list(lst):
    lst.sort()
    print("List sorted.")

def reverse_list(lst):
    lst.reverse()
    print("List reversed.")

def main():
    my_list = []

    while True:
        print("\nMenu:")
        print("1. Add Element")
        print("2. Remove Element")
        print("3. Display List")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_element(my_list)
        elif choice == 2:
            remove_element(my_list)
        elif choice == 3:
            display_list(my_list)
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
