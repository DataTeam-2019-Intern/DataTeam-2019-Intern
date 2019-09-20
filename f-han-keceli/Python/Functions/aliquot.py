def aliquot(num):
    aliquot_numbers = []
    
    for i in range(2,num):
        if (num % i ==0):
            aliquot_numbers.append(i)
    return aliquot_numbers

while True:
    num = input("Number:")
    if(num == 'q'):
        print("Program has ended")
        break
    else:
        num = int(num)
        print("Aliquot numbers are:",aliquot(num))