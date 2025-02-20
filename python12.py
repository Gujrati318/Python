class StringManipulator:
    def __init__(self):
        self.text = ""
    
    def get_string(self):
        self.text = input("Enter a string: ")
    
    def print_uppercase(self):
        print("Uppercase String:", self.text.upper())
string_obj = StringManipulator()
string_obj.get_string()
string_obj.print_uppercase()
