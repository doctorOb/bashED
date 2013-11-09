import os
import base_scenario

from verification_helpers import prompt

class Scenario(base_scenario.Scenario):

    def __init__(self):
        self.scenario_description = ("Literally, you're boring, so just do as I say: "
                "please just enter the phrase 'yhacksuc...cess!'"
        self.hint = "type `ls` and see which file might contain the passwords, then type `bashed play` to continue"
        self.win_message = "Great job! You found the file!"
        self.dir = os.path.dirname(os.path.realpath(__file__))

    def validate(self):
        return prompt("What did I tell you to enter?", "yhacksuc...cess!")
