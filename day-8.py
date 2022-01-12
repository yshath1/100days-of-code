# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# num=int(input("input your number to check for prime: "))
# def primenum(number): 
#   if number > 1:
#     for i in range(2, number//2):
#       if (number % i) == 0:
#         print("is not a prime number")
#         break
#     else:
#       print( "is a prime number")
#   else:
#     print( "is not a prime number")

# primenum(number=num)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
my_string  = "hello"
difference = +5
new_string = ''.join((chr(97+(ord(letter)-97+difference) % 26) for letter in my_string))
print(new_string)