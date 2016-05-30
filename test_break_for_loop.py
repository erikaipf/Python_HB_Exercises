# for j in ["1","2","5","3","4"]:
# 	# Validate the sequence number
# 	if int(j) != 5:
# 		print j
# 	else:
# 		print "Invalid number (%s) on the sequence!\nGAME OVER!" % (j)
# 		# Exit of the loop
# 		break

# print "out of loop"

v_user_sequence = "1 2  3 4 3 2 2234 "
list_seq = [int(i) for i in v_user_sequence.split()] 

#v_user_sequence.split()

print list_seq