# Course Intro to Programming - Hackbright Academy
# Ch. 8 Scope - Activity 2 - Extra code: Menu in loop
# by Erika Freiha 03-May-2016

def calculate_tip(bill_amount, tip_percentage = 18):
	'''Calculate the amount of the Tip by some Percentage of a bill'''
	return ((bill_amount * tip_percentage) / 100)
	
def calculate_total_bill(bill_amount, tip_amount):
	'''Calculate the total bill with Tip'''
	return (bill_amount + tip_amount)

def split_bill(bill_amount, number_people = 1):
	'''Split the bill per person'''
	return (bill_amount / number_people)

def print_totals_bill(tip_amount, total_bill):
	'''Print the total of the bill and the Tip Amount'''
	# Shows the totals to the User
	print "Total Tip : %f" % (tip_amount)
	print "Total Bill: %f" % (total_bill)

def print_split_bill(total_split):
	'''Print the total of the bill per person'''
	# Shows the total per person to the User
	print "The total per person is: %f" % (total_split)

def main():
	menu_option = 0
	client_bill_amount = 0
	client_tip_percentage = 0
	
	while menu_option != 4:
		# Show the main menu to the User
		print ""
		print "******** Main Menu ********"
		print "|  1 - Define Bill Amount |"
		print "|  2 - Calculate Tip      |"
		print "|  3 - Split the bill     |"
		print "|  4 - Exit               |"
		print "***************************"

		# Save the user's choice in a variable
		menu_option = int(raw_input("Select one option: "))

		# Verify the user's choice
		if menu_option == 1:
			# Option 1 - Define Bill Amount
			# Ask the user the Bill Amount and save in a variable
			client_bill_amount = float(raw_input("How much is the bill amount? "))
		elif menu_option == 2:
			# Option 2 - Calculate Tip
			if client_bill_amount > 0:
				# Ask the user the Tip Percentage and save in a variable
				client_tip_percentage = float((raw_input("How much is the percentage of the tip? ")))
				
				# Calculate the Tip Amount and save in a variable
				tip_amount = calculate_tip(client_bill_amount,client_tip_percentage)
				# Calculate the Total of the Bill with Tip and save in a variable
				total_bill = calculate_total_bill(client_bill_amount, tip_amount)

				# Shows the totals to the User
				print_totals_bill(tip_amount, total_bill)
			else:	
				print "Please, select first the option 1 - Define Bill Amount"
				# OR You can ask the values
				## Ask the user the Bill Amount and save in a variable
				#client_bill_amount = float(raw_input("How much is the bill amount? "))			
		elif menu_option == 3:
			# Option 3 - Split the bill
			# Verify if the Amount was defined
			if client_bill_amount > 0 and client_tip_percentage > 0:
				# Ask the user a quantity of people to split thle bill and save in a variable
				quantity_split = int((raw_input("How many people would you like to split? ")))
				
				# Calculate the bill per person
				total_bill_per_person = split_bill(total_bill, quantity_split)
				
				# Show the totals to the User
				print_totals_bill(tip_amount, total_bill)
				# Show the total per person to the User
				print_split_bill(total_bill_per_person)
			else:
				if client_bill_amount == 0:
					print "Please, select first the option 1 - Define Bill Amount"
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
				elif client_tip_percentage == 0:
					print "Please, select first the option 2 - Calculate Tip"
					# OR You can ask the values
					## Ask the user the Tip Percentage and save in a variable
					#client_tip_percentage = float((raw_input("How much is the percentage of the tip?")))
		            #
		            ## Calculate the Tip Amount and save in a variable
					#tip_amount = calculate_tip(client_bill_amount,client_tip_percentage)
					## Calculate the Total of the Bill with Tip and save in a variable
					#total_bill = calculate_total_bill(client_bill_amount, tip_amount)
		elif menu_option != 4:
			print "Invalid Option."		
	# Show final message
	print "Thank you for use Bill Calculator!"

# If is the main program (not imported in other file)
if __name__ == '__main__':
    # Execute the code to test
	main()