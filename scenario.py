import os
import shutil
import glob

class BashED_Scenario():

	def __init__(self):
        self.scenario_description = ""
		src = "setup/"
		dest = "../../sandbox/"
		shutil.copytree(src, dest)

	def checkpoint():
		src = "../../sandbox/"
		dest = "../../checkpoint/"
		shutil.copytree(src, dest)

	def recover():
		src = "../../checkpoint/"
		dest = "../../sandbox/"
		files_to_remove = glob.glob(dest + "*")
		for file in files_to_remove:
			os.remove(file)
		shutil.copytree(src, dest)

	def print_prompt():
        print self.scenario_description

	def validate():
		pass
