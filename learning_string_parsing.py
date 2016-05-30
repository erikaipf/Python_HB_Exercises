print "Converting a string in a list:"
print "  my_name = 'Erika'"
my_name = 'Erika'
print "  list(my_name) =", list(my_name)
print ""
print "Converting a sequence of numbers in a list: '1,2,3,4,5'.split(',') =", '1,2,3,4,5'.split(',')
print ""
print "fish_list = 'One fish two fish red fish blue fish '"
fish_list = 'One fish two fish red fish blue fish '
print ""
print "Replacing string: fish_list.replace(' fish', '') = '" + fish_list.replace(' fish', '') + "'"
print ""
print "Using more than one function in a string or variable:" 
print "  'One fish two fish red fish blue fish '.replace(' fish', '').split(' ') =", 'One fish two fish red fish blue fish'.replace(' fish', '').split(' ')
print "  or"
print "  fish_list.replace(' fish', '').split(' ') =", fish_list.replace(' fish', '').split(' ')
print ""
print "Strings with hiden codes: grocery_str = 'item:apples,quantity:4,price:1.50\\n'"
grocery_str = 'item:apples,quantity:4,price:1.50\n'
print ""
grocery_str = grocery_str.strip()
print "Cleaning hiden code on strings: grocery_str.strip() = '" + grocery_str + "'"
print ""
print "Using index to get the price:"
print "  grocery_str.split(',') = ", grocery_str.split(',')
print "  grocery_str.split(',')[2] = '" + grocery_str.split(',')[2] + "'"
print "  grocery_str.split(',')[2].split(':') =" , grocery_str.split(',')[2].split(':')
print "  grocery_str.split(',')[2].split(':')[1] = '" + grocery_str.split(',')[2].split(':')[1] + "'"
print "  float(grocery_str.split(',')[2].split(':')[1]) = " + grocery_str.split(',')[2].split(':')[1]
print ""
print "Calculating Quantity x Price (4 x 1.50):"
print "  float(grocery_str.split(',')[1].split(':')[1]) * float(grocery_str.split(',')[2].split(':')[1]) = " + str(float(grocery_str.split(',')[1].split(':')[1]) * float(grocery_str.split(',')[2].split(':')[1]))
print ""
print """Example using functions:\n
def make_variable_str(num, string):
 	return string[num].strip().split(",")

def total_subitem_price(variable):
 	return float(variable[1].split(":")[1]) * float(variable[2].split(":")[1])

items = ["item:apples,quantity:4,price:1.50\\n", "item:pears,quantity:5,price:2.00\\n", "item:cereal,quantity:1,price:4.49\\n"]
apples = make_variable_str(0, items)
pears = make_variable_str(1, items)
cereal = make_variable_str(2, items)

total_bill = total_subitem_price(apples) + total_subitem_price(pears) + total_subitem_price(cereal)
print total_bill"""
print "\nResult = ",
def make_variable_str(num, string):
 	return string[num].strip().split(",")

def total_subitem_price(variable):
 	return float(variable[1].split(":")[1]) * float(variable[2].split(":")[1])

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]
apples = make_variable_str(0, items)
pears = make_variable_str(1, items)
cereal = make_variable_str(2, items)

total_bill = total_subitem_price(apples) + total_subitem_price(pears) + total_subitem_price(cereal)
print total_bill