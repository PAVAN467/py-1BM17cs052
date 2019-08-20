def reverse_words () :
	test_str=text.split(" ")
	test_str.reverse()
	print(" ".join(test_str))

def reverse_letters() :
	test_str = text.split(" ")
	for i in test_str:
		print(i[::-1],end=" ")


text=input("enter the test : ")
print()
print("reversed word in terms of position : ",end=" ")
reverse_words()
print()
print("reversed letters of every words in its position : ",end=" ")
reverse_letters()
print()
