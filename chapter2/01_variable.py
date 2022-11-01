#are the various others ways of writing string

a = "Vinit"
v = 'Vinit'
u = '''Vinit is
a android developer
'''# in this way you can print multiple lines
b = 43
c = 56.67
g = True #boolean value
y=None #none value

#printing the variables
print(a,b,c,v,u)
print(g)
print(y)

#printing the types of variables
print(type(a))
print(type(b))
print(type(c))
print(type(g))
print(type(y))
print(type(v))
print(type(u))

#assignment operator
a = 12
a += 2
print(a)
a-=3
print(a)
a*=2
print(a)
a/=2
print(a)
print(type(a))

#comparison operator
b = (4>7)
# b=(14>=7)
# b=(14<7)
# b=(14==7)
print(b)

#logical operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 or bool2 is",(bool1 or  bool2))
print("The value of not bool1 is",(not bool1))

#type casting :- is way to convert one data type into another
a = "10" # iska data type string hai integer nahi
print(type(a))
a = int(a) #ab isne 10 jo string tha usko integer me convert kiya hai
print(a + 5)#ab ye 10+5 ka value print kar dega agar tu bina type casting k add karne ko try karta tho error throw karta
print(type(a)) 

