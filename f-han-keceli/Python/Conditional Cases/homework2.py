#Question1
"""

print("Body Mass Index: Weight / Height(m) ** Height(m)")

weight = float(input("Input your weight: "))
height = float(input("Input your height(m): "))

bmi = weight / (height ** height)

if( bmi < 18.5 ):
    print("Slim")
elif(bmi >= 18.5 and bmi < 25):
    print("Normal")
elif(bmi >= 25 and bmi < 30):
    print("Overweight")
else:
    print("Obese")
"""

#Question2
'''

print("Please input 3 number:")

a = float(input("First number:"))
b = float(input("Second number:"))
c = float(input("Third number:"))

if(a >= b and a >= c):
    print("{} is the highest number ".format(a))
elif(b >= a and b >= c):
    print("{} is the highest number".format(b))
else:
    print("{} is the highest number".format(c))
'''

#Question3
'''

mid1 = float(input("Input first midterm grade:"))
mid2 = float(input("Input second midterm grade:"))
final = float(input("Input final grade:"))

grade = (mid1 * 0.3) + (mid2 * 0.3) + (final * 0.4)

if(grade >= 90):
    print("AA")
elif(grade >= 85):
    print("BA")
elif(grade >= 80):
    print("BB")
elif(grade >= 75):
    print("CB")
elif(grade >= 70):
    print("CC")
elif(grade >= 65):
    print("DC")
elif(grade >= 60):
    print("DD")
elif(grade >= 55):
    print("FD")
else:
    print("FF")
'''

#Question4
'''

figure = input("Which geometrical figure want to know?")

if(figure == "Quadrilateral"):
    print("Please input edges by respectively.")
    a = int(input("Edge-1:"))
    b = int(input("Edge-2:"))
    c = int(input("Edge-3:"))
    d = int(input("Edge-4:"))
    
    if(a == b and a == c and a == d):
        print("Square")
    elif(a == c and b == d):
        print("Rectangle")
    else:
        print("Quadrilateral")
        
elif(figure == "Triangle"):
    a = int(input("Edge-1:"))
    b = int(input("Edge-2:"))
    c = int(input("Edge-3:"))
    if(abs(a+b) > c and abs(a+c) > b and abs(b+c)):
        if (a == b and a == c):
            print("Equilateral triangle")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Isoscles triangle")
        else:
            print("Scalena triangle")
    else:
        print("Undefined triangle")
else:
    print("Invalid figure")
'''