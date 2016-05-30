# Create the dictionary
shopping_lists = {}

def show_all_lists():
	'''Show all keys and values from the list'''
	global shopping_lists

	if len(shopping_lists) < 1:
		print "Your shopping list is empty!"
	else:
		# Loop to show each list
		for name_list in shopping_lists.keys():
			# Show the name of the list
			print "\n" + name_list + ":"
			# Verify if the list has items
			if len(shopping_lists[name_list]) < 1:
				print " No items"
			else:
				# Loop to show the items
				for items_list in shopping_lists[name_list]:
					# Show the items
					print ' - ' + items_list

def verify_list(list_name): #, show_msg = True):
	''' Verify if the name is valid and if the list exist or not
	    1-Exist, 2-No Exist, 3-Error or Invalid name'''
	# Show the items from a specific list
	global shopping_lists

	# Verify if the list name is valid
	if len(list_name) < 1:
		print "Please enter a valid name for the list."
		# return 3-Invalid name
		return 3
	else:
		# Lower the name of the list
		list_name = list_name.lower()

		# Verify if the list name exist
		if list_name in shopping_lists.keys():
			# Return 1-Exist
			return 1
		else:
			#if show_msg:
			#	print "Sorry the list %s doesn't exist!" % (list_name)
			# Return 2-No Exist
			return 2

def show_list(list_name):
	'''Show the items from a specific list'''
	global shopping_lists

	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(list_name)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		# Change the name to lower case
		list_name = list_name.lower()
		# Verify if the list has items
		if len(shopping_lists[list_name]) < 1:
			print "%s doesn't have items." % (list_name)
		else:
			# Print name of the list
			print "\n" + list_name + ":"
			# Loop to print the items
			for item in shopping_lists[list_name]:
				# Print the items from the list
				print " - " + item
	elif list_ok == 2:
		# Return 1-List No Exist
		print "Sorry the list %s doesn't exist!" % (list_name)
	
def add_new_list(new_list):
	'''Add a new list'''
	global shopping_lists

	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(new_list)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		print "List %s already exist!" % (new_list)
		return False
	elif list_ok == 2:
		# Return 1-List No Exist
		# Lower the name of the list
		new_list = new_list.lower()
		# Create the list name
		shopping_lists[new_list] = []
		print "List %s added." % (new_list)
		return True
	else:
		return False

def remove_list(list_name):
 	'''Remove a list'''
 	global shopping_lists

 	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(list_name)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		# Lower the name of the list
		list_name = list_name.lower()
		# Remove the list
		del shopping_lists[list_name]
		print "List %s removed." % (list_name)
	elif list_ok == 2:
		# Return 1-List No Exist
		print "Sorry the list %s doesn't exist!" % (list_name)
	
def add_new_item(list_name, item_name):
	'''Add new item to a list'''
	global shopping_lists

	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(list_name)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		# Lower the name of the list
		list_name = list_name.lower()
		
		# Verify if the item name is valid
		if len(item_name) < 1:
			print "Please enter a valid name for the item."
		else:
			# Lower the name of the item
			item_name = item_name.lower()

			# Verify if the list name exist
			if item_name in shopping_lists[list_name]:
				print "Item %s already in the list." % (item_name)
			else:
				# Add the new item
				shopping_lists[list_name] = shopping_lists[list_name] + [item_name,] 
				# Sort the list
				shopping_lists[list_name].sort()
				print "New item %s added to list %s." % (item_name, list_name)
	elif list_ok == 2:
		# Return 1-List No Exist
		print "Sorry the list %s doesn't exist!" % (list_name)
	
def add_new_items_to_list(list_name):
	'''Process to add how many items the user wants to add to a list'''
	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(list_name)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		# Loop to add more items to the list
		while True:
			user_item = raw_input("\nList " + list_name + "\nEnter the name of the item to add: ")
			# Add new item to the list
			add_new_item(list_name, user_item)
			# Ask the user
			user_add_more = raw_input("\nWould you like to add more items?\nType:  Y  to add more,  N  to go back to Main Menu: ")
			# Verify the user answer
			if user_add_more.lower() != "y":
				# Exit from the loop
				break
	elif list_ok == 2:
		# Return 1-List No Exist
		print "Sorry the list %s doesn't exist!" % (list_name)
	
def remove_item(list_name, item_name):
	'''Remove an item from a list'''
	global shopping_lists

	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(list_name)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		# Lower the name of the list
		list_name = list_name.lower()
		# Print name of the list
		print "\n" + list_name + ":"
		# Loop to print the items
		for item in shopping_lists[list_name]:
			# Print the items from the list
			print " - " + item		
		
		# Verify if the item name is valid
		if len(item_name) < 1:
			print "Please enter a valid name for the item."
		else:
			# Lower the name of the item
			item_name = item_name.lower()

			# Verify if the list name exist
			if item_name in shopping_lists[list_name]:
				# Remove the item
				shopping_lists[list_name].remove(item_name)
				print "Item %s removed from list %s." % (item_name, list_name)
			else:
				print "Item %s doesn't exist in the list %s." % (item_name, list_name)
	elif list_ok == 2:
		# Return 1-List No Exist
		print "Sorry the list %s doesn't exist!" % (list_name)
	
def remove_items_from_list(list_name):
	'''Remove items from the list'''
	# Verify the list name is valid = Return 1-List Exist, 2-List No Exist, 3-Error or Invalid name
	list_ok = verify_list(list_name)
	
	# Verify the return of the function
	if list_ok == 1:
		# Return 1-List Exist
		# Loop to add more items to the list
		while True:
			user_item = raw_input("\nList " + list_name + "\nEnter the name of the item to remove: ")
			# Remove the item to the list
			remove_item(list_name, user_item)
			# Ask the user
			user_remove_more = raw_input("\nWould you like to remove more items?\nType:  Y  to remove more,  N  to go back to Main Menu: ")
			# Verify the user answer
			if user_remove_more.lower() == "n":
				# Exit from the loop
				break
	elif list_ok == 2:
		# Return 1-List No Exist
		print "Sorry the list %s doesn't exist!" % (list_name)
	
def main():
	while True:
		# Show the main menu to the User
		print """
		      "*********** Shopping Lists **********"
		      "*-----------------------------------*"
		      "************* Main Menu *************"
		      "|  1 - Show all lists               |"
		      "|  2 - Show a specific list         |"
		      "|  3 - Add a new list               |"
		      "|  4 - Add an item to a list        |"
		      "|  5 - Remove an item from a list   |"
		      "|  6 - Remove a specific list       |"
		      "|  7 - Exit                         |"
		      "*************************************"
		      """
		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select one option: "))
		except ValueError:
			menu_option = None
		
		# Verify the user options' choice
		if menu_option == 1:
			# Option 1 - Show all lists
			show_all_lists()
		elif menu_option == 2: 
			# Option 2 - Show a specific list 
			user_list = raw_input("Enter the name of the list: ")
			# Search and print the items from the list
			show_list(user_list)
		elif menu_option == 3: 
			# Option 3 - Add a new list
			user_list = raw_input("Enter the name of the new list: ")
			# Add a new list
			if add_new_list(user_list):
				user_item = raw_input("\nWould you like to add items to the list?\nType:  Y  to add items,  N  to go back to Main Menu: ")
				if user_item.lower() == 'y':
					# Add a new list
					add_new_items_to_list(user_list)
		elif menu_option == 4: 
			# Option 4 - Add an item to a list
			user_list = raw_input("Enter the name of the list: ")
			# Add items to the list
			add_new_items_to_list(user_list)
		elif menu_option == 5: 
			# Option 5 - Remove an item from a list
			user_item = raw_input("Enter the name of the list: ")
			# Remove items from the list
			remove_items_from_list(user_item)
		elif menu_option == 6: 
			# Option 6 - Remove a specific list
			user_item = raw_input("Enter the name of the list to remove: ")
			# Remove list
			remove_list(user_item)
		elif menu_option == 7:
			# Option 7 - Exit
			# Print the Shopping list
			show_all_lists()
			# Exit the loop
			break
		else:
			print "Invalid Option! Try again."	
	
	# Show final message
	print "\nThank you for using Shopping Lists!"


if __name__ == '__main__':
	main()