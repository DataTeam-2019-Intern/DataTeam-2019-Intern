print("""
**********************************
User Login System
**********************************
      """)

sys_username = "Han"
sys_password = "12345"

login_train = 3

while True:
    username = input("Username:")
    password = input("Password:")
    if(username != sys_username and password == sys_password):
        print("Wrong username..")
        login_train-= 1
    elif(username == sys_username and password != sys_password):
        print("Wrong password..")
        login_train-= 1
    elif(username != sys_username and password != sys_password):
        print("Username and passwrod wrong")
        login_train-= 1
    else:
        print("Login is successfull")
        break
    if(login_train == 0 ):
        print("Try again later")
        break
    