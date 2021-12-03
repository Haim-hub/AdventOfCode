file = open("data.txt", "r")
gamma = ''
epsilon = ''
pop = [0,0,0,0,0,0,0,0,0,0,0,0]


for txt in file:
	x = list(txt)
	for i in range(12):
		if x[i] is '1':
			pop[i] += 1
		else:
			pop[i] -= 1

for p in pop:
	if p > 0:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'	

def tobit(word):
	val = 0
	x = list(word[::-1])
	for i in range (12):
		val += int(x[i])* 2**int(i)
	return val
print(gamma[0])
print(epsilon[0])		

