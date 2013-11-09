

class Mission():
	
	def __init__(self):
		self.mission_description = ""
		self.win_message = ""
		self.dir = ""

	def print_prompt(self):
		print self.mission_description

	def print_correct(self):
		print self.win_message

	def clean_dirs(self):
		self.sandbox = os.path.join(self.dir, "..", "..", "..", "..", "sandbox")
		self.chkpoint = os.path.join(self.dir, "..", "..", "..", "..", "checkpoint")
		if os.path.isdir(self.sandbox):
            shutil.rmtree(self.sandbox)
        if os.path.isdir(self.chkpoint):
            shutil.rmtree(self.chkpoint)
