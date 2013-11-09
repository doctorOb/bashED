import os
import base_scenario

from verification_helpers import prompt

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = "First, young recruit, we need to find the enemies password file! They're storing their password on this very machine! We need you to use the command 'ls' in order to see what's in thie folder. Once you think you've found it, let me know, so the boys downstairs can get to cracking it!"
        self.hint = "Type 'ls' and hit enter. Which one do you think contains the password? Type the name of the file."
        self.win_message = "Great job agent! We need you to do a few more things, and it's going to get dangerous!"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return prompt("Enter the name of the secret file", "passwords.txt")
