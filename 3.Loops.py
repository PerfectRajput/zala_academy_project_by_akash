# 1. Write a program to print  “Bright IT Career”  ten times using for loop 
for i in range(10):

 print ("Bright IT Career")

# 2. Write a java program to print 1 to 20 numbers using the while loop. 

i = 1
while i <= 20:
  print(i)
  i += 1

# 3. Program to equal operator and not equal operators 

num1 = int(input("Enter the 1nd number: "))
num2 = int(input("Enter the 2nd number: "))
print(num1 == num2)
print(num1!= num2)

# 4. Write a program to print the odd and even numbers. 

def odd_even(numbers):
  for i in numbers:
    if i % 2 == 0: 
        print("The Number",i,"is even: ")
    else:
        print("The Number",i,"is odd: ")      
try:        
    nums = list(map(int,input("Enter numbers by spaces: ").split()))
    odd_even(nums) 
except:
   print("Please Enter integers i.e. numbers")


# 5. Write a program to print largest number among three numbers. 

num3 = int(input("Enter the 3rd number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("Largest number is: ",largest)  


# 6. Write a  program to print even number between 10 and 20 using while 

a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()

# 7. Write a program to print 1 to 10 using the do-while loop statement. 

a = 1
while True:
    print(a)
    a = a + 1
    if(a > 10):
        break 
print()

# 8. Write a program to find Armstrong number or not 

sum = 0
temp = 0
temp = num1
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if num1 == sum:
    print(num1," is an amstrong number")
else:
    print(num1," is not an amstrong number")

# 9. Write a program to find the prime or not. 

num = int(input("Enter a number: "))
if(num > 1):
    for i in range(2,num):
        if num % i == 0:
            print(" not a Prime Number: ",num)
            break
    else:
        print("Prime number: ",num)
else:
    print("Not a Prime Number: ",num)

# 10. Write a program to palindrome or not. 

temp = num1
rev = 0
while(num1 > 0):
    dig = num1 % 10
    rev = rev * 10 + dig
    num1 = num1 // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 

# 11. Program to check whether a number is EVEN or ODD using switch 

if num1 % 2 == 0:
    print("{0} is Even ".format(num1))
else:
    print("{0} is Odd ".format(num1))  

# 12. Print gender (Male/Female) program according to given M/F using switch

Gender = input("Enter M or F: ").upper()

switch = {
    "M": "Male",
    "F": "Female"
}

print(switch.get(Gender, "Invalid input"))
