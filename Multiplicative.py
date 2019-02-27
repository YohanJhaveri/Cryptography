class Multiplicative:

	key = 0
	alpha = []

	def __init__(self, key):
		self.key = key;
		self.alpha = [chr(x) for x in range(65,91)] + [' ']

	def encrypt(self, s):
		encrypted = ''
		for letter in s:
			alpha_code = self.alpha.index(letter.upper())
			transpose = (self.key * alpha_code)%len(self.alpha)
			encrypted += self.alpha[transpose]
		return encrypted


	# def decrypt(): #TODO: Understand the euclidian algorithm for finding reverse modulus



multiplicative = Multiplicative(8)
print(multiplicative.encrypt(" Hello my name is Yohan"))