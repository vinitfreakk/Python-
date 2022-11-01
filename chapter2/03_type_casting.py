#type casting :- is way to convert one data type into another if possible for eg :- you cannot covert "vinit" string into integer.
a = "10" # iska data type string hai integer nahi
print(type(a))
a = int(a) #ab isne 10 jo string tha usko integer me convert kiya hai
print(a + 5)#ab ye 10+5 ka value print kar dega agar tu bina type casting k add karne ko try karta tho error throw karta
print(type(a)) 