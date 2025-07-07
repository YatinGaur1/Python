#swapping of two by temp variable
num1=input("Enter the first number? ")
num2=input("Enter the second number? ")

temp=num1
num1=num2
num2=temp

print("num1= "+num1+""+"\nnum2="+num2)

#swapping of two number by arithimetic operator(+,-)
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("num1= "+str(num1)+"\nnum2= "+str(num2))

#swapping of two using xor(^) operation
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))

num1=num1^num2
num2=num1^num2
num1=num1^num2

print("num1= "+str(num1)+"\nnum2= "+str(num2))

#swapping the two number by arithmetic operator(*,/)
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))

num1=num1*num2
num2=num1//num2
num1=num1//num2

print("num1= "+str(num1)+"\nnum2= "+str(num2))