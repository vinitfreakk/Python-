l1 = [55,45,96,36,54,555]
print(l1)
print("sorting is taking place of the above list")
l1.sort()
print(l1)
print("The above list is getting reversed")
l1.reverse()
print(l1)
print("The list gets appended meaning we can add new value at the end of the list")
l1.append("vinit")
l1.append(56)
print(l1)
print("In the above list at particular index we are going to add the other element")
l1.insert(2,677)
print(l1)
print("From the above list By using pop function lets remove value at index 2")
l1.pop(2)
print(l1)
print("from the above list By using remove function lets remove the value 56 without using index")
l1.remove(56)
print(l1)