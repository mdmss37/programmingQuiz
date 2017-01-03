import itertools

# simple solution with for loop
# def exchange(money, coins):
# 	coin_tup = coins
# 	count = 0
# 	for i in range(0,int((money/coin_tup[0]))+1):
# 		for j in range(0,int((money/coin_tup[1]))+1):
# 			for k in range(0,int((money/coin_tup[2]))+1):
# 				for m in range(0,int((money/coin_tup[3]))+1):
# 					if (coin_tup[0] * i + coin_tup[1] * j + coin_tup[2] * k + coin_tup[3] * m == money) and (i + j + k + m) <= 15:
# 						print(coin_tup[0],i,coin_tup[1],j,coin_tup[2],k,coin_tup[3],m)
# 						count += 1
# 	return count

# the solution easy to expand, but take too much time to complete
def exchange(money, coins):
	coin_list = list(coins)
	count = 0
	for i in range(2,16):
		# itertools.combinations_with_replacement --> Overlapping combination(重複組み合わせ)
		for tup in list(itertools.combinations_with_replacement(coins, i)):
			if sum(tup) == money:
				count += 1
	return count
 
print(exchange(1000,(500,100,50,10)))
