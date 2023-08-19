import time as t
f="FLAMES"
print(f.center(59, '•'))
print("Enter names without space... ")
a=(input("Enter a boy name :")) 
b=(input("Enter a girl name :")) 
a1=a
b1=b
a. lower()
b. lower()
a=list(a)
b=list(b)
#----------------------------------------------------------------
#this function is used to seperate the two names and count num
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
	c=a+b
	num=len(c)
	return num
n=sep(a, b) 	
#---------------------------------------------------------------
#this part is uaed to caclulate the flames
f=["Friendship","Love","Affection","Marriage","Enemies","Sister"]
temp=n
c=1
while(len(f)!=1):
    for i in range(0, n):
                  if (n>len(f)) and (c==1):
                      temp=n-len(f)
                      if (i==(temp-1)):
                              try:
                                  del f[i]
                                  f=f[i:]+f[:i]
                                  
                              except:
                                  if (temp>len(f)):
                                      temp=temp-len(f)
                                      c+=1
                  else:
                      if (i==temp-1):
                          del f[i]
                          f=f[i:]+f[:i]
                        
t.sleep(1)
print("Calculating..... ")
t. sleep(2)
print("the relationship between ",a1," and ",b1, " is")
print(f[0].center(59,"-")) 
