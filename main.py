from utils import pgcd, bezout, inverse

if __name__ == '__main__':
	print "Hello world!"

	print "pgcd(6, 9) should be equal 3 :", pgcd(6, 9)
	print "pgcd(3, 1) should be equal 1 :", pgcd(3, 1)

	print "bezout(57, 33) should be equal (3, -4, 7) :", bezout(57, 33)
	print "bezout(2, -4) should be equal (2, -1, -1) :", bezout(2, -4)
	
	print "inverse(2,7) should be equal 4 :", inverse(2, 7)
	print "inverse(-2,7) should be equal 3 :", inverse(-2, 7)
	print "inverse(-9,7) should be equal 3 :", inverse(-9, 7)
