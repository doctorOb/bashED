import os
import base_scenario

from verification_helpers import prompt

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = "It looks like they've added another password, but this time it will be even harder! This time, they moved it out of this folder (a.k.a. a \"directory\"). Use 'cd folder-name' (menaing \"change directory\") to move into that directory and have a look around. To go back up, use 'cd ..'. Good luck agent."
        self.hint = "You can run 'cd folder1' to go into folder1, then you can 'ls' inside that one. to go back up a folder, use 'cd ..'"
        self.win_message = "Well done. You're on you way to greater things."
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return prompt("Which folder was it in? folder1 or folder2?", "folder2")
