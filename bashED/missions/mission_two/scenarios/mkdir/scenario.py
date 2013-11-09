import os
import base_scenario

from verification_helpers import *

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = ("I left my secret file for super secret codes out in the open! In order to keep these files safe, I need you to move them to a new folder! Use the mkdir command to make the folder 'SECRET'")
        self.hint = "Use the command 'mkdir SECRET' to create a folder"
        self.win_message = "THANK THE LORD FOR YOUR QUICK RESPONSE."
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return dir_exists("SECRET") 
