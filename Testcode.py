# #python practice after a long time 
# # How a loop work 

colors = ("red","green")
for color in colors:
    print(color) #print the color in colors
    for i in color:
        print(i)

# #range 

for i in range (20):
    print (i) # zero to 19 
    print(i+1) # 1 to 20

for i in range (3):
    print (i)

# # input in python 

var1 = int(input("enter your value :"))
var2 = int(input("enter your value :"))

sum = (var1 + var2)
print(sum)

score = 100
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")




#  function 
# a function is a block of code that run only when its called 

def fahrenheit_to_celsious(fahrenheit): #define function 
    return (fahrenheit -32) * 5/9 #actual function

