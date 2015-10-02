def pgcd(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a

def bezout(a, b):
	(u0, u1) = (1, 0)
	(v0, v1) = (0, 1)
	while b != 0:
		r = a % b
		q = (a - r) / b
		(a, b) = (b, r)
		(u0, u1) = (u1, u0 - q*u1)
		(v0, v1) = (v1, v0 - q*v1)
	return (a, u0, v0) if a > 0 else (-a, -u0, -v0)
 
def inverse(a, n):
	res = 0
	if n > 1 and pgcd(a, n) == 1:
		(a, u0, v0) = bezout(a, n)
		res = u0 % n
	# TODO: Afficher un message d'erreur si res == 0	 
	return res
 
def theoreme_chinois(xis, pis):
	N = 1
	total = 0
	for pi in pis:
		N = N * pi
	for (xi, pi) in zip(xis, pis):
		Ni = N / pi
		(_, ui, _) = bezout(Ni, pi)
		total = total + ui*Ni*xi
	return total % N

if __name__ == '__main__':
	print theoreme_chinois([3, 4, 5], [17, 11, 6])