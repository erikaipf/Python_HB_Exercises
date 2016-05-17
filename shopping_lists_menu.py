# Course Intro to Programming - Hackbright Academy
# Ch. 9 List
# by Erika Freiha 05-May-2016
# Upgrate some functions, While Loop, Error Exception - 06-May-2016

shopping_list = []

def order_global_list():
	global shopping_list
	shopping_list.sort()
	print shopping_list

def add_item_global_list(new_item):
	global shopping_list

	# Convert the value of the new item to lower case
	new_item = new_item.lower()

	# Verify if the new item is already in the list
	if new_item in shopping_list:
		print "Item already in the list."
	else:
		# Add item in the list
		shopping_list.append(new_item)
		# Sort list
		order_global_list()

def remove_item_global_list(value_item):
	global shopping_list
	
	# Convert the value of the new item to lower case
	value_item = value_item.lower()

	# Verify if the item is in the list
	if value_item in shopping_list:
		# Remove the value from the list
		shopping_list.remove(value_item)
		# Sort the list
		shopping_list.sort()
	else:
		print "Item is not in the list."

def print_list(show_empty_msg = True):
	global shopping_list
	
	if len(shopping_list) > 0:
		print "\nYour shopping list:"
		
		for x in shopping_list:
			print " - ", x
	else:
		if show_empty_msg == True:
			print "Your Shopping List is empty."
def main():
	
	while (True):
		# Show the main menu to the User
		print """
		      "****** Shopping List ******"
		      "*-------------------------*"
		      "******** Main Menu ********"
		      "|  1 - Add Item           |"
		      "|  2 - Remove Item        |"
		      "|  3 - Show List          |"
		      "|  4 - Exit               |"
		      "***************************"
		      """
		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select one option: "))
		except ValueError:
			menu_option = None
			
		if menu_option == 1:
			# Option 1 - Add Item
			new_user_item = str((raw_input("Enter the name of the new item to add: ")))
			
			add_item_global_list(new_user_item)
		elif menu_option == 2:
			# Option2 - Remove Item
			user_item = str((raw_input("Enter the name of the item to remove: ")))
			
			remove_item_global_list(user_item)
		elif menu_option == 3:
			# Option 3 - Show List
			print_list()
		elif menu_option == 4:
			# Option 4 - Exit
			# Print the Shopping list
			print_list(False)
			# Exit the loop
			break
		else:
			print "Invalid Option! Try again."	
	
	# Show final message
	print "\nThank you for using Shopping List!"

# If is the main program (not imported in other file)
if __name__ == '__main__':
    # Execute the code to test
	main()