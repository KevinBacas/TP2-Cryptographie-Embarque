from utils import pgcd, bezout

if __name__ == '__main__':
	print "Hello world!"
	print "pgcd(6, 9) should equal 3 :", pgcd(6, 9)
	print "pgcd(3, 1) should equal 1 :", pgcd(3, 1)
	print "bezout(57, 33) should equal (3, -4, 7) :", bezout(57, 33)
	print "bezout(2, -4) should equal (2, -1, -1) :", bezout(2, -4)
