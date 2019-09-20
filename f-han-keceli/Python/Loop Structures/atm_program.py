print("""
***********************************
Welcome to ATM

Transactions;

1. Balance Inquiry

2. Deposit

3. Withdraw cash

Press 'Q' for exit..
***********************************
""")

balance = 1000

while True:
    transaction = input("Select Transaction")
    
    if(transaction == "Q"):
        print("Thanks for chosing us.")
        break
    
    elif(transaction == "1"):
        print("Your balance is {}".format(balance))
    
    elif(transaction == "2"):
        amount =  float(input("Input cash amount:"))
        balance += amount
    
    elif(transaction == "3"):
        amount = float(input("Input cash amount:"))
        
        if(balance - amount < 0):
            print("Insufficient Balance..")
            continue
    else:
        print("Invalid transaction")
    

