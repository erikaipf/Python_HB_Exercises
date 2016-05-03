# Course Intro to Programming - Hackbright Academy
# Ch. 8 Scope - Activity 1

def calculate_tip(bill_amount,tip_percentage):
	'''Calculate the amount of the Tip by some Percentage of a bill'''
	return ((bill_amount * tip_percentage) / 100)
	
def calculate_total_bill(bill_amount,tip_amount):
	'''Calculate the total bill with Tip'''
	return bill_amount + tip_amount

def split_bill(bill_amount,number_people):
	'''Split the bill per person'''
	return bill_amount / number_people

def main():
	# Ask the user the Bill Amount and save in a variable
	client_bill_amount = float(raw_input("How much is the bill amount?"))
	# Ask the user the Tip Percentage and save in a variable
	client_tip_percentage = float((raw_input("How much do you want to tip(%)?")))
    
    # Calculate the Tip Amount and save in a variable
	tip_amount = calculate_tip(client_bill_amount,client_tip_percentage)
	# Show the value to the User
	print "Tip Amount is %f" % (tip_amount)

	# Calculate the Total of the Bill with Tip and save in a variable
	total_bill = calculate_total_bill(client_bill_amount, tip_amount) 
	# Show the value to the User
	print "Total bill + Tip is %f" % (total_bill)

	# Ask the user a quantity of people to split thle bill and save in a variable
	quantity_split = float((raw_input("How many people would like to split?")))

	# Calculate the bill per person
	total_bill_person = split_bill(total_bill,quantity_split)
	# Show the value to the User
	print "The bill per person is %f" % (total_bill_person)


# If is the main program (not imported in other file)
if __name__ == '__main__':
    # Execute the code to test
	main()