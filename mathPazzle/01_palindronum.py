def base_two(number):
	base_two = ''
	while number > 0:
		base_two = str(number%2) + base_two
		# print(base_two)
		number = number // 2
		print(number)
	return base_two

def base_eight(number):
	base_eight = ''
	while number > 0:
		base_eight = str(number%8) + base_eight
		# print(base_eight)
		number = number // 8
	return base_eight

def palindro_num(number):
	for ni in range(1,number):
		base_two_number = base_two(ni)
		base_eight_number = base_eight(ni)
		print("base10:{}, base2:{}, base8:{}".format(ni,base_two_number,base_eight_number))
		if (ni >=10) and (str(ni) == str(ni)[::-1]) and (base_two_number == base_two_number[::-1]) and (base_eight_number == base_eight_number[::-1]):
			return ni


print(palindro_num(1000))
