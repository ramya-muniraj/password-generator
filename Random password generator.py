import random
import string

length=int(input("Enter the length of your password to be generated:"))

characters=string.printable  #concatenates ascii_lettes,digits,punctuations

password=(''.join(random.choice(characters)for i in range(length)))

print("Your password is:",password)
