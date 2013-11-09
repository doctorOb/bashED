import os
import base_scenario

from verification_helpers import *

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = ("Make sure a directory 'durr' exists, and in that directory is an empty file called 'df.txt'. Also, there must be a file 'f.txt', containing only the text 'a character'. Also, enter 'yale'."
        self.hint = "'touch file.txt' creates an empty file called file.txtt. mkdir makes directories. `echo 'a string' > file.txt make the contents of file.txt be 'a string'"
        self.win_message = "Great job! You did it!"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return dir_exists("durr") and file_exists(os.path.join("durr", "df.txt")) and file_exists("f.txt") and file_matches('f.txt', os.path.join(self.dir, 'f.txt')) and prompt("Enter something", "yale") 
