from math import ceil

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

def elements_inversibles(n):
	res = []
	for ni in xrange(n):
		if inverse(ni, n):
			res.append(ni)
	return res

def rabin_miller(p, t):
	res = False
	if 0 < t and t < p-1:
		q = p-1
		k = 0
		while (q & 0b1) != 1:
			q = q/2
			k = k+1
		b = pow(t, q, p)
		if b == 1 or b == (p-1):
			res = True
		else:
			while k > 0 and not res:
				b = pow(b, 2, p)
				if b == (p-1):
					res = True
				k = k-1
	return res

def generer_nombre_premier(n):
	with open('/dev/urandom', 'r') as f:
		a = long((f.read(int(ceil(n/8)))).encode('hex'), 16) | (1 << n-1)
		if (a & 1) == 0:
			a = a + 1
		while not rabin_miller(a, 10):
			a = a + 2
		return a

def generer_cle_RSA(n):
	p = generer_nombre_premier(n)
	q = generer_nombre_premier(n)
	N = p*q
	fi_N = (p-1)*(q-1)
	e = generer_nombre_premier(n) % fi_N
	d = inverse(e, fi_N)
	return (p, q, N, e, d)
	
def signature_RSA_CRT(m,K):
	(p, q, N, e, d) = K
	res = False
	if N > m:
		dp = d % (p-1)
		dq = d % (q-1)
		sp = pow(m, dp, p)
		sq = pow(m, dq, q)
		res = theoreme_chinois([sp, sq], [p, q])
	return res

def signature_RSA_CRT_faute(m, K):
	(p, q, N, e, d) = K
	res = False
	if N > m:
		dp = d % (p-1)
		dq = d % (q-1)
		sp = pow(m, dp, p)
		sq = pow(m, dq, q) + 1
		res = theoreme_chinois([sp, sq], [p, q])
	return res

if __name__ == "__main__":
	K = generer_cle_RSA(1024)
	print signature_RSA_CRT(42, K)
