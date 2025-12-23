# # 1. Write a program to print your name. 
name = "Arpit"
print(name)

# # 2. Write a program for a Single line comment and multi-line comments 

print("Python uses # for both multiline and single line comment")
print("Python uses # for both multiline and single line comment")
print("Python uses # for both multiline and single line comment")
print("Python uses # for both multiline and single line comment")

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 

int = 10
boolean = True
char = "Arpit"# python only has string data type 
float = 4.0
double  = 4.0958584 # python 
print("\n the type is: ",type(int),"\nthe type is",type(boolean),"\nthe type is",type(char),"\nthe type is",type(float),"\nthe type is",type(double))

# # 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables
x = 19
y = 11

def outer():
     x = 10
     y =20 
     print("outer scope",x,y)# local scope

     def inner():
         f = 15
         d = 25
         print("inner scope",x,y,d,f) #local scope
    
     inner()    
     print("Outer Scope: ",x,y)#local scope

 outer()
 print("global scope",x,y)#global scope

