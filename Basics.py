print("Hello MindCoders!")


# object - mynamevariableobj
# class
# variable
#myNameVariable - Camel Casin
# my_Name_Variable - snake Casin


age = 4
print(age)

age = "four"
print(age)

name = "kapil"
profession ="Coder"
experience ="no"
print("Hello, I am", name, " I am a ", profession," professionally. And I have ", experience," experience")

x = b"Hello"
a = 10
b = 20.6
c = False
d = None
e = [1, 2, 3, 4, "write"]
f = (1, 2, "puma" , 4,5)
g = range(1, 2, 3)
h = {"name": "kapil" , "age": 20}
i = {1,2,3,4,5}
j = bytearray(10)
k = memoryview(bytes(25))
l = 2 + 3j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))

print(5 >> 2)

print(x:=3)

print(x == 1)
print(x == 2)

print(x != 1)
print(x != 2)

x = 4
print(x < 5 or x < 10)
print(x > 5 or x > 10)
print(x > 3 or x > 10)
print(not(x > 3 or x > 10))

x = 20
y = 20
print (x is y)

x = ["Maruti", "BMW"]
y = ["Maruti" , "BMW"]

z = x
print(x is y)
print(y is z)
print(x is z)

print(x is not y)
print(y is not z)
print(x is not z)

name = input("Please enter your name: ")
print("Hello", name)

x = input("Enter first value for sum: ")
y = input("Enter secand value for sum: ")
z = x + y
print("sum: ", z)

z = int(x) + int(y)
print("sum: ",z)