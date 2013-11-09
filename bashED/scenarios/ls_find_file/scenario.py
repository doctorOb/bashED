"""this file should be the subclass which defines the prompt, how to verify the solution, the help, and the win message, maybe more stuff"""
import os

from verification_helpers import prompt, SCENARIO_DIR


class LsScenario():#this should eventually be a subclass of the main Scenario, but that doesn't exist yet...
#I'm looking at you Tyler Stone

    def __init__(self):
        self.scenario_description = ("You're a secret agent and you need to get into "
                                     "some system or something like that. There's a "
                                     "file in this directory that contains the "
                                     "password to the system. Use the `ls` command "
                                     "to see the files in the current directory, and "
                                     "find the files with the passwords!")
        self.help = "type `ls` and see which file might contain the passwords, then type `bashed play` to continue"
        self.path = os.path.join(SCENARIO_DIR, "ls_find_file")
        self.win_message = "Great job! You found the file!"

    def verify(self):
        return prompt("Enter the name of the secret file", "passwords.txt")
