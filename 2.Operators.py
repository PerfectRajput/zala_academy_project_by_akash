
# 1. Write a function for arithmetic operators(+,-,*,/) 
num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
def arithmetic():
    def add():
        result = num1 + num2
        print(result)
    add()
    def sub():
        result = num1 - num2
        print(result)
    sub()
    def mul():
        result = num1 * num2
        print(result)
    mul()
    def div():
        result = num1 / num2
        print(result)
    div()

arithmetic()
             

# 2. Write a method for increment and decrement operators(++, --) 

# python doesn't have ++ and -- operators like other languages so i used loops for increment 
class unary_operators:
    def increment():
        for i in range(num1):
            print("increments of number:",i)
    increment()        
    print("--------------------") 
    def decrement():   
        for i in range(num1,-1,-1):
            print("decrement of numbers",i)
    decrement()

# 3. Write a program to find the two numbers equal or not. 
def equal_or_not():
    if(num1 == num2):
        print("The numbers are eqaul")
    else:
        print("The numbers are not equal")    
equal_or_not()
# 4. Program for relational operators (<,<==, >, >==) 
def relation():
    print(num1<num2)
    print(num1<=num2)
    print(num1>num2)
    print(num1>=num2)
    print(num1 == num2)
    print(num1!=num2)
relation()
# 5. Print the smaller and larger number 

def small_large():
    if num1 < num2:
        print(num1,"is smaller")
    else:
        print(num2,"is smaller")    

    if num1 > num2:
        print(num1,"is greater")  
    else:
        print(num2,"is greater")     
       
small_large()
