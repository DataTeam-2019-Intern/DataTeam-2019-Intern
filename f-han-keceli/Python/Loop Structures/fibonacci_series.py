a = 1 
b = 1

fibonacci = [a,b]

num = int(input("Input fibonacci range:"))

for i in range(num):
    a,b = b,a+b
    print("a:",a,"b:",b)
    fibonacci.append(b)
    
print(fibonacci)