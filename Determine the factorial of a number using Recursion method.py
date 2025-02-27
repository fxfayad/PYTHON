n = int(input("Enter a number: "))  
fact = 1
temp = n  

while temp > 1:
    fact *= temp
    temp -= 1

print(f"Factorial of {n} is {fact}")