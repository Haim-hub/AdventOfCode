
file = open("data.txt", "r")
horizontal = 0
depth = 0
aim = 0

for txt in file:
	x = list(txt)
	if x[0] is 'f':
		horizontal += int(x[8])
		depth += aim*int(x[8])
	if x[0] is 'd':
		aim += int(x[5])
	if x[0] is 'u':
		aim -= int(x[3])

print(horizontal*depth)
