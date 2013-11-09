import os
import shutil
import glob

class Scenario():

	def __init__(self):
		self.scenario_description = ""
	  	self.hint = ""
	  	self.win_message = ""

	def setup(self):
		self.src = "setup/"
		self.dest = "../../sandbox/"
		if os.path.isdir(self.dest):
			shutil.rmtree(self.dest)
		shutil.copytree(self.src, self.dest)

	def checkpoint(self):
		self.src = "../../sandbox/"
		self.dest = "../../checkpoint/"
		if os.path.isdir(self.dest):
			shutil.rmtree(self.dest)
		shutil.copytree(self.src, self.dest)

	def recover(self):
		self.src = "../../checkpoint/"
		self.dest = "../../sandbox/"
		if os.path.isdir(self.dest):
			shutil.rmtree(self.dest)
		shutil.copytree(self.src, self.dest)

	def print_prompt(self):
		print self.scenario_description

	def print_hint(self):
		print self.hint

	def print_correct(self):
		print self.win_message
	  
	def validate(self):
		pass
