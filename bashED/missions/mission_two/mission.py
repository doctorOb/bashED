import os
import base_mission

class Mission(base_mission.Mission):
	
	def __init__(self):
		self.mission_description = "THANK GOD YOU'RE HERE AGENT! WE NEED SOMEONE LIKE YOU ON THE FRONT LINES TODAY. The enemy has breached our security systems!"
		self.win_message = "You conquered the abyss!"
		self.dir = os.path.dirname(os.path.realpath(__file__))
