#filtering number to odd and even list
"""
a_num=int(input("Please enter any number:"))
even_list=[]
odd_list=[]
def odd_even(user_num):
    for num in range (1,user_num+1):
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
odd_even(a_num)
print(f"The odd list is {odd_list}")
print(f"The even list is {even_list}")

#printing sum
first_num=int(input("Please enter a number:"))
second_num=int(input("Please enter another number:"))
def addition(n1,n2):
    sum=n1+n2
    return sum
print(f"The sum of those numbers is {addition(first_num, second_num)}")
""" 

#printing a name
first_name,sur_name=str(input("Please provide name:")).split(" ")
print(f"Your name is {first_name} {sur_name}")

#printing first natural numbers less than or equal to 10 using if/else
user_num=int(input("Please provide a number:"))
def natural_num(any_num):
     for num in range (1,any_num):
         if any_num<=10:
print(f"{any_num}")
natural_num(user_num)
        
