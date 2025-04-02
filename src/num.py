import math

def totient(x):
	start = 2
	arr = []
	tested = False
	while start <= x && (tested || start*start < x):
		if x % start == 0:
			tested = True
			arr.append(start)
			while x % start == 0:
				x = int(x/start)
	r = x
	for i in arr:
		r *= (1-1/i)
	return int(r)

			
		

