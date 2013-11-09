import os

def closest_path(path):
    """given a potential path (such as /root/sys/almostaname), finds the closest directory in the tree"""
    path = os.path.abspath(path)
    while not os.path.isdir(path):
        path = path[0:path.rindex('/')]
    return path



print(closest_path('/Users/danrobertson/YHack'))
print(closest_path('../'))
print(closest_path('..'))

