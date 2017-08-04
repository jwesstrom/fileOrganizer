# -*- coding: utf-8 -*-
# makes degree symbol possible


class fileObject(object):

	def __init__(self, name, folder, ext):
		self.name = name
		self.folder = folder
		self.ext = ext

fileTypes = {}

fileList = []

import cPickle as pickle
import os
from os.path import join, getsize
for root, dirs, files in os.walk('/home/jon/Downloads'):
	for i in files:

		tExt = i.split('.')
		tName = '.'.join(tExt[0:-1])
		tExt = tExt[-1]





		fileList.append(fileObject(tName, root, tExt))

		tObject = fileList[-1]

		try: 
			fileTypes[tExt].append(tObject)
		except KeyError:
			fileTypes[tExt] = [tObject]


print len(fileList) 