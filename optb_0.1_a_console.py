start = 0
print ("enter count of splitters")
delcount = int(input())
delcountt = delcount
x = 1 - delcountt
y = int(1)
base_spl = [0]*10
signalm = [0]*10
signalab = [0]*10
magpot = [0, 0.32, 0.49, 0.76, 1.06, 1.42, 1.56, 1.93, 2.34, 2.71, 3.17]
abpot = [0, 13.7, 10.08, 8.16, 7.11, 6.29, 5.39, 4.56, 4.01, 3.73, 3.19]

def enter_splitters():
	print ("enter type of", y, "splitter\n"
		"1 - 5/95 \n"
		"2 - 10/90 \n"
		"3 - 15/85 \n"
		"4 - 20/80 \n"
		"5 - 25/85 \n"
		"6 - 30/70 \n"
		"7 - 35/65 \n"
		"8 - 40/60 \n"
		"9 - 45/55 \n"
	    "10 - 50/50 \n")
	pass
	
while y < delcount + 1:
	enter_splitters()
	firstspl = int(input())
	base_spl[y-1] = firstspl
	y += 1

signalm[0] = magpot[base_spl[0]]
signalab[0] = abpot[base_spl[0]]
y=0
while y < delcount:
	signalm[y] = round(signalm[y - 1] + magpot[base_spl[y]], 2)
	signalab[y] = round(signalab[y - 1] + abpot[base_spl[y]], 2)
	y += 1
	



print (delcount, x, firstspl, "test ok", base_spl, "\n", signalm, "\n", signalab)
