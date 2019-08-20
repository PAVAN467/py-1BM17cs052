or_list=[]
a=input("Enter the element : ")

while a!='s' :
	or_list.append(int(a))
	a=input("Enter the element : ")

print("original_list : ",or_list)

even_list=[]
i=0
for i in range(len(or_list)) :
	if(i%2==0) :
		even_list.append(or_list[i])


print("even_list : ",even_list)
