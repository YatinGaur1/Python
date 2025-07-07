str1="This is a string .\n we are creating it in python."
print(str1)

#concatenation 
str2="hello"
str3="world"
final_str=str2+str3
print(final_str)
#length function used in python
print(len(final_str))

# indexing or character accessability
str4="apna_college"
ch=str4[2]
print(ch)

# str4[0]="2" this is not valid;

#positive indexing slicing

str5="hello_world"
print(str5[:len(str5)])
print(str5[:])
print(str5[1:4])

#negative indexing slicing
str6="apple"
print(str6[-5:-3])
print(str6[-1:-2])#not give anything 
print(str6[-1:])#but it give only one 
print(str6[-3:-1])

#string functions 
print()
str7="i am studying python from ApnaCollege"

#enswith function give true if string ends with given argument else give false;
print(str7.endswith("ege"))
print(str7.endswith("app"))

#capitalizes funtion capital 1st character of string create new string
print(str7.capitalize())
print(str7) #but original string will not be change permanently
str7=str7.capitalize()# originally changed str7

#repalce function replace all occurance of old value to new
str7.replace("o","a")
print(str7.replace("o","a"))
print(str7.replace("python","javascript"))
print(str7) #origanlly string does not change


#find function --> search the word in a string if exist return its starting index else given -1 remember negative index only used in slicing not other thing like find functin -1 mean invalid index
str7.find("o") 
print(str7.find("o"))
print(str7.find("javascript"))

#count function -->count all the occurance of subsritng in a given string if not exist given -1
str7.count("o")
print(str7.count("o"))