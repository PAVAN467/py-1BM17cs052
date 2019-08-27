
#program for divisor a number
n=int(input("enter the number : "))
print("The divisor of the number are : ",end="")
print(n,"",end="")
for i in range((n//2),2,-1) :
	if n%i==0 :
		print(i,end=" ")
		
print(str(1),str(0))

