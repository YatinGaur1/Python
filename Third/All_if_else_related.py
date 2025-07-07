#nested if else
height=int(input("enter your height"))

if height>=3:
    print("can ride")
    age=int(input("what is your age"))
    if age<=18:
        print("Please pay 250Rs")

    else:
        print("Please pay 500Rs")
else:
    print("Can't ride")
print("bye")
#
bill=0
if(height>=3):
    print("can't ride")
    age=int(input("What is your age? "))
    if age<12:
        bill=150
        print("Ticket price is 150Rs.")

    elif age<=18:
        bill=250
        print("Ticket price is 250 Rs.")
    else:
        bill=500
        print("Ticket price is 500Rs")

print("bye")
#true love calculator
name1=input("What is your name?")
name2=input("Waht is his/her name?")
combine_string=name1+name2
lower_case_string=combine_string.lower()


t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true=t+r+u+e

l=lower_case_string.count("t")
o=lower_case_string.count('e')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=t+o+v+e

love_score=int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"your score is {love_score} and you go together like coke and mantos ")
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score}and you are alright together")
else:
    print(f"your love score is {love_score}")


#check year is leap year or not
year=int(input("Enter the year"))
if(year%4==0):
    if(year%100==0):
       if(year%400==0):
           print("year is leap year")
       else:
           print("not leap year")
    else:
       print("year is leap year ")
else:
    print("year is not leap year")