# Course Intro to Programming - Hackbright Academy
# Ch. 9 List - Activity 1
# by Erika Freiha 05-May-2016

# Examples of using lists
print "Creating an empty list: my_list = []"
my_list = []
print "My empty list is", my_list
print ""
print "Creating a list with values: my_list = [1, 2, 'kitten', 4, 'five']"
my_list = [1, 2, "kitten", 4, "five"]
#  index   0  1     2      3    4            
print ""
print "My list now is", my_list
print " index          0  1     2      3    4"
print "               -5 -4    -3     -2   -1"
print ""
print "The third element in my list: my_list[2] =", my_list[2]
print ""
print "The third index of my list: my_list[3] =", my_list[3]
print ""
print "Length of my_list: len(my_list) =", len(my_list)
print ""
print "Ways to access the last element of the list:"
print "my_list[4] =", my_list[4]
print "my_list[-1] =", my_list[-1]
print "my_list[(len(my_list)-1)] =", my_list[(len(my_list)-1)]
print "my_list[4:] =", my_list[4:]
print ""
print "Add new element to my list at the end: my_list.append(6)"
my_list.append(6)
print "My list now is", my_list
print " index          0  1     2      3    4     5"
print "               -6 -5    -4     -3   -2    -1"
print ""
print "Add more than one elements to my list at the end: my_list.extend([7,8])"
my_list.extend([7,8])
print "My list now is", my_list
print " index          0  1     2      3    4     5  6  7"
print "               -8 -7    -6     -5   -4    -3 -2 -1"
print ""
print "Concatenation of lists: my_list + ['kitten','cat']"
my_list = my_list + ['kitten','cat']
print "My list now is", my_list
print " index          0  1     2      3    4     5  6  7      8        9"
print "               -10-9    -8     -7   -6    -5 -4 -3     -2       -1"
print ""
print "Looking for an element in the list (Membership):"
print "5 in my_list =",5 in my_list
print "7 in my_list =",7 in my_list
print ""
print "Count how many times the value appears in the list:"
print "my_list.count('kitten') =", my_list.count('kitten')
print ""
print "Delete last item from the list: my_list.pop()"
my_list.pop()
print "My list now is", my_list
print " index          0  1     2      3    4     5  6  7      8"
print "               -9 -8    -7     -6   -5    -4 -3 -2     -1"
print ""
print "Remove the value from the list (only the first found one): my_list.remove('kitten')"
my_list.remove('kitten')
print "My list now is", my_list
print " index          0  1  2    3     4  5  6     7"
print "               -8 -7 -6   -5    -4 -3 -2    -1"
print ""
print "Delete index from the list: del my_list[7]"
del my_list[7]
print ""
print "My list now is", my_list
print " index          0  1  2    3     4  5  6"
print "               -7 -6 -5   -4    -3 -2 -1"
print ""
print "Search the index of a value: my_list.index('five') =", my_list.index('five')
print ""
print "Sort list: my_list.sort()"
my_list.sort()
print ""
print "My list now is", my_list
print " index          0  1  2  3  4  5    6"
print "               -7 -6 -5 -4 -3 -2   -1"
print ""
print "Repetition of lists: [1,2,3] * 3"
print [1,2,3] * 3
print ""
print "Iteration: for x in [1, 2, 3]: print x"
print "               print x"
for x in [1, 2, 3]:
	print x
print ""
print "Iteration: for x in my_list: print x"
print "               print x"
for x in my_list:
	print x