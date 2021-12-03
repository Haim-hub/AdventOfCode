file = open("data.txt", "r")
oxygen = []
carbon = []
file_length = 0

for txt in file:
	x = list(txt)
	file_length += 1
	oxygen.append(x)
	carbon.append(x)
		


def removeOBytes(bitOp, index):
	o = 0
	while o < len(oxygen):
	 	if oxygen[o][index] == bitOp:
			oxygen.pop(o)
		else:		
			o += 1

def removeCBytes(bitOp, index):
	c = 0
	while c < len(carbon):
	 	if carbon[c][index] == bitOp:
			carbon.pop(c)
		else:		
			c += 1


	
	
for i in range(12):
	pop = 0
	for o in oxygen:
		if o[i] is '1':
			pop += 1
		else:
			pop -= 1

	if pop >= 0:
		removeOBytes('0',i)
	else:
		removeOBytes('1',i)

for i in range(12):
	if 1 < len(carbon):
		pop = 0
		for c in carbon:
			if c[i] is '1':
				pop += 1
			else:
				pop -= 1

		if pop >= 0:
			removeCBytes('1',i)
		else:
			removeCBytes('0',i)				


def tobit(word):
	val = 0
	x = list(word[::-1])
	for i in range (12):
		val += int(x[i])* 2**int(i)
	return val

oxygen[0].pop(12)
carbon[0].pop(12)
print(tobit(oxygen[0])*tobit(carbon[0]))
