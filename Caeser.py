class Caeser:
	
	key = 0
	alpha = []

	def __init__(self, key):
		self.key = key 
		self.alpha = [chr(x) for x in range(65,91)]

	def encrypt(self, s):
		encrypted = ""
		for letter in s:
			letter = letter.upper()
			if letter != ' ':
				old_pos = self.alpha.index(letter)
				new_pos = old_pos + self.key
				if new_pos >= 26: new_pos -= 26 
				new_letter = self.alpha[new_pos]
			else:
				new_letter = ' '
			encrypted += new_letter
		return encrypted

	def decrypt(self, s):
		decrypted = ""
		for letter in s:
			if letter != ' ':
				old_pos = self.alpha.index(letter)
				new_pos = old_pos - self.key
				if new_pos < 0: new_pos += 26
				new_letter = self.alpha[new_pos]
			else:
				new_letter = ' '
			decrypted += new_letter
		return decrypted


class Caeser_Hack:

	alpha = []

	def __init__(self):
		self.alpha = [chr(x) for x in range(65,91)]

	def hack(self, s):
		for key in range(26):
			decrypted = ""
			for letter in s:
				if letter != ' ':
					old_pos = self.alpha.index(letter)
					new_pos = old_pos - key
					if new_pos < 0: new_pos += 26
					new_letter = self.alpha[new_pos]
				else:
					new_letter = ' '
				decrypted += new_letter
			print("Key " + str(key) + ": " + decrypted)


	# def find_key(self, caeser):
	# 	for x in range(1,26):
	# 		s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			caeser.encrypt(s)


caeser = Caeser(13)

encrypted = caeser.encrypt("This is my secret message")
decrypted = caeser.decrypt(encrypted)

print(encrypted)
print(decrypted)

caeser_hack = Caeser_Hack()
caeser_hack.hack("GUVF VF ZL FRPERG ZRFFNTR")
# caeser_hack.find_key(caeser)
