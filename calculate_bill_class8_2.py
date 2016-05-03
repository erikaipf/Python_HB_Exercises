# Course Intro to Programming - Hackbright Academy
# Ch. 8 Scope - Activity 2

def calculate_tip(bill_amount, tip_percentage):
	'''Calculate the amount of the Tip by some Percentage of a bill'''
	return ((bill_amount * tip_percentage) / 100)
	
def calculate_total_bill(bill_amount, tip_amount):
	'''Calculate the total bill with Tip'''
	return (bill_amount + tip_amount)

def split_bill(bill_amount, number_people):
	'''Split the bill per person'''
	return (bill_amount / number_people)

def print_totals_bill(tip_amount, total_bill):
	'''Print the total of the bill and the Tip Amount'''
	# Shows the totals to the User
	print "Total Tip: %f" % (tip_amount)
	print "Total Bill: %f" % (total_bill)
	print ""

def print_split_bill(total_split):
	'''Print the total of the bill per person'''
	# Shows the total per person to the User
	print "The total per person is: %f" % (total_split)
	print ""

def main():
	# Ask the user the Bill Amount and save in a variable
	client_bill_amount = float(raw_input("How much is the bill amount?"))
	# Ask the user the Tip Percentage and save in a variable
	client_tip_percentage = float((raw_input("How much is the percentage of the tip?")))
	
	# Calculate the Tip Amount and save in a variable
	tip_amount = calculate_tip(client_bill_amount,client_tip_percentage)
	# Calculate the Total of the Bill with Tip and save in a variable
	total_bill = calculate_total_bill(client_bill_amount, tip_amount)

	# Show the main menu to the User
	print ""
	print "Select one option:"
	print "1 - Calculate tip"
	print "2 - Split the bill"
	print ""

	# Save the user's choice in a variable
	user_option = int(raw_input())

	# Verify the user's choice
	if user_option == 1:
		# Option 1 - Calculate Tip
		# Shows the totals to the User
		print_totals_bill(tip_amount, total_bill)
		
		# Show the second menu to the User
		print "Would you like to split the bill?"
		print "Y - Yes"
		print "N - No"
		print ""
		
		# Save the user's choice in a variable
		user_option = str(raw_input())

		# Verify the user's choice
		if user_option == "Y" or user_option == "y":
			# Ask the user a quantity of people to split thle bill and save in a variable
			quantity_split = int((raw_input("How many people would you like to split?")))
			
			# Calculate the bill per person
			total_bill_per_person = split_bill(total_bill, quantity_split)

			# Show the total per person to the User
			print_split_bill(total_bill_per_person)
		elif user_option != "Y" and user_option != "y" and user_option != "N" and user_option != "n":
			print "Sorry! Invalid Choice."
	elif user_option == 2:
		# Option 2 - Split the bill
		# Ask the user a quantity of people to split thle bill and save in a variable
		quantity_split = int((raw_input("How many people would you like to split?")))
		
		# Calculate the bill per person
		total_bill_per_person = split_bill(total_bill, quantity_split)

		# Show the totals to the User
		print_totals_bill(tip_amount, total_bill)
		# Show the total per person to the User
		print_split_bill(total_bill_per_person)


	# Show final message
	print "Thank you for use Bill Calculator!"

# If is the main program (not imported in other file)
if __name__ == '__main__':
    # Execute the code to test
	main()