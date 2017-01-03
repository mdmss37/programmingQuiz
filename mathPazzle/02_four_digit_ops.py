ops = ['+', '-', '*', '/', '']

# if use other than *, correct answer can not be obtained.
# ops = ['*', '']

for num in range(1000, 10000):
	num = str(num)
	for i in range(0, len(ops)):
		for j in range(0, len(ops)):
			for k in range(0, len(ops)):
				arith_num = num[0] + ops[i] + num[1] + ops[j] + num[2] + ops[k] + num[3]
				if len(arith_num) > 5:
					try:
						if str(eval(arith_num)) == num[::-1]:
							print('{},{}'.format(num, arith_num))
					except:
						continue		