a=list(input("Enter a name")) 
b=list(input("Enterva name")) 
i=j=0
while (len(a)>i):
  while (len(b)>j):
    if (a[i]==b[j]):
      del a[i]
      del b[j]
      i=j=0
    j+=1
  i+=1
print(a, b, sep="\n")