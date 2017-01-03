# current_stick_num starts from 1
def cut_stick(stick_length, people_num, current_stick_num):
	# if current_stick_num >= stick_length, stick has been cut to 1 unit each, no more recursion.
	if current_stick_num >= stick_length:
		return 0
	# if current_stick_num < people_num, each stick can be cut to half, current_stick_num * 2
	elif current_stick_num < people_num:
		return 1 + cut_stick(stick_length, people_num, current_stick_num * 2)
	# else, the current_stick_num increase by the people_num	
	else:
		return 1 + cut_stick(stick_length, people_num, current_stick_num + people_num)

print(cut_stick(20, 3, 1))
print(cut_stick(100, 5, 1))
