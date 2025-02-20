class NumberPalindrome:
    def __init__(self, number):
        self.number = number
    
    def get_palindrome(self):
        return int(str(self.number)[::-1])
num = int(input("Enter a number: "))
palindrome_generator = NumberPalindrome(num)
print("Palindrome of the number:", palindrome_generator.get_palindrome())
