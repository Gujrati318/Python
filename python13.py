class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width
    
    def display_area(self):
        print("Area of the rectangle:", self.compute_area())
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_obj = Rectangle(length, width)
rectangle_obj.display_area()
