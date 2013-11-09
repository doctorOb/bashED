import os
import shutil
import glob

class Scenario():

    def __init__(self):
        self.dir = ""
        self.scenario_description = ""
        self.hint = ""
        self.win_message = ""

    def setup(self):
        self.src = os.path.join(self.dir, "setup")
        self.dest = os.path.join(self.dir, "..", "..", "..", "..", "sandbox")
        self.chkpoint = os.path.join(self.dir, "..", "..", "..", "..", "checkpoint")
        if os.path.isdir(self.dest):
            shutil.rmtree(self.dest)
        if not os.path.isdir(self.chkpoint):
            shutil.copytree(self.src, self.chkpoint)
        shutil.copytree(self.src, self.dest)

    def checkpoint(self):
        self.src = os.path.join(self.dir, "..", "..", "..", "..", "sandbox")
        self.dest = os.path.join(self.dir, "..", "..", "..", "..", "checkpoint")
        if os.path.isdir(self.dest):
            shutil.rmtree(self.dest)
        shutil.copytree(self.src, self.dest)

    def recover(self):
        self.src = os.path.join(self.dir, "..", "..", "..", "..", "checkpoint")
        self.dest = os.path.join(self.dir, "..", "..", "..", "..", "sandbox")
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
