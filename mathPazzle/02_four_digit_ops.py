# Q: you can put operator to each digit of 4 digit number,
# it is ok you do not put operator. but you need to use operator at least once.
# after caculation, the result needs to be same as palindrome of original number.
# please find such number from 1000 to 9999.

# in case 100 ~ 999
# 351 -> 3 * 51 = 153
# 621 -> 6 * 21 = 126
# 886 -> 8 * 86 = 668



# ops = ['+', '-', '*', '/', '']
ops = ["*", ""]

for num in range(1000, 10000):
	num = str(num)
	if num[::-1][0] == "0":
		continue
	for i in range(0, len(ops)):
		for j in range(0, len(ops)):
			for k in range(0, len(ops)):
				arith_num = num[0] + ops[i] + num[1] + ops[j] + num[2] + ops[k] + num[3]
				# need to use at least one op, so len of arith_num > 5
				if len(arith_num) > 5:
					try:
						if str(eval(arith_num)) == num[::-1]:
							print('{},{}'.format(num, arith_num))
					except:
						continue

# Hint:
# if use other than *, correct answer can not be obtained.
# in case use "+" as OP, max number is 999 + 9 = 1008. "-" and "/" also can not be used.
# ops = ['*', '']