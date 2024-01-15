## Write a python program to swap two numbers using a third variable
x=int(input("enter the number"))
y=int(input("enter the number"))

temp=x
x=y
y=temp

print (x,y)
## Write a python program to swap two numbers without using third variable
a= 14
b =15
print("before swapping:",a,b)
a=a+b
b=a-b
a=a-b
print("after swapping:",a,b)
##. Write a python program to read two numbers and find the sum of their cubes
a=14
b=10
sum= a**3+b**3
print(sum)
## Write a python program to read three numbers and if any two variables are equal, print that number
a=2
b=3
c=2
if (a==b):
    print(a)
elif (b==c):
    print(b)
elif (c==a):
    print(c)
else:
    print("all the numbers are different")
## Write a python program to read three numbers and find the smallest among them
    a=5
    b=7
    c=10
    smallest=min(a,b,c)
    print(smallest)
## Write a python program to read three numbers and print them in ascending order (without using sort function)
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=int(input("enter the number"))
    minimum=min(a,b,c)
    maximum=max(a,b,c)
    mid_value= (a+b+c)-(minimum+maximum)
    print(minimum,mid_value,maximum