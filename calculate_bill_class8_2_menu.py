# Course Intro to Programming - Hackbright Academy
# Ch. 8 Scope - Activity 2 - Extra code: Menu in loop
# by Erika Freiha 03-May-2016

# Create the variables
client_tip_percentage = 18

def calculate_tip(bill_amount, tip_percentage = 18):
	'''Calculate the amount of the Tip by some Percentage of a bill'''
	# Calculate the Tip Amount
	return ((bill_amount * tip_percentage) / 100)
	
def calculate_total_bill(bill_amount, tip_amount):
	'''Calculate the total bill with Tip'''
	return (bill_amount + tip_amount)

def split_bill(bill_amount, number_people = 1):
	'''Split the bill per person'''
	return (bill_amount / number_people)

def print_totals_bill(bill_amount, tip_percentage, tip_amount, total_bill):
	'''Print the total of the bill and the Tip Amount'''
	# Shows the totals to the User
	print "  Bill Amount       : %f" % (bill_amount)
	print "  Percentage of Tip :",(tip_percentage), "%"
	print "  Total Tip         : %f" % (tip_amount)
	print "  Total Bill        : %f" % (total_bill)

def print_split_bill(quantity_split, total_split):
	'''Print the total of the bill per person'''
	# Shows the total per person to the User
	#print "The bill splitted by %i people is: %f" % (quantity_split, total_split)
	print "  People to split   : %i" % (quantity_split)
	print "  Amount per person : %f" % (total_split)

def main():
	client_bill_amount    = 0
	client_tip_percentage = 18
	client_quantity_split = 1
	tip_amount            = 0
	total_bill            = 0
	total_bill_per_person = 0

	while (True):
		# Show the main menu to the User
		print """
		      "******** Main Menu ********"
		      "|  1 - Define Bill Amount |"
		      "|  2 - Calculate Tip      |"
		      "|  3 - Split the bill     |"
		      "|  4 - Print the totals   |"
		      "|  5 - Exit               |"
		      "***************************"
		      """

		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select one option: "))
		except ValueError:
			menu_option = None
		
		# Verify the user's choice
		if menu_option == 1:
			# Option 1 - Define Bill Amount
			try:
				# Ask the user the Bill Amount and save in a variable
				client_bill_amount = float(raw_input("How much is the bill amount? "))
				
				if client_bill_amount <= 0:
					print "The value needs to be grater than 0 (zero)!  Please try again."
			except ValueError:
				client_bill_amount = 0
				print "The value is not valid!  Please try again."
		elif menu_option == 2:
			# Option 2 - Calculate Tip
			# Verify if the bill amount was entered before
			if client_bill_amount > 0:
				try:
					# Ask the user the Tip Percentage and save in a variable
					client_tip_percentage = float((raw_input("How much is the percentage of the tip? ")))
					
					if client_tip_percentage < 0:
						print "The value can not be negative!  Please try again."
					else:
						# Calculate the Tip Amount and save in a variable
						tip_amount = calculate_tip(client_bill_amount,client_tip_percentage)
						# Calculate the Total of the Bill with Tip and save in a variable
						total_bill = calculate_total_bill(client_bill_amount, tip_amount)

						# Shows the totals to the User
						print_totals_bill(client_bill_amount, client_tip_percentage, tip_amount, total_bill)
				except ValueError:
					print "The value is not valid!  Please try again."
			else:	
				print "Please select first the option 1 - Define Bill Amount"
				# OR You can ask the values
				## Ask the user the Bill Amount and save in a variable
				#client_bill_amount = float(raw_input("How much is the bill amount? "))			
		elif menu_option == 3:
			# Option 3 - Split the bill
			# Verify if the Amount was defined
			if client_bill_amount > 0:
				try:
					# Ask the user a quantity of people to split thle bill and save in a variable
					client_quantity_split = int((raw_input("How many people would you like to split? ")))
					
					if client_quantity_split <= 0:
						print "The quantity need to be grater than 0 (zero)!  Please try again."
					else:
						# Calculate the bill per person
						total_bill_per_person = split_bill(total_bill, client_quantity_split)
						
						# Show the totals to the User
						print_totals_bill(client_bill_amount, client_tip_percentage, tip_amount, total_bill)
						# Show the total per person to the User
						print_split_bill(client_quantity_split, total_bill_per_person)
				except ValueError:
					client_bill_amount = 0
					print "The value is not valid!  Please try again."
			else:
				print "Please select first the option 1 - Define Bill Amount"
				# OR You can ask the values
				## Ask the user the Bill Amount and save in a variable
				#client_bill_amount = float(raw_input("How much is the bill amount?"))
				## Ask the user the Tip Percentage and save in a variable
				#client_tip_percentage = float((raw_input("How much is the percentage of the tip?")))
	            #
	            ## Calculate the Tip Amount and save in a variable
				#tip_amount = calculate_tip(client_bill_amount,client_tip_percentage)
				## Calculate the Total of the Bill with Tip and save in a variable
				#total_bill = calculate_total_bill(client_bill_amount, tip_amount)
		elif  menu_option == 4:
			# Option 4 - Print the totals
			if client_bill_amount <= 0:
				print "Please select first the option 1 - Define Bill Amount"
			else:
				if tip_amount <= 0 and client_tip_percentage > 0:
					# Calculate the Tip Amount and save in a variable
					tip_amount = calculate_tip(client_bill_amount, client_tip_percentage)
					# Calculate the Total of the Bill with Tip and save in a variable
					total_bill = calculate_total_bill(client_bill_amount, tip_amount)
					# Calculate the bill per person
					total_bill_per_person = split_bill(total_bill, client_quantity_split)
							
				# Show the totals to the User
				print_totals_bill(client_bill_amount, client_tip_percentage, tip_amount, total_bill)
				# Show the total per person to the User
				print_split_bill(client_quantity_split, total_bill_per_person)
		elif menu_option == 5:
			# Option 5 - Exit
			# Go out from the while loop
			break
		else:
			print "Invalid Option!  Please try again."
	# Show final message
	print "\nThank you for use Bill Calculator!"

# If is the main program (not imported in other file)
if __name__ == '__main__':
    # Execute the code to test
	main()