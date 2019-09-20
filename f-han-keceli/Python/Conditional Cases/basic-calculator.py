print("""-------------------------------------
      Welcome to Calculator Program!
      Operations;
      
      1.Summation
      
      2.Substraction
      
      3.Multiplication
      
      4.Division
-------------------------------------
""")

a = int(input("First number:"))
b = int(input("Second number:"))

operation = input("Input operations:")

if operation == "1":
    print(" {} and {} sum is {}".format(a,b,a+b))
elif operation == "2":
    print(" {} and {} sum is {}".format(a,b,a-b))
elif operation == "3":
    print(" {} and {} sum is {}".format(a,b,a*b))
elif operation == "4":
    print(" {} and {} sum is {}".format(a,b,a/b))
else:
    print("Invalid input.")    
    