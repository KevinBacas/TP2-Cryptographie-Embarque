from utils import pgcd, bezout, inverse, theoreme_chinois, elements_inversibles

if __name__ == '__main__':
	print "Hello world!"

	print "pgcd(6, 9) should be equal 3 :", pgcd(6, 9)
	print "pgcd(3, 1) should be equal 1 :", pgcd(3, 1)

	print "bezout(57, 33) should be equal (3, -4, 7) :", bezout(57, 33)
	print "bezout(2, -4) should be equal (2, -1, -1) :", bezout(2, -4)
	
	print "inverse(2,7) should be equal 4 :", inverse(2, 7)
	print "inverse(-2,7) should be equal 3 :", inverse(-2, 7)
	print "inverse(-9,7) should be equal 3 :", inverse(-9, 7)
	
	print "theoreme_chinois([3, 4, 5], [17, 11, 6]) should return 785 :", theoreme_chinois([3, 4, 5], [17, 11, 6])

	print "len(elements_inversibles(60)) should return 16 :",  len(elements_inversibles(60))
