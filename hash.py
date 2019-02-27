alpha = 'ABCDEF'

def truncate(l, key):
	while True:
		try:
			for x in range(key):
				l[x] = str(int(l[x]) ^ int(l[key]))
				# if len(l[x])==2: l[x] = str(int(l[x][0]) ^ int(l[x][1]))
				del l[key]

		except IndexError:
			for x in range(len(l)):
				if int(l[x]) >= 10: l[x] = alpha[int(l[x])-10]
			break;
	return l

def convert_hex_char_to_int(s):
	if s == 'a':s ='10'
	if s == 'b':s ='11'
	if s == 'c':s ='12'
	if s == 'd':s ='13'
	if s == 'e':s ='14'
	if s == 'f':s ='15'
	return s

def fill(s,n):
	l = list(s)
	while len(l)<n+2:
		l.insert(2,'0')
	return ''.join(l) 

def strip(s):
	l = list(s)
	while True:
		if(l[2]=='0'): del l[2]
		elif(l[2]=='1'): break
	return ''.join(l) 

def product(l):
	r = 1
	for x in l:
		r *= x
	return r

def no_head(l):
	return [x[2:] for x in l]


def shuffle(s,n):
	r = ''
	x = 0
	while len(r)<len(s):
		r += s[x::n]
		x += 1
	return r

def hash(s):

	#INTEGER
	integer = [ord(x) for x in s]
	reverse_binary_integer = [int(strip('0b' + bin(x)[::-1][:-2]),2) for x in integer]
	integer_position_weighted = [ord(x)*(s.index(x)+3) for x in s]

	#BINARY
	binary = [bin(x) for x in integer]
	no_0b_binary = no_head(binary) #binary strings without the '0b'

	filled_binary = [fill(bin(x),8) for x in integer] #binary strings that are filled to 8 characters
	no_0b_filled_binary = no_head(filled_binary)
	
	reverse_binary = ['0b' + fill(x,8)[::-1][:-2] for x in binary]
	no_0b_reverse_binary = no_head(reverse_binary)

	stripped_reverse_binary = [strip(x) for x in reverse_binary]
	no_0b_stripped_reverse_binary = no_head(stripped_reverse_binary)

	join_integer = ''.join([str(x) for x in integer])
	join_binary = ''.join(no_0b_binary) #all binary digits as one long string
	join_filled_binary = ''.join(no_0b_binary)
	join_reverse_binary = ''.join(no_0b_reverse_binary)
	join_no_0b_filled_binary = ''.join(no_0b_filled_binary)
	join_reverse_binary_integer = ''.join([str(x) for x in reverse_binary_integer])

	concat = no_0b_binary + no_0b_filled_binary + no_0b_reverse_binary + no_0b_stripped_reverse_binary
	concat = ''.join(concat)

	# print('integer: ',integer)
	# print('integer_position_weighted', integer_position_weighted)
	# print('binary: ',binary)
	# print('no_0b_binary: ',no_0b_binary)
	# print('filled_binary: ',filled_binary)
	# print('no_0b_filled_binary: ',no_0b_filled_binary)
	# print('reverse_binary: ',reverse_binary)
	# print('no_0b_reverse_binary: ',no_0b_reverse_binary)
	# print('stripped_reverse_binary: ',stripped_reverse_binary)
	# print('no_0b_stripped_reverse_binary: ', no_0b_stripped_reverse_binary)
	# print('',join_no_0b_filled_binary)	
	# print('',join_reverse_binary)

	#HEXADECIMAL
	hexadecimal = [hex(x) for x in integer]
	no_0x_hexadecimal = no_head(hexadecimal)
	join_hexadecimal = ''.join(hexadecimal)

	reverse = s[::-1] #Consider XORing 's' with its reverse

	#BITWISE OPERATORS: ^ , & , | , << , >> 


	#NON-UNIQUE VALUES
	length = len(s) #binary of length

	num_zeroes = join_binary.count('0')
	num_ones = join_binary.count('1')
	binary_length = len(join_binary)

	integer_sum = sum(integer)
	integer_product = product(integer)


	binary_of_hex = [bin(ord(x)) for x in list(join_hexadecimal)]
	no_0b_binary_of_hex = no_head(binary_of_hex)
	join_no_0b_binary_of_hex = ''.join(no_0b_binary_of_hex)
	concat += bin(num_zeroes)[2:] + bin(num_ones)[2:] + bin(binary_length)[2:] + bin(integer_sum)[2:] + bin(integer_product)[2:] + join_no_0b_binary_of_hex

	# print(concat)

	shuffled_concat = shuffle(concat,length+2)

	# print(shuffled_concat)

	final_string = int(concat) ^ int(shuffled_concat)
	final_binary_string = ''.join([bin(int(x))[2:] for x in list(str(final_string))])
	FINAL_STRING = int(final_binary_string)^int(final_binary_string[::-1])

	# print(final_string)

	hashed_value = ''.join(truncate(list(str(final_string)),8))

	return hashed_value
	# Consider calculating all of the above for the reversed string as well 
	# Consider expanding string to 512 characters and then truncating from there

l = []


all = [chr(x) for x in range(65,91)] + [chr(x) for x in range(100,126)]

for a in all:
	for b in all:
		for c in all:
			# for d in all:
				l.append(hash(a+b+c))

#86400-86415
print(l)
s = set(l)
print(s)

print('Set Length: ' + str(len(s)))
print('List Length: ' + str(len(l)))

if len(s)!=len(l): print('FAILED') 
else: print('PASSED')
