# this is prison mike.
"""
the worst thing about prison
was the dementors
"""
print("dont drop the soap")


def dial(phone_num):
    print(f"{phone_num} \n calling ... ")

def openDialer(num_length, user_provided_num):
    if num_length > 10 and type (user_provided_num)==str:
        print("number invalid")
    elif num_length < 10 and type (user_provided_num)==int:
        print("call ended")
    elif num_length==10 and type (user_provided_num)==int:
        dial(int(user_provided_num))
    else:
        return
user_provided_num=int(input("Please provide number"))
openDialer (user_provided_num)
print (f"calling {user_provided_num}")



