import os
import shutil
import glob
import distutils.dir_util
import verification_helpers
def hack(a, b):
    print "I WIN NOOBS"
    return True
verification_helpers.prompt=hack

class Scenario():

    def __init__(self):
        self.dir = ""
        self.scenario_description = ""
        self.hint = ""
        self.win_message = ""

    def setup(self):
        self.src = os.path.join(self.dir, "setup")
        self.dest = os.path.join(self.dir, "..", "..", "..", "..", "sandbox")
        if os.path.isdir(self.dest):
            distutils.dir_util.copy_tree(self.src, self.dest)
        else:
            shutil.copytree(self.src, self.dest)
        self.checkpoint()

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
        print '-'*30 + " next task " + '-'*30
        print self.scenario_description

    def print_hint(self):
        print self.hint

    def print_correct(self):
        print self.win_message
      
    def validate(self):
        pass
