##Write a program to demonstrate basic data type in python. 
a=10
b="bhavay"
c=0.21
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
##2.	Check whether a number is even or odd
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
##Find the Factorial of a Number
    def factorial(n)
        if n==0 or n==1:
            return 1
        else: 
            return n*factorial(n-1)
## Write a program to print this patterns
##           *
##         *     *
##       *    *     *
##     *   *     *     *  
rows=4
for i in range(1,rows+1):
    spaces=" "*(rows-i)
    stars=" * "*i
    print(spaces+stars)
## 8.	Write a program to print this series
             1 1 2 3 5 8 13 
    a,b =1,1
    number_of_terms=7
    next_term=b
    count = 1
    while count<= number_of_terms:
        print(next_term,end=" ")
        count+=1
        a,b=b,next_term
        next_num=a+b
        print()

    


