import os
import base_scenario

from verification_helpers import *

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = ("Now, I need you to move my secret codes file to the secret folder using the command 'mv'!")
        self.hint = "Use the command 'mv SECRET_CODES.txt SECRET' to move the file to the folder."
        self.win_message = "Phew. We should be safe... OH NO WAIT"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return file_exists(os.path.join("SECRET", "SECRET_CODES.txt")) 
