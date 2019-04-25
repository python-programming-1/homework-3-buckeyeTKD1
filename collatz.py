def p(n):
	if int(n) % 2 == 0:
		return n/2
	if int(n) % 2 == 1:
		return n*3+1
n= int(input ("choose a number to start with"))
while (n != 1):
        n=p(n)
        print (n)
else: 
        print("1")

