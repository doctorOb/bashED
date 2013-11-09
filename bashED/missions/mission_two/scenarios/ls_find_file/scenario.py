import os
import base_scenario

from verification_helpers import prompt

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = ("You're a secret agent and you need to get into "
                                     "some system or something like that. There's a "
                                     "file in this directory that contains the "
                                     "password to the system. Use the `ls` command "
                                     "to see the files in the current directory, and "
                                     "find the files with the passwords!")
        self.hint = "type `ls` and see which file might contain the passwords, then type `bashed play` to continue"
        self.win_message = "Great job! You found the file!"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return prompt("Enter the name of the secret file", "passwords.txt")
