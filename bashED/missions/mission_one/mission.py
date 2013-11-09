import os
import base_mission

class Mission(base_mission.Mission):
	
	def __init__(self):
		self.mission_description = "Hello young agent! I know this is your fist day but we have a TOP PRIORITY mission for you. It's of dire urgency.?"
		self.win_message = "You successfully navigated your first perilousmission."
		self.dir = os.path.dirname(os.path.realpath(__file__))
