import json

alpha = list('ABCDEF')

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

def num_ones(s):
	return list(s).count('1')

def num_zeroes(s):
	return list(s).count('0')

def fill(s):
	s = s[2:]
	while len(s)<8:
		s = '0'+s
	return s

def hash(s):

	r = ''
	x = 0
	for x in range(len(s)): r+=s[x::3]

	o = ''.join([fill(bin(ord(x))) for x in r]) #produces the binary representation of the input string
	# print('o: ',o)
	o = fill(bin(len(o))) + fill(bin(num_ones(o))) + o + fill(bin(num_zeroes(o))) + fill(bin(len(o))) 
	# print('o: ',o)
	integers = sum([ord(x)*num_ones(bin(ord(x)))*num_zeroes(bin(ord(x))) for x in s])
	# print('integers: ',integers)

	h = ''.join([hex(x)[2:] for x in integers]) # converts the binary string to its hexadecimal string
	
	# print('h: ',h)

	b = ''.join([fill(bin(ord(x))) for x in h]) # converts each individual character of the hex string into binary form
	# print('b: ',b)
	o = (((len(b)//len(o))+1) * o)[:len(b)]
	# print('o: ',o)
	l = list(str(int(b) ^ int(o))) #performs XOR 
	# print('l: ',l)

	n = len(s)

	if n < 8: l = truncate(l, 8)
	elif 8 <= n < 16: l = truncate(l, 16)
	elif 16 <= n < 32: l = truncate(l, 32)
	elif 32 <= n < 64: l = truncate(l, 64)
	elif 64 <= n < 128: l = truncate(l, 128)

	return ''.join(l)


# with open('data.json') as f:
#     l = json.load(f)
#     print(l)

l = []

print(hash('hello'))

all = [chr(x) for x in range(65,91)] + [chr(x) for x in range(100,126)]

for a in all:
	for b in all:
		for c in all:
			for d in range(3):
				l.append(hash(a+b+c+str(d)))
				# print(hash(a+b+c))

#86400-86415

s = set(l)

print('Set Length: ' + str(len(s)))
print('List Length: ' + str(len(l)))

if len(s)!=len(l): print('FAILED') 
else: print('PASSED')

# print(l, len(l))
	

# def Repeat(x): 
#     _size = len(x) 
#     repeated = [] 
#     for i in range(_size): 
#         k = i + 1
#         for j in range(k, _size): 
#             if x[i] == x[j] and x[i] not in repeated: 
#                 repeated.append(x[i]) 
#     return repeated 

# r = Repeat(l)
# print(r)
# print([l.index(x) for x in r])

# with open('data.json', 'w') as outfile:
#     json.dump(l, outfile)

# Repeated Hashes for n = 8:
# 1342
# 5905