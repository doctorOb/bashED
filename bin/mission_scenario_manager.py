import os
import importlib

MISSION_DIR = os.path.join("bashED", "missions")
MISSION_ORDER = os.path.join(MISSION_DIR, "mission_order.txt")
SCENARIO_FILE = "scenario_order.txt"


def get_next_mission_str(prev_mission):
    """takes in the previous mission name, gives the next mission
    empty string if that was the last mission defined"""
    with open(MISSION_ORDER, 'r') as f:
        for line in f:
            if line == prev_mission:
                break
        return f.readline()


def get_next_scenario_str(curr_mission, prev_scenario):
    """takes in the previous scenario name and current mission, gives the next scenario
    empty string if that was the last scenario defined"""
    with open(os.path.join(MISSION_DIR, curr_mission, SCENARIO_FILE), 'r') as f:
        for line in f:
            if line == prev_scenario:
                break
        return f.readline()


def get_next_mission(prev_mission):
    """takes in the previous mission name and gives the next mission object"""
    mstr = get_next_mission_str(prev_mission)
    module = importlib.import_module(os.path.join(MISSION_DIR, mstr, "mission"))
    return module.Mission()


def get_next_scenario(curr_mission, prev_scenario):
    """takes in the previous mission name and gives the next mission object"""
    sstr = get_next_scenario_str(prev_scenario)
    module = importlib.import_module(os.path.join(MISSION_DIR, curr_mission, sstr, "scenario"))
    return module.Scenario()
