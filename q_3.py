# string_name= "navgurukul"
# if "n" in string_name :
#     print("n hai")
# else: 
    # print('n nahi hai')

    # print ("n" in string_name)
    # print (type("n" in string_name))


user = input("enter your password :")
if len(user)>6 or len(user)<=16:
    if 'a' or "z" in user:
        if "$" in user:
            if "2" or "8" in user:
                print("your password is strong :")
            else:
                print("use integer")
        else:
            print("use special character")
    else:
        print("make a stron pass word")
else:
    print("password is too weak")

        
            