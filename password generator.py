import random
import string

charvalues=string.ascii_letters+string.punctuation+string.digits
passlength=int(input("Enter Password Length :"))
password=""
for i in range(passlength):
    val=random.choice(charvalues)
    password=password+val

print("Your Password is :",password)