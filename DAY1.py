##Write a Python program to print "Hello, World!"
print("hello world")
##Write a program to swap the values of two variables.
a=10
b=5
a,b=b,a
print(a,b)
##Calculate the area of a circle given its radius.
radius= float(input("enter the radius"))
area=float(3.14*radius**2)
print(f"the area of circle is:", area)
##Write a program to demonstrate basic data type in python. 
a=10
b="bhavay"
c=0.21
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
##	Check whether a number is even or odd
a=int(input("enter the number"))
if a%2==0:
    print("number is even")
else:
    print("number is odd")
## Check whether an entered year is leap year or not.
a=int(input("enter the year "))
    if a%400==0:
        print("its a leap year")
    else:
        print("its not leap year")  
##Write a program to check whether a character is vowel or consonants.
alp=input("enter the alphabet")  
if alp==('a','e','i','o','u'):
    print("its a vowel")
else:
    print("its a consonant")
##	Write a program to find the smallest of two numbers.
    a=int(input("enter the no."))
    b=int(input("enter the no."))
    min_num= min(a,b)
    print("min_num")




    
     



    


