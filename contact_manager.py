from contact import*

address_book = []

def display_contact_info(first_name, last_name, mobile_phone, work_phone, email, twitter_handle):
	print "\nFirst Name     :", first_name.title()
	print "Last Name      :", last_name.title()
	print "Mobile Phone   :", mobile_phone
	print "Work Phone     :", work_phone
	print "Email          :", email
	print "Twitter Handle :", twitter_handle

def search_contact_name(contact_obj_list, first_name, last_name, return_option = "o"):
	'''Search for a contact by First and Last Name, return the first instance found
	   Return Options:
	        o - return the Object (letter o)
	        i - return Index (letter i)'''
	
	# Loop to search the contact list
	for index in range(len(contact_obj_list)):
		if contact_obj_list[index].first_name == first_name.lower() and contact_obj_list[index].last_name == last_name.lower():
			# Verify the return option
			if return_option.lower() == "o":
				# Return the object for the contact
				return contact_obj_list[index]
			else:
				# Return the index for the contact in the list
				return index
			# Stop the search
			break

def add_contact_to_list(show_message, contact_obj_list, first_name, last_name, mobile_phone = "", work_phone = "", email ="", twitter_handle =""):
	# Instantiate the contact
	new_contact = Contact(first_name.lower(), last_name.lower(), mobile_phone, work_phone, email.lower(), twitter_handle.lower())
	# Add the contact to a list
	contact_obj_list.append(new_contact)
	
	if show_message:
		# Show message to show the contact was created
		print "\nContact %s %s added!" % (first_name, last_name)

def add_new_contact(show_message, contact_obj_list, first_name, last_name, mobile_phone = "", work_phone = "", email ="", twitter_handle =""):
	# Add a new contact to the list
	# Validate the First and Last Name
	if first_name.strip(' ') == "":
		if show_message:
			print "\nThe First Name is blank.  Please try again."
	elif last_name.strip(' ') == "":
		if show_message:
			print "\nThe Last Name is blank.  Please try again."
	else:
		# Search for a contact by First and Last Name (return the Object)
		old_contact = search_contact_name(contact_obj_list, first_name, last_name, "o")
		
		# Verify if some old contact was found
		if old_contact != None:
			# Show the old contact
			old_contact.display_contact()
			# Ask the user's choice
			user_option = raw_input("\nThis First and Last Name combination already exists.\nWould you like to make a second contact with that Name combination?  Type  Y  to create or any other key to cancel: ")
			# Verify the user option
			if user_option.lower() == "y":
				# Instantiate the contact object and Add contact to a list
				add_contact_to_list(show_message, contact_obj_list, first_name, last_name, mobile_phone, work_phone, email, twitter_handle)
		else:
			# Instantiate the contact object and Add contact to a list
			add_contact_to_list(show_message, contact_obj_list, first_name, last_name, mobile_phone, work_phone, email, twitter_handle)

def validate_file_name(file_name):
	if file_name.strip(' ') == "":
		print "\nThe file name cannot be blank.  Please try again."
		return False
	elif " " in file_name:
		print "\nThe file name cannot have blank spaces.  Please try again."
		return False
	elif file_name.count(".") == 0:
		print "\nThe file name has to contain the extension (for example file_name.txt).  Please try again."
		return False
	elif file_name.count(".") > 1:
		print "\nThe file name cannot have more than one extension.  Please try again."
		return False
	else:
		return True

def write_contact_file(show_message, contact_obj_list, contact_file_name = ""):
	# Verify if the file name came as parameter
	if contact_file_name == "":
		# Set the default name for the file
		contact_file_name = 'cm_address_book.txt'

	# Verify if exist contacts at the list
	if len(contact_obj_list) > 0:
		# Variable to count the contacts added to the file
		count_contacts = 0
		try:
			# Create the file Contact Manager Address Book
			with open(contact_file_name, "w+") as contact_file:
				for contact_obj in contact_obj_list:
					# Add contact to a file
					contact_file.write(contact_obj.first_name + "," + contact_obj.last_name + "," + contact_obj.mobile_phone + "," + contact_obj.work_phone + "," + contact_obj.email + "," + contact_obj.twitter_handle + '\n')
					count_contacts += 1

			# Confirm the creation of the file
			if show_message:
				print "\nFile %s created with %i contacts." % (contact_file_name, count_contacts)
		except Exception as error:
			if show_message:
				print error
	else:
		if show_message == True:
			print "\nSorry! There are no contacts to export."

def read_contact_file(show_message, contact_obj_list, contact_file_name = ""):
	# Verify if the name of the file is blank
	if contact_file_name.strip(" ") == "":
		# Set default name
		contact_file_name = 'cm_address_book.txt'

	#if show_message:
	#	print "\nLooking for the contact file %s. Please Wait." % (contact_file_name)

	try:
		# Create the file Contact Manager Address Book
		with open(contact_file_name) as contact_file:
			list_contacts = contact_file.readlines()

		# Verify if there are contacts on the file
		if len(list_contacts) > 0:
			# Loop to add contacts
			for item in list_contacts:
				## Add the contact without validate for duplicates
				#add_contact_to_list(contact_obj_list, item.strip().split(',')[0], item.strip().split(',')[1], item.strip().split(',')[2], item.strip().split(',')[3], item.strip().split(',')[4], item.strip().split(',')[5])
				# Check for duplicates contacts and Add the contact
				add_new_contact(show_message, contact_obj_list, item.strip().split(',')[0], item.strip().split(',')[1], item.strip().split(',')[2], item.strip().split(',')[3], item.strip().split(',')[4], item.strip().split(',')[5])
		else:
			# Contact List from the file is empty
			if show_message:
				print "\nNo contacts were found."
	except Exception as error:
		if show_message:
			print error

def display_all_contacts(contact_obj_list):
	if len(contact_obj_list) == 0:
		print "\nThere are no contacts in the list."
	else:
		# Initiate variable to count contacts and pause the screen
		count_contacts = 0

		print "\nContacts in the list:"
		# Loop to show all the contacts
		for contact in contact_obj_list:
			# show the contact information
			contact.display_contact()
			# Increment contacts count
			count_contacts += 1
			if count_contacts % 3 == 0 and count_contacts < (len(contact_obj_list) - 1):
				# Message to pause the program and show the contacts
				raw_input("\nPress <Enter> to display more contacts.")
		
		# Message to pause the program and show the contacts
		raw_input("\nEnd of contact list. Press <Enter> to return to menu.")

def display_search_contacts(contact_obj_list, search_option, first_name = "", last_name = "", mobile_phone = "", work_phone = "", email ="", twitter_handle ="", general_info = ""):
	'''	Search Options:
		1 - by Full Name
		2 - by First Name
		3 - by Last Name
		4 - by Mobile Phone
		5 - by Work Phone
		6 - by Email
		7 - by Twitter Handle
		8 - by All Fields
	'''
	# Variable to count how many contacts was found
	contact_listed = 0

	# Verify the parameters
	if (search_option == 1 and len(first_name.strip(' ')) > 0 and len(last_name.strip(' ')) > 0) or (search_option == 2 and len(first_name.strip(' ')) > 0) or (search_option == 3 and len(last_name.strip(' ')) > 0) or (search_option == 4 and len(mobile_phone.strip(' ')) > 0) or (search_option == 5 and len(work_phone.strip(' ')) > 0 ) or (search_option == 6 and len(email.strip(' ')) > 0) or (search_option == 7 and len(twitter_handle.strip(' ')) > 0) or (search_option == 8 and len(general_info.strip(' ')) > 0):
		# Valid parameters
		print "\nSearch Results:"
		# Loop to search the contact list
		for contact in contact_obj_list:
			# Verify the user's choice
			if search_option == 1:
				# 1 - by Full Name
				# Verify the First and Last Name
				#if contact.first_name == first_name.lower() and contact.last_name == last_name.lower():
				if first_name.lower() in contact.first_name and last_name.lower() in contact.last_name:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 2:
				# 2 - by First Name
				# Verify the First Name
				#if contact.first_name == first_name.lower():
				if first_name.lower() in contact.first_name:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 3:
				# 3 - by Last Name
				# Verify the Last Name
				#if contact.last_name == last_name.lower():
				if last_name.lower() in contact.last_name:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 4:
				# 4 - by Mobile Phone
				# Verify the Mobile Phone
				#if contact.mobile_phone == mobile_phone.lower():
				if mobile_phone.lower() in contact.mobile_phone:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 5:
				# 5 - by Work Phone
				# Verify the Work Phone
				#if contact.work_phone == work_phone.lower():
				if work_phone.lower() in contact.work_phone:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 6:
				# 6 - by Email
				# Verify the Email
				#if contact.email == email.lower():
				if email.lower() in contact.email:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 7:
				# 7 - by Twitter
				# Verify the Twitter
				#if contact.twitter_handle == twitter_handle.lower():
				if twitter_handle.lower() in contact.twitter_handle:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1
			elif search_option == 8:
				# 8 - by All Fields
				if general_info.lower() in contact.first_name or general_info.lower() in contact.last_name or general_info.lower() in contact.mobile_phone or general_info.lower() in contact.work_phone or general_info.lower() in contact.email or general_info.lower() in contact.twitter_handle:
					# Show the contact
					contact.display_contact()
					# Increment the count
					contact_listed += 1

			# Check if the number is divided by 3
			if contact_listed > 0 and contact_listed % 3 == 0:
				# Message to pause the program and show the contacts
				raw_input("\nPress <Enter> to display more contacts.")
				
		# Verify if some contact was found
		if contact_listed == 0:
			print "\nNo contacts were found for this search!"
		else:
			# Message to pause the program and show the contacts
			raw_input("\nEnd of search list. Press <Enter> to return to menu.")
	else:
		print "\nInvalid parameters! Please try again."

def show_search_menu():
	'''Show the Search Menu Formatted'''
	print """
			+-----------------------------+
			|       Contact Manager       |
			+-----------------------------+
			|         Search Menu         |
			+-----------------------------+
			|  1 - by Full Name           |
			|  2 - by First Name          |
			|  3 - by Last Name           |
			|  4 - by Mobile Phone        |
			|  5 - by Work Phone          |
			|  6 - by Email               |
			|  7 - by Twitter Handle      |
			|  8 - by All Fields          |
			+-----------------------------+
			|  0 - Return to Main Menu    |
			+-----------------------------+
		  """

def menu_search_contact(contact_obj_list):
	# Validate the parameters
	if len(contact_obj_list) == 0:
		print "\nThere are no contacts in the list."
	else:
		# Loop to choose Search Menu options
		while True:
			# Show the Search Menu formatted
			show_search_menu()

			# Protect against error for the conversion to int(), case the user type <Enter> or String
			try:
				menu_option = int(raw_input("Select an option from the Search Menu: "))
			except ValueError:
				menu_option = None

			# Verify the user's choice
			if menu_option == 1:
				# 1 - by Full Name
				first_name = raw_input("\nPlease enter the First Name: ")
				# Verify the first name
				if first_name.strip(' ') == "":
					print "\nFirst Name cannot be blank.  Please try again."
				else:
					last_name = raw_input("Please enter the Last Name: ")
					# Verify the last name
					if last_name.strip(' ') == "":
						print "\nLast Name cannot be blank.  Please try again."
					else:
						display_search_contacts(contact_obj_list, search_option = menu_option, first_name = first_name, last_name = last_name)
			elif menu_option == 2:
				# 1 - by First Name
				first_name = raw_input("\nPlease enter the First Name: ")
				# Verify the first name
				if first_name.strip(' ') == "":
					print "\nFirst Name cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, first_name = first_name)
			elif menu_option == 3:
				# 1 - by Last Name
				last_name = raw_input("\nPlease enter the Last Name: ")
				# Verify the last name
				if last_name.strip(' ') == "":
					print "\nLast Name cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, last_name = last_name)
			elif menu_option == 4:
				# 4 - by Mobile Phone
				mobile_phone = raw_input("\nPlease enter the Mobile Phone: ")
				# Verify the Mobile Phone
				if mobile_phone.strip(' ') == "":
					print "\nMobile Phone cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, mobile_phone = mobile_phone)
			elif menu_option == 5:
				# 5 - by Work Phone
				work_phone = raw_input("\nPlease enter the Work Phone: ")
				# Verify the Work Phone
				if work_phone.strip(' ') == "":
					print "\nWork Phone cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, work_phone = work_phone)
			elif menu_option == 6:
				# 6 - by Email
				email = raw_input("\nPlease enter the Email: ")
				# Verify the Email
				if email.strip(' ') == "":
					print "\nEmail cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, email = email)
			elif menu_option == 7:
				# 7 - by Twitter Handle
				twitter_handle = raw_input("\nPlease enter the Twitter Handle: ")
				# Verify the Twitter
				if twitter_handle.strip(' ') == "":
					print "\nTwitter cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, twitter_handle = twitter_handle)
			elif menu_option == 8:
				# 8 - by All Fields
				general_info = raw_input("\nPlease enter the Information: ")
				# Verify the Twitter
				if general_info.strip(' ') == "":
					print "\nInformation cannot be blank.  Please try again."
				else:
					display_search_contacts(contact_obj_list, search_option = menu_option, general_info = general_info)
			elif menu_option == 0:
				# 0 - Exit
				# Return to Main Menu
				break
			else:
				print "\nInvalid option! Please select an option from the Search Menu."

def show_update_menu():
	'''Show the Update Menu formatted'''
	print """
			+-----------------------------+
			|       Contact Manager       |
			+-----------------------------+
			|         Update Menu         |
			+-----------------------------+
			|  1 - First Name             |
			|  2 - Last Name              |
			|  3 - Mobile Phone           |
			|  4 - Work Phone     	      |
			|  5 - Email                  |
			|  6 - Twitter Handle         |
			+-----------------------------+
			|  0 - End Updates            |
			+-----------------------------+
		  """

def update_contact_menu(contact_obj):
	'''Menu and options to Update a contact'''

	if contact_obj == None:
		print "\nInvalid contact!"
	else:
		while True:
			# Show the contact info
			contact_obj.display_contact()

			# Show the Update menu formatted
			show_update_menu()

			try:
				# Testing using String without convert to integer
				update_menu_option = raw_input("\nSelect the information you would like to change: ")
			except ValueError:
				update_menu_option = None

			# Verify the user option
			if update_menu_option == "1":
				# Option 1 - Update First Name
				new_info = raw_input("\nEnter the New First Name: ")
				if len(new_info.strip(" ")) > 0:
					# Confirm the change
					print "\nYou are changing the contact's First Name\n From: %s\n To  : %s" % (contact_obj.first_name, new_info)
					confirm_change = raw_input("\nConfirm the change?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if confirm_change.lower() == "y":
						# Change the first name
						contact_obj.change_first_name(new_info.lower())
						print "\nContact First Name changed!"
				else:
					print "\nInvalid information!  Please try again."
			elif update_menu_option == "2":
				# Option 2 - Update Last Name
				new_info = raw_input("\nEnter the New Last Name: ")
				if len(new_info.strip(" ")) > 0:
					# Confirm the change
					print "\nYou are changing the contact's Last Name\n From: %s\n To  : %s" % (contact_obj.last_name, new_info)
					confirm_change = raw_input("\nConfirm the change?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if confirm_change.lower() == "y":
						# Change the first name
						contact_obj.change_last_name(new_info.lower())
						print "\nContact Last Name changed!"
				else:
					print "\nInvalid information!  Please try again."
			elif update_menu_option == "3":
				# Option 3 - Update Mobile Phone
				new_info = raw_input("\nEnter the New Mobile Phone: ")
				if len(new_info.strip(" ")) > 0:
					# Confirm the change
					print "\nYou are changing the contact's Mobile Phone\n From: %s\n To  : %s" % (contact_obj.mobile_phone, new_info)
					confirm_change = raw_input("\nConfirm the change?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if confirm_change.lower() == "y":
						# Change the Mobile Phone
						contact_obj.change_mobile_phone(new_info.lower())
						print "\nContact Mobile Phone changed!"
				else:
					print "\nInvalid information!  Please try again."
			elif update_menu_option == "4":
				# Option 4 - Update Work Phone
				new_info = raw_input("\nEnter the New Work Phone: ")
				if len(new_info.strip(" ")) > 0:
					# Confirm the change
					print "\nYou are changing the contact's Work Phone\n From: %s\n To  : %s" % (contact_obj.work_phone, new_info)
					confirm_change = raw_input("\nConfirm the change?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if confirm_change.lower() == "y":
						# Change the Work Phone
						contact_obj.change_work_phone(new_info.lower())
						print "\nContact Work Phone changed!"
				else:
					print "\nInvalid information!  Please try again."
			elif update_menu_option == "5":
				# Option 5 - Update Email
				new_info = raw_input("\nEnter the New Email: ")
				if len(new_info.strip(" ")) > 0:
					# Confirm the change
					print "\nYou are changing the contact's Email\n From: %s\n To  : %s" % (contact_obj.email, new_info)
					confirm_change = raw_input("\nConfirm the change?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if confirm_change.lower() == "y":
						# Change the Email
						contact_obj.change_email(new_info.lower())
						print "\nContact Email changed!"
				else:
					print "\nInvalid information!  Please try again."
			elif update_menu_option == "6":
				# Option 6 - Update Twitter Handle
				new_info = raw_input("\nEnter the New Twitter Handle: ")
				if len(new_info.strip(" ")) > 0:
					# Confirm the change
					print "\nYou are changing the contact's Twitter Handle\n From: %s\n To  : %s" % (contact_obj.twitter_handle, new_info)
					confirm_change = raw_input("\nConfirm the change?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if confirm_change.lower() == "y":
						# Change the Twitter Handle
						contact_obj.change_twitter_handle(new_info.lower())
						print "\nContact Twitter Handle changed!"
				else:
					print "\nInvalid information!  Please try again."
			elif update_menu_option == "0":
				# Exist from the loop menu
				break
			else:
				print "\nInvalid option! Please select an option from the Update Menu."

def remove_first_contact_by_name(contact_obj_list, first_name, last_name):
	'''Remove the first instance of the First and Last name and stop'''
	# Verify if the list has contacts
	if len(contact_obj_list) == 0:
		print "\nThere are no contacts in the list."
	else:
		# Initialize the variable to count if contacts could be found
		contacts_found = 0
		
		# Loop to search the list
		for index in range(len(contact_obj_list)):
			# Compare Fist and Last Name
			if first_name.lower() in contact_obj_list[index].first_name and last_name.lower() in contact_obj_list[index].last_name:
				# Found a match contact
				# Increment variable
				contacts_found += 1
				# Show Contact information
				contact_obj_list[index].display_contact()
				# Ask confirmation to remove
				user_option = raw_input("\nAre you sure you want to remove this contact?  Type  Y  to confirm or any other key to cancel: ")
				# Verify the user's choice
				if user_option.lower() == "y":
					# Delete contact from the list
					del contact_obj_list[index]
					print "\nContact removed!"
					# Stop the loop
					break
		
		# Verify if could found some contact
		if contacts_found == 0:
			print "No contacts were found!"

def remove_contact_by_name(contact_obj_list, first_name, last_name):
	'''Remove all instances with the same first name and last name'''
	# Verify if the list is empty
	if len(contact_obj_list) == 0:
		print "\nThere are no contacts in the list."
	else:
		# Initialize the list index
		index = 0
		# Initialize the variable to count if contacts could be found
		contacts_found = 0
		
		# Loop to search the list
		while True:
			# Test to check only indexes in the list
			if index < len(contact_obj_list):
				# Compare Fist and Last name
				if first_name.lower() in contact_obj_list[index].first_name and last_name.lower() in contact_obj_list[index].last_name:
					# Found a match contact
					# Increment variable
					contacts_found += 1
					# Show Contact information
					contact_obj_list[index].display_contact()
					# Ask confirmation to remove
					user_option = raw_input("\nAre you sure you want to remove this contact?  Type  Y  to confirm or any other key to cancel: ")
					# Verify the user's choice
					if user_option.lower() == "y":
						# Delete contact from the list
						del contact_obj_list[index]
						print "\nContact %s %s removed!" % (first_name, last_name)
					else:
						# Set to next index
						index += 1
				else:
					# Set to next index
					index += 1
			else:
				# Stop the loop
				break

		# Verify if could found some contact
		if contacts_found == 0:
			print "No contacts were found!"

def show_main_menu():
	'''Show the Main Menu formatted'''
	print """
			+-----------------------------+
			|       Contact Manager       |
			+-----------------------------+
			|          Main Menu          |
			+-----------------------------+
			|  1 - Display All Contacts   |
			|  2 - Add Contacts           |
			|  3 - Search Contacts        |
			|  4 - Update Contact         |
			|  5 - Remove Contact         |
			+-----------------------------+
			|  6 - Import Contacts        |
			|  7 - Export Contacts        |
			+-----------------------------+
			|  0 - Exit                   |
			+-----------------------------+
		  """

def main_menu(contact_obj_list):
	# Loop to choose Main Menu options
	while True:
		# Show the main menu formatted
		show_main_menu()

		# Protect against error for the conversion to int(), case the user type <Enter> or String
		try:
			menu_option = int(raw_input("Select an option from the Main Menu: "))
		except ValueError:
			menu_option = None

		# Verify the user's choice
		if menu_option == 1:
			# Option 1 - Display all contacts
			display_all_contacts(contact_obj_list)
		elif menu_option == 2:
			# Option 2 - Add Contacts
			# Loop to keep adding Contacts
			while True:
				print "\nPlease enter the new contact information:"
				# Get the new contact information
				first_name = raw_input("First Name    : ")
				last_name = raw_input("Last Name     : ")
				mobile_phone = raw_input("Mobile Phone  : ")
				work_phone = raw_input("Work Phone    : ")
				email = raw_input("Email         : ")
				twitter_handle = raw_input("Twitter Handle: ")

				# Add the new contact
				add_new_contact(True, contact_obj_list, first_name, last_name, mobile_phone, work_phone, email, twitter_handle)
				
				# Ask the user to quit or add more contacts
				add_more_contacts = raw_input("\nWould you like to add another contact?  Type  Y  to add or any other key to return to Main Menu: ")
				# Verify the user's option
				if add_more_contacts.lower() != 'y':
					# Stop the adding contact loop 
					break
		elif menu_option == 3:
			# Option 3 - Search Contacts
			if len(contact_obj_list) == 0:
				print "There are no contacts in the list."
			else:
				menu_search_contact(contact_obj_list)
		elif menu_option == 4:
			# Option 4 - Update Contact
			if len(contact_obj_list) == 0:
				print "There are no contacts in the list."
			else:
				# Loop to keep searching Contacts
				while True:
					# Get the contact information
					first_name = raw_input("\nPlease enter the First Name to find the contact: ")
					# Verify the first name
					if first_name.strip(' ') == "":
						print "\nFirst Name cannot be blank!  Please try again."
					else:
						last_name = raw_input("Please enter the Last Name: ")
						# Verify the last name
						if last_name.strip(' ') == "":
							print "\nLast Name cannot be blank!  Please try again."
						else:
							# Initialize the variable to count if contacts could be found
							contacts_found = 0

							# Loop to search the contact list
							for index in range(len(contact_obj_list)):
								# Compare the first and last name
								if first_name.lower() in contact_obj_list[index].first_name and last_name.lower() in contact_obj_list[index].last_name:
									# Show Contact Menu to Update
									update_contact_menu(contact_obj_list[index])
									# Increment the variable
									contacts_found += 1

							if contacts_found == 0:
								print "No contacts were found!  Please try again."

					# Ask the user to quit or update more contacts
					update_more_contacts = raw_input("\nWould you like to update another contact?  Type  Y  to yes or any other key to return to Main Menu: ")
					# Verify the user's option
					if update_more_contacts.lower() != 'y':
						# Stop the updating contact loop 
						break
		elif menu_option == 5:
			# Option 5 - Remove Contact
			if len(contact_obj_list) == 0:
				print "There are no contacts in the list."
			else:
				# Loop to keep searching Contacts
				while True:
					# Get the contact information
					first_name = raw_input("\nPlease enter the First Name to find the contact: ")
					# Verify the first name
					if first_name.strip(' ') == "":
						print "\nFirst Name cannot be blank.  Please try again."
					else:
						last_name = raw_input("Please enter the Last Name: ")
						# Verify the last name
						if last_name.strip(' ') == "":
							print "\nLast Name cannot be blank.  Please try again."
						else:
							# Remove contact from the list
							remove_contact_by_name(contact_obj_list, first_name, last_name)

					# Ask the user to quit or Remove more contacts
					remove_more_contacts = raw_input("\nWould you like to remove another contact?  Type  Y  to yes or any other key to return to Main Menu: ")
					# Verify the user's option
					if remove_more_contacts.lower() != 'y':
						# Stop the removing contact loop 
						break
		elif menu_option == 6:
			# Option 6 - Import Contacts
			# Ask the file name
			user_file_name = raw_input("\nEnter the file name to import contacts: ")

			# Verify the file name
			if validate_file_name(user_file_name):
				# Change the file name to lower case
				user_file_name = user_file_name.lower()
				# Read the contact list file
				read_contact_file(True, contact_obj_list, user_file_name)
		elif menu_option == 7:
			# Option 7 - Export Contacts
			if len(contact_obj_list) == 0:
				print "There are no contacts in the list."
			else:
				# Ask the file name
				user_file_name = raw_input("\nEnter a name for the export file you want to create,\nfor example contact_list.txt: ")

				# Verify the file name
				if validate_file_name(user_file_name):
					# Change the file name to lower case
					user_file_name = user_file_name.lower()
					# Write the file
					write_contact_file(True, contact_obj_list, user_file_name)
		elif menu_option == 0:
			# Option 0 - Exit
			# Write the file
			write_contact_file(False, contact_obj_list)
			print "\nThank you for using the Contact Manager!"
			# Exit from the loop and end the program
			break
		else:
			print "\nInvalid option! Please select an option from the Main Menu."

def main():
	global address_book

	# Import contacts from default file (if found)
	read_contact_file(False, address_book)
	
	print "\n\nWelcome to Contact Manager"

	# Show the main menu
	main_menu(address_book)
	
if __name__ == "__main__":
	main()