#Question1:

"""
num = int(input("Input an integer:"))

count = 1 
perfectnum = 0

while True:
    if  num % count == 0:
        perfectnum+=count
        
    count+=1
    if count >= num:
        break
if num == perfectnum:
    print(num,"is a perfect number.")
else:
    print(num,"isn't a perfect number.")
"""

#Question2:

"""    
num = int(input("Input an integer:"))
digitCount = 0
sum = 0
numberplace = 0
temp1 = num

while(temp1>0):
    temp1 //= 10
    digitCount+=1
    
temp2 = num

while(temp2 > 0):
    numberplace = temp2 % 10
    sum += numberplace ** digitCount
    temp2 //= 10
    
if(sum == num):
    print(num,"is an armstrong number.")
else:
    print(num,"isn't an armstrong number.")
"""

#Question3:

"""
count=1
for i in range(1,11):
    print("***************************",count,"***************************" )
    count+=1
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
"""

#Question4:

"""
sum = 0

while True:
    num = input("Input an integer:")
    print("Press Q for exit..")
 
    if(num == "q" or num == "Q"):
        break
    num = int(num)
   
    sum+=num
print("Inputted numbers summation are",sum)
"""

#Question5:

"""
for i in range(1,101):
    if(i%3 != 0):
        continue
    print(i)
"""

#Question6

"""
First Solution:
array = []
for i in range(1,101):
    if(i % 2 == 0):
        array.append(i)
print(i)
"""


"""
Second Solution by List Comprehension:
array = [i for i in range(1,101) if i % 2 == 0 ]
print(array)
"""