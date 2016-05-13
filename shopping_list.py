# Create the dictionary
shopping_lists = {}

def show_all_stores():
	# Show all keys and values from the list
	global shopping_lists

	if len(shopping_lists) < 1:
		print 'Your shopping list is empty!'
	else:
		print shopping_lists

def show_spe_store():
	# Show the items from a specific store
	global shopping_lists

	spe_store = raw_input("Please enter the name of the store: ")#.lower()

	if spe_store in shopping_lists.keys():
		if len(shopping_lists[spe_store]) < 1:
			print "%s doesn't have items." % (spe_store)
		else:
			print spe_store, "\n", shopping_lists[spe_store]
	else:
		print "Sorry the store doesn't exist!"

def add_store():
	# Add a Store to the list
	global shopping_lists

	add_store = raw_input("Please add the name of the store: ") #.lower()
	
	if add_store in shopping_lists.keys():
		print "Store already exist!"
	else:
		shopping_lists[add_store] = []

# def remove_store(key):
# 	global shopping_lists
# 	pass

def add_item_to_store():
	global shopping_lists

	while True:
		store = raw_input("Please enter the name of the store: ")#.lower()

		if store not in shopping_lists:
			print "Sorry the store doesn't exist!"
		else:
			add_item = raw_input("Please add the item: ")#.lower()

			shopping_lists[store] = shopping_lists[store] + [add_item,]
			#shopping_lists[store] = shopping_lists[store].sort

			break

	#must also sort
	

# def remove_item_from_store(key,value):
# 	global shopping_lists
# 	pass

# def main_menu():
# 	pass

def main():
	# create the loop
	# call the menu
	# test the user option
	add_store()
	add_item_to_store()
	add_item_to_store()
	add_item_to_store()
	show_all_stores()
	show_spe_store()

if __name__ == '__main__':
	main()
