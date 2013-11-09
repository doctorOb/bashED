import os
import shutil
import glob

class BashED_Scenario():

	def __init__(self):
		src = "setup/"
		dest = "../../sandbox/"
		shutil.copytree(src, dest)

	def checkpoint():
		src = "../../sandbox/"
		dest = "../../checkpoint/"
		files_to_remove = glob.glob(dest + "*")
		for file in files_to_remove:
			os.remove(file)
		shutil.copytree(src, dest)