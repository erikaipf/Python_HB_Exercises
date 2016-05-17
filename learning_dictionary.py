# Course Intro to Programming - Hackbright Academy
# Dictionary
# by Erika Freiha 15-May-2016

# Examples of using Dictionary
print "Dictionary = {Key : Values}"
print "Creating an empty Dictionary: my_dicio = {}"
my_dicio = {}
print ""
print "Adding values: my_dicio['String'] = 'Sequence of caracters'"
my_dicio['String'] = 'Sequence of caracters'
print ""
print "Adding values: my_dicio['Number'] = 9"
my_dicio['Number'] = 9
print ""
print "Adding with values: my_dicio['List'] = [3,2,1,'z','b','f',]"
my_dicio['List'] = [3,2,1,'z','b','f',]
print ""
print "Printing the dictionary: my_dicio =", my_dicio
print "Printing the dictionary (Pairs): my_dicio.items() =", my_dicio.items()
print "Printing the dictionary: my_dicio.keys() =", my_dicio.keys()
print "Printing the dictionary: my_dicio.values() =", my_dicio.values()
print ""
print "Show values for key: my_dicio['String'] =", my_dicio['String']
print "Show values for key: my_dicio['Number'] =", my_dicio['Number']
print "Show values for key: my_dicio['List'] =", my_dicio['List']
print ""
print "Show values for key and List Index: my_dicio['List'][0] =", my_dicio['List'][0]
print "Loop my_dicio"
for i in my_dicio:
	print ' - ', i
print "Loop my_dicio.keys()"
for i in my_dicio.keys():
	print ' - ', i
print "Loop my_dicio.values()"
for i in my_dicio.values():
	print ' - ', i
print "Loop my_dicio.items()"
for i in my_dicio.items():
	print ' - ', i
print "Sort"
my_dicio["List"].sort()
print my_dicio["List"]

#  How to sort the Keys?