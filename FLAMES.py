a=list(input("Enter a name :")) 
b=list(input("Enterva name :")) 
def sep(a, b):
	i=j=0
	while (len(a)>i):
		  while (len(b)>j):
		  	  if (a[i]==b[j]):
		  	  	del a[i]
		  	  	del b[j]
		  	  	i=j=0
		  	  else:
		  	  	j+=1
		  j=0
		  i+=1
	print(a, b, sep="\n")
	c=a+b
	num=len(c)
	print ( num) 
sep(a, b)
#
