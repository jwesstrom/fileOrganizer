# -*- coding: utf-8 -*-


dict = {}

dict['test'] = []

try:
	dict['test'].append('a')
	print dict['test']
except KeyError:
	print 'asd'


# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# dict['Age'] = 8; # update existing entry
# dict['School'] = "DPS School"; # Add new entry


# print "dict['Age']: ", dict['Age']
# print "dict['School']: ", dict['School']