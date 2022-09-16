# age = int(input("Please provide your age: "))

# conditional statement
# if block only

"""
print("code started ....")
if age>18:
    print(f"you can play the game because you are above {age}")

print("code ended ....")

#if-else block
if age>18:
    print(f"you can play the game since you're above {age}")
else:
    print("you need to be above 18 to play")
"""

# proper use of if-elif-else block
"""
if age<0:
    print("invalid age, please input valid age")
elif 0<age<=10:
    print("the price of the ticket is 100")
elif 10<age<=20:
    print("the price of the ticket is 200")
else:
    print("the price of the ticket is 300")
"""
# ask a two integer number with user and a function should return their addition
"""
a = int(input("Please enter a number:"))
b = int(input("Please enter another number:"))
def addition(num1,num2):
    sum = num1+num2
    return sum
print(f"The sum of the above numbers is {addition(a,b)}")
"""
"""
brandname = str(input("Provide brand name"))
model = str(input("Provide model name"))
price = int(input("Provide price"))
def info(brand_name,model_name,laptop_price):
    return f"{brand_name} {model_name} @ Rs.{laptop_price}"
print(info(brandname,model,price))
"""
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
"""
a = int(input("Please enter first number:"))
b = int(input("Please enter second number"))
def multiplication(n1,n2):
    product=n1*n2
def addition(n1,n2):
    sum=n1+n2
 if product<=1000:
    return product
 else:
    return sum
print(f"The result is {multiplication(a,b)}")
"""
#loops in python
#range function in python
#print(f"the range from 1 to 10 is: {range(1,10+1)}")
for num in range(1,11):
    print ("the number in range is: --> {num}")