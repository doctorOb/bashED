import os
import base_scenario

from verification_helpers import prompt

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = "Alright agent, our enemy has gotten smarter this time! They've realized we've stolen their password, so they've hidden it, by putting a '.' in front of the name! Unfortunately, just using ls won't cut it! You'll have to employ advanced tacticts! Use the '-a' with 'ls', and that should do the trick!"
        self.hint = "Type 'ls -a' and hit enter. The '-a' is called a flag, and it tells ls to display both the hidden and the non hidden files in this folder."
        self.win_message = "Jesus H. Christ agent! You've found the hidden password file! You bypassed their security! We've got to put you on harder stuff!"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return prompt("Enter the name of the password file:", ".passes.txt")
