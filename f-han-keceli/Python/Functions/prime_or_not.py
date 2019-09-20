def prime(num):
    if(num == 1):
        return False
    
    elif(num == 2):
        return True
    else:
        for i in range(2,num):
            if (num % i == 0):
                return False
            return True

while True:
    num = input("Input a number:")
    
    if (num == 'q'):
        break
    else:
        num = int(num)
        
        if(prime(num)):
            print(num,"is a prime number.")
        else:
            print(num,"isn't a prime number.")
    