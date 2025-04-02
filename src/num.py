import math

def totient(x):
	debut = 2
	tab = []
	test = False
	while debut <= x and (test or debut*debut < x):
		if x % debut == 0:
			test = True
			tab.append(debut)
			while x % debut == 0:
				x = int(x/debut)
	r = x
	for i in tab:
		r *= (1-1/i)
	return int(r)

			
		

