print("""-----------------------------------
Login:
-----------------------------------""")
    
sys_user_name = "Han"
sys_password = "12345"

user_name = input("User Name:")
password = input("Password:")


if (user_name == sys_user_name and sys_password != password):
    print("Password is incorrect...")
    
elif(user_name != sys_user_name and sys_password == password):
    print("User Name is incorrect...")
    
elif(user_name != sys_user_name and sys_password != password):
    print("User name and password is incorrect...")
else:
    print("Login is sucessfully...")






