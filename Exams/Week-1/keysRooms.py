rooms = [[1,2,3], [0], [0], [0]]
keys = [False]*(len(rooms)+1)
# print(keys)
for i in range(0,(len(rooms)+1)):
	keys[i] = False
ans = True
# for i in range(0,len(rooms)):
# 	print(rooms[i])
# 	for j in range(0,len(rooms[i])):
# 		print(rooms[i][j])
# 		pass
for i in range(0,len(rooms)):
	if i!=0:
		for k in range(1,i+1):
			if keys[k] != True:
				ans = False
				break
	if i>0 and ans == False:
		break
	for j in range(0,len(rooms[i])):
		v = rooms[i][j]
		keys[v] = True
	# print(keys)

print(ans)
