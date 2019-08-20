n=int(input("enter the number : "))
factors=[n,n//2]
i=n//2
while i!=1 :
	i-=1
	if n%i==0 :
		factors.append(i)

print(factors)
