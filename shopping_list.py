# Course Intro to Programming - Hackbright Academy
# Ch. 9 List
# by Erika Freiha 05-May-2016

shopping_list = []

#Option 1: local scope variable 
def order_list(list_to_order):
	list_to_order.sort()
	return list_to_order

#Option 2: global scope variable
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

def main():
	menu_option = 0
	client_bill_amount = 0
	client_tip_percentage = 0
	
	while menu_option != 4:
		# Show the main menu to the User
		print ""
		print "****** Shopping List ******"
		print "*-------------------------*"
		print "******** Main Menu ********"
		print "|  1 - Add Item           |"
		print "|  2 - Remove Item        |"
		print "|  3 - Show List          |"
		print "|  4 - Exit               |"
		print "***************************"

		# Save the user's choice in a variable
		menu_option = int(raw_input("Select one option: "))

		if menu_option == 1:
			# Option 1 - Add Item
			new_user_item = str((raw_input("Inform the new item to add in the shopping List: ")))
			
			add_item_global_list(new_user_item)
		elif menu_option == 2:
			# Option2 - Remove Item
			user_item = str((raw_input("Inform the item to remove from the shopping List: ")))
			
			remove_item_global_list(user_item)
		elif menu_option == 3:
			# Option 3 - Show List
			print "\nYour shopping list:"
			for x in shopping_list:
				print " - ", x
		elif menu_option != 4:
			print "Invalid Option."	
	
	# Show final message
	print "Thank you for use Shopping List!"

# If is the main program (not imported in other file)
if __name__ == '__main__':
    # Execute the code to test
	main()