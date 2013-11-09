import os
import base_mission

class Mission(base_mission.Mission):
	
	def __init__(self):
		self.mission_description = "You have to go on your first perilous mission. today."
		self.win_message = "You successfully navigated your first perilousmission."
		self.dir = os.path.dirname(os.path.realpath(__file__))
