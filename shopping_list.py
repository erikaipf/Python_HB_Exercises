shopping_list = ['blue','pink','purple','orange']

#Option 1: local scope variable, return 
def alphabetical_order(list_to_order):
	list_to_order.sort()
	return list_to_order

#Option 2: global scope variable, print
def alphabetical_list():
	global shopping_list
	shopping_list.sort()
	print shopping_list

def add_list(new_item):
	global shopping_list

	new_item = new_item.lower()

	if new_item in shopping_list:
		print "Item already in the list."
	else:
		shopping_list.append(new_item)
		alphabetical_list()

def remove_item(value_item):
	global shopping_list
	
	value_item = value_item.lower()

	if value_item in shopping_list:
		shopping_list.remove(value_item)
		shopping_list.sort()
	else:
		print "Item is not in the list."

remove_item("black")