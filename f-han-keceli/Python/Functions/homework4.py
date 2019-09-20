#Question 1:

"""
def perfect(number):
    
    summation = 0
    
    for i in range(1,number):
        
        if (number % i == 0):
            summation += i
            
    return summation == number


for i in range(1,1001):
    if (perfect(i)):
        print("Perfect Number:",i)
"""





#Question 2:

"""
def find_GCD(num1,num2):
    
    i = 1
    gcd = 1
    
    while(i <= num1 and i <= num2):
        
        if(not (num1 % i) and not (num2 % i)):
            gcd = i
        i += 1
    return gcd
num1 = int(input("First number:"))
num2 = int(input("Second number:"))

print("Greatest common divisor:",find_GCD(num1,num2))
"""





#Question 3:

"""
def find_LCM(num1,num2):
    
    i = 2
    lcm = 1
    
    while True:
        if(num1 % i == 0 and num2 % i == 0):
            lcm *= i
            
            num1 //= i
            num2 //= i
        
        elif(num1 % i == 0 and num2 % i != 0):
            lcm *= i
            
            num1 //= i
        elif(num1 % i != 0 and num2 % i == 0):
            lcm *= i 
            
            num2 //= i
        else:
            i+=1
        if(num1 == 1 and num2 == 1 ):
            break
        return lcm;
num1 = int(input("First number:"))
num2 = int(input("Second number:"))

print("Least common multiple:",find_LCM(num1,num2))
"""





#Question 4:

"""
unit_digits = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
tens_digits = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Ninety"]

def reading(number):
    
    first = number % 10
    second = number // 10
    
    return tens_digits[second] + " " + unit_digits[first]


number = int(input("Number:"))
print(reading(number)) 
"""

#Question 5:






def find_pythagorean():
    
    pythagorean_list = list()
    for i in range(1,101):
        for j in range(1,101):
            
            c = (i ** 2 + j ** 2) * 0.5
            
            if(c == int(c)):
                pythagorean_list.append((i,j,int(c)))
    return pythagorean_list

for i in find_pythagorean():
    print(i)
