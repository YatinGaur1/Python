a=5
b=5
print(a is b)
print(id(a))
print(id(b))
print(a is not b)
b=6
print(a is b)
print(a is not b)
print(id(a))
print(id(b))
a=6#here memory is created different for a=6 not a=5 changes a=6 because int is immutable data type
print(id(a))