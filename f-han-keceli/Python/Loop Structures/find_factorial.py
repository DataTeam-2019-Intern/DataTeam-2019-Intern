print("""
***********************************
Program for finding fact of number

Press 'Q' for exit..
***********************************
""")

while True:
    number = input("Number:")
    if(number == "Q"):
        print("End of program.")
        break
    
    else:
        number = int(number)
        factorial = 1
        
        for i in range(2,number+1):
            print("Factorial",factorial,"i:",i)
            factorial *= i
    print("Factorial",factorial)
    
    