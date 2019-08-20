test_list=[]
def search_element(test_list,key) :
	present=False
	if key in test_list :
		present=True
	return present

a=input("Enter the element : ")
while a!='s' :
	test_list.append(int(a))
	a=input("Enter the element : ")

print("test_list : ",test_list)

key= int(input("enter the element to search : "))
print(search_element(test_list,key))
