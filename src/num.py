import math

def totient(x):
	if math.is_prime(x):
		return x-1
	start = 2
	arr = []
	while start <= x:
		if x % start == 0:
			arr.append(start)
			while x % start == 0:
				x = int(x/start)
	r = x
	for i in arr:
		r *= (1-1/i)
	return int(r)

			
		

