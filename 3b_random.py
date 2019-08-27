from Random import randint
import string

str1=string.printable

for i in range(6) :
	print("the random password is : ",str1[randint(0,100)])
