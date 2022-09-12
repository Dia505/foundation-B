age = int(input("Please provide your age: "))

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
if age<0:
    print("invalid age, please input valid age")
elif 0<age<=10:
    print("the price of the ticket is 100")
elif 10<age<=20:
    print("the price of the ticket is 200")
else:
    print("the price of the ticket is 300")

