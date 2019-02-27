class Transposition:
	
	key = 0

	def __init__(self, key):
		self.key = key 

	def encrypt(self, s):
	
		l = [[]]

		encrypted = ""

		for i in range((len(s)//self.key)):
			l.append([])

		for x in range(len(s)):
			l[x//self.key].append(s[x])

		for a in range(self.key):
			for b in range(len(l)):
				try:
					encrypted += l[b][a]
				except IndexError:
					encrypted += ' '
		print(l)
		return encrypted


	def decrypt(self, s):

		l = []

		decrypted = ""

		y = len(s)//self.key

		for i in range(y):
			l.append([])

		for x in range(len(s)):
			l[x%y].append(s[x])

		for a in l:
			for b in a:
				try:
					decrypted += b
				except IndexError:
					decrypted += ' '
		print(l)
		return decrypted

transposition = Transposition(2)
encrypt = transposition.encrypt("WHO DO YOU THINK YOU ARE!")
decrypt = transposition.decrypt(encrypt)

print(encrypt)
print(decrypt)