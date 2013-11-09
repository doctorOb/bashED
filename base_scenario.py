import os
import shutil
import glob

class BashED_Scenario():

	def __init__(self):
        self.scenario_description = ""
        self.hint = ""
        self.win_message = ""
		src = "setup/"
		dest = "../../sandbox/"
		shutil.copytree(src, dest)

	def checkpoint(self):
		src = "../../sandbox/"
		dest = "../../checkpoint/"
		shutil.copytree(src, dest)

	def recover(self):
		src = "../../checkpoint/"
		dest = "../../sandbox/"
		files_to_remove = glob.glob(dest + "*")
		for file in files_to_remove:
			os.remove(file)
		shutil.copytree(src, dest)

	def print_prompt(self):
        print self.scenario_description

	def validate(self):
		pass

    def print_hint(self):
        print self.hint

    def print_correct(self):
        print self.win_message
