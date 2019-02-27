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

def fill(s):
	s = s[2:]
	while len(s)<8:
		s = '0'+s
	return s

def convert(s):
	if s == 'a':s ='10'
	if s == 'b':s ='11'
	if s == 'c':s ='12'
	if s == 'd':s ='13'
	if s == 'e':s ='14'
	if s == 'f':s ='15'

	return s

def hash(s):
	a = 0
	n = len(s)
	# for p in range(len(s)): l+=s[p::3]
	_int = [ord(x)*num_ones(bin(ord(x))) for x in s]
	print(_int)
	_hex = ''.join([hex(x)[2:] for x in _int])
	_list_hex = list(_hex)
	print(_list_hex)
	_num_hex = [convert(x) for x in _list_hex]
	print(_num_hex)
	_filled_long_binary = [fill(bin(ord(x))) for x in _list_hex]
	_shortened_binary = truncate(_filled_long_binary, 64)
	print(l)



	if n < 8: l = truncate(l, 5)
	elif 8 <= n < 16: l = truncate(l, 16)
	elif 16 <= n < 32: l = truncate(l, 32)
	elif 32 <= n < 64: l = truncate(l, 64)
	elif 64 <= n < 128: l = truncate(l, 128)

	return ''.join(l)


hash('hello')

# with open('data.json') as f:
#     l = json.load(f)
#     print(l)

l = []

for x in range(99999): 
	l.append(hash(str(x)))
	# print(hash(str(x)))
	# print(hash(str(x)))

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