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
 