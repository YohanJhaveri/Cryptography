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

def hash(s):

	r = ''
	x = 0
	for x in range(len(s)): r+=s[x::3]

	o = ''.join([bin(ord(x))[2:] for x in r]) #produces the binary representation of the input string
	h = ''.join([hex(ord(x))[2:] for x in o]) # converts the binary string to its hexadecimal string
	b = ''.join([bin(ord(x))[2:] for x in h]) # converts each individual character of the hex string into binary form
	o = (((len(b)//len(o))+1) * o)[:len(b)]
	l = list(str(int(b) ^ int(o))) #performs XOR 

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


all = [chr(x) for x in range(65,91)] + [chr(x) for x in range(100,126)]


for a in all:
	for b in all:
		for c in all:
			# for d in all:
				l.append(hash(a+b+c))
				# print(hash(str(x)))

# for x in range(99999):
# 	l.append(hash(str(x)))

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