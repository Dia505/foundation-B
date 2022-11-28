#loops in python
#range function in python
#print(f"the range from 1 to 10 is: {range(1,10+1)}")

#list object
num_list =[]

week_days_list = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",]

for num in range(1,11):
    print ("the number in range is: --> {num}")
    num_list.append(num)

print(num_list)

counter = 0
for day in week_days_list:
    counter += 1
    print(f"the {counter} day is: -->{day}")

#same program with the help of range function
for position in range(0, len(week_days_list)):
    print(f"the {position} position in day is: -->{week_days_list[position]}")

#enumerate function
for position,day in enumerate(week_days_list):
    print(f"the {position+1} ###### day is: -->{day}")

odd_list = []
even_list=[]
def filter_odd_even(user_provided_num):
    for num in range(1,user_provided_num+1):
        if num % 2 == 0:
           even_list.append(num)
        else:
            odd_list.append(num)

any_num = int(input("please provide any number:"))
filter_odd_even(any_num)

print(f"the odd list is: {[odd_list]}")
print(f"the even list is: {[even_list]}")
    
#ask age from user with filter and check he/she is eligible for vote. The person must be 19 or greater.
age=int(input("please provide age:"))
if age>=19:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#ask a num with user and filter odd and add in odd list.
the_num=int(input("Please provide any number:"))
odd_list=[]
def filter_odd(user_provided_num):
    for num in range(1,user_provided_num+1):
        if num % 2 == 1:
           odd_list.append(num)
filter_odd(the_num)
print(f"the odd numbers are {odd_list}")

"""
def list_creator(any_num):
    for i in range(1, any_num+1):
        if i % 2 == 1:
            odd_list.append(i)
        return odd_list
print(list_creator(any_num))
"""
#printing name 
f_name, s_name = input("please provide name:").split(" ")
print(f"your full name is: {f_name} {s_name}")
