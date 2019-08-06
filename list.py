list=[]
n_list=[]
a=0
while a!=-1:
    a=int(input("enter the elements and -1 to stop"))
    list.append(a)
list=list[:-1]    
print("entered list is ",list)

for i in range(0,len(list)) :
    if i %2 ==0 :
        n_list.append(list[i])

print("entered list is ",n_list)
    
       