import os
import base_scenario

from verification_helpers import *

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = ("THEY FOUND THE SECRET FOLDER AND NOW THEY'RE GOING TO BREAK IN. DELETE THE FOLDER NOW USING 'rm'")
        self.hint = "Use the command 'rm SECRET_CODES.txt' to delete the secret file"
        self.win_message = "Phew. We should be safe... OH NO WAIT"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return not file_exists(os.path.join("SECRET", "SECRET_CODES.txt")) 
