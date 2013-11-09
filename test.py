import os
from StringIO import StringIO
import sys

def closest_path(path):
    """given a potential path (such as /root/sys/almostaname), finds the closest directory in the tree"""
    path = os.path.abspath(path)
    while not os.path.isdir(path):
        path = path[0:path.rindex('/')]
    return path



print(closest_path('/Users/danrobertson/YHack'))
print(closest_path('../'))
print(closest_path('..'))

matches = ['consolepanel','consolehat','consofd','consod']

i = 0
while True:
	candidate = matches[0][i]
	for match in matches:
		if match[i] != candidate:
			stop = True
			break
	if stop:
		break
	i+=1

