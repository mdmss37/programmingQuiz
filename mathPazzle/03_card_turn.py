def create_cards_facingdown(n):
	empty_dic = {}
	for i in range(1,n):
		empty_dic[i] = False
	return empty_dic

cards_set = create_cards_facingdown(101)

def card_turn(start):
	current = cards_set
	
	while start < 101:
		#print(start)
		for i in range(start,101,start):
			#print(current[i])
			if current[i] == False:
				current[i] = True
			elif current[i] == True:
				current[i] = False
			#print(current[i])	
		start += 1		
	return current		
turned_card = card_turn(2)

for card in turned_card:
	if turned_card[card] == False:
		print(card)
