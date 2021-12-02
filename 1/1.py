file = open("data.txt", "r")
a = 0
prev = 173
for x in file:
	if x > prev:
		a = a+1
	prev = x
print(a)	