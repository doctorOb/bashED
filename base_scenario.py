import os
import shutil
import glob

class BashED_Scenario():

	def __init__(self):
        self.scenario_description = ""
        self.hint = ""
        self.win_message = ""
		self.src = "setup/"
		self.dest = "../../sandbox/"
		shutil.copytree(src, dest)

	def checkpoint(self):
		self.src = "../../sandbox/"
		self.dest = "../../checkpoint/"
		shutil.copytree(src, dest)

	def recover(self):
		self.src = "../../checkpoint/"
		self.dest = "../../sandbox/"
		self.files_to_remove = glob.glob(dest + "*")
		for file in self.files_to_remove:
			os.remove(file)
		shutil.copytree(src, dest)

	def print_prompt(self):
        print self.scenario_description

    def print_hint(self):
        print self.hint

    def print_correct(self):
        print self.win_message
        
	def validate(self):
		pass