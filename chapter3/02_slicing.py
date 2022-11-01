#concatenating two strings
print("concatenating two strings")
greeting = "Good Morning,"
name = "Vinit"
c = greeting+name
print(c)

#accesing string Character using indexing
print("accesing string Character using indexing")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

#slicing
print("slicing example")
print(name[0:4])#frist term is including and last term is excluding
print(name[1:4])#frist term is including and last term is excluding
print(name[2:3])#frist term is including and last term is excluding
print(name[0:5])#frist term is including and last term is excluding
print(name[:4])#is same as name[0:4]
print(name[0:])#is same as name[0:5]

#negative indexing and negative slicing
print("negative indexing and negative slicing")
c  = name[-4:-1]#is same as name[1:4]
print(c)

#slicing with skip value
print("slicing with skip value")
name = "vinitisandroiddeveloper"
print(name[0:20:3])#two letters will get skipped while printing



