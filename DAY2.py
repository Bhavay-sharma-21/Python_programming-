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
## check whether a number is prime or not 
num=int(input("enter the number"))
if num > 1:
    for i in range (2,int(num/2)+1):
         if (num % i)==0:
            print("it is a not a prime number")
            break
    else:
            print("it is a prime number")
            
else:
    print("it is not a prime number")
            
## Make a simple calculator 
def add(x,y):
     return x+y
def subtract(x,y):
     return x-y
def multiply(x,y):
     return x*y
def divide(x,y):
     if y!=0:
          return x/y
     else:
          return"cannot divide by zero"
while True:
     num1=float(input("enter the number"))
     operand=input("enter the operator(+,-,*,/):")
     num2=float(input("enter the number"))
     if operand =="+":
          result= add(num1,num2)
     elif operand=="-":
          result=subtract(num1,num2)
     elif operand=="*":
          result=multiply(num1,num2)
     elif operand=="/":
          result=divide(num1,num2)
     else:
          print("invalid input")
print(f"Result: {result}")
