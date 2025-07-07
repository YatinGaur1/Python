height=int(input("Enter the height of your"))
if(height>3):
    print("you have token required")#here indentation very very important
    print("you are ready to watched movie")#here indentation very very important
else:
    print("you not allow to give token")#here indentation very very important

#check whether number is odd or even
number=int(input("Enter the value of number "))
if (number%2==0):
    print("Number is even")
else:
    print("number is odd")

#greatest of 3 numbers
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))

if(num1>=num2 and num1>=num3):
    print("First number is greater :",num1)
elif(num2>=num3):
    print("second number is greater :",num2)
else:
    print("third number is greater :",num3)

#greatest number from four input
num4=int(input("enter the first number :"))
num5=int(input("enter the second number :"))
num6=int(input("enter the third number :"))
num7=int(input("enter the fourth number :"))

if(num4>=num5 and num5>=num6 and num5>=num7):
    print("first number is greater :", num5)
elif(num5>=num6 and num5>=num7):
    print("second number is greater :", num6)
elif(num6>=num7):
    print("third number is greater :", num7)
else:
    print("fourth number is greater :",num7)

