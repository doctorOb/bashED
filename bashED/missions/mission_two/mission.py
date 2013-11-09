import os
import base_mission

class Mission(base_mission.Mission):
	
	def __init__(self):
		self.mission_description = "You're about to veture out into the abyss for your second mission"
		self.win_message = "You conquered the abyss!"
		self.dir = os.path.dirname(os.path.realpath(__file__))
