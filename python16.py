class PrimeFinder:#class deine
    def __init__(self, start, end):#constructor
        self.start = start #store the start range
        self.end = end #store the end of range

    def is_prime(self, num):# prime numbeer check
        if num < 2: #return false beacuse prime no start from 2
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  #if no divisor found the function return true

    def display_primes(self): #find and display prime number 
        for num in range(self.start, self.end + 1): #Object that implement
            if self.is_prime(num):#if true they will print 
                print(num, end=" ")#print number on the same line 
        print()

start = int(input("Enter start of range: "))# Take input from the user 
end = int(input("Enter end of range: "))

prime_finder = PrimeFinder(start, end) #create an object 
prime_finder.display_primes()# display prime number  
