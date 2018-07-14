lis1 =[0]*8
lis2 =[0]*8
x = int(input())
y = int(input())
i = 7
while x>0:
	lis1[i] = x%2
	x=x//2
	i-=1
i = 7
while y>0:
	lis2[i] = y%2
	y=y//2
	i-=1
count = 0
for i in range(0,len(lis1)):
	if(lis1[i]!=lis2[i]):
		count+=1
print(count)