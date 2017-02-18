# find n(> 9), which is palindrome in base10, base2 and base8.

# 2017/2/18(Sat)

def convert_base2(number):
	if number <= 0:
		raise ValueError
	n = number
	result = ""
	while n >= 2:
		result = str(n % 2) + result
		n = n // 2
	return str(n) + result

def convert_base8(number):
	if number <= 0:
		raise ValueError
	n = number
	result = ""
	while n >= 8:
		result = str(n % 8) + result
		n = n // 8
	return str(n) + result

def palindrome_check(string):
	return string == string[::-1]

def palindronumber_1():
	n = 10
	while True:
		if palindrome_check(str(n)) and palindrome_check(convert_base2(n)) and palindrome_check(convert_base8(n)):
			return n
		n += 1

print(palindronumber_1())







