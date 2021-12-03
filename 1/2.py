file = open("data.txt", "r")
a=173
b=179
c=200
d=b
e=c

increase = 0

for x in file:
	f = x
	g = int(d)+int(e)+int(f)
	h = int(a)+int(b)+int(c)
	if  h < g:
		increase += 1
	a=b
	b=c
	d=c
	c=f
	e=f

print(increase)