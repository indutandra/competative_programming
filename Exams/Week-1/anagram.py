
s=str(input())
t=str(input())
s= s.lower()
t= t.lower()
dict1 = {}
dict2 = {}
n1 = len(s)
n2 = len(t)
k = True

for i in range(0,n1):
	if s[i]==" ":
		continue
	if s[i] in dict1:
		dict1[s[i]]+=1
	else:
		dict1[s[i]]=1
for j in range(0,n2):
	if t[j]== " ":
		continue
	if t[j] in dict2:
		dict2[t[j]]+=1
	else:
		dict2[t[j]]=1
for i in range(0,n1):
	if dict1 != dict2:
		k = False
# if n1!=n2:
# 	k = False
print(k)
