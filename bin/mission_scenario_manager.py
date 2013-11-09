import os
import importlib
import imp

MISSION_DIR = os.path.join("..","bashED", "missions")
MISSION_ORDER = os.path.join(MISSION_DIR, "mission_order.txt")
SCENARIO_FILE = "scenario_order.txt"

"""OMG please refactor this to not have such repetative code, plz plzpl z"""

def get_scenario_by_str(mission_str, scenario_str):
    module = imp.load_source('Scenario', os.path.join(MISSION_DIR, mission_str, 'scenarios', scenario_str, "scenario.py"))
    return module.Scenario()


def get_first_mission_str():
    with open(MISSION_ORDER, 'r') as f:
        return f.readline()[:-1]


def get_first_scenario_str(mission_str):
    with open(os.path.join(MISSION_DIR, mission_str, SCENARIO_FILE)) as f:
        return f.readline()[:-1]


def get_first_mission():
    mstr = get_first_mission_str()
    module = imp.load_source('Mission', os.path.join(MISSION_DIR, mstr, "mission.py"))
    return module.Mission()


def get_first_scenario(mission_str):
    sstr = get_first_scenario_str(mission_str)
    module = imp.load_source('Mission', os.path.join(MISSION_DIR, mission_str, "scenarios", sstr, "scenario.py"))
    return module.Scenario()


def get_next_mission_str(prev_mission):
    """takes in the previous mission name, gives the next mission
    empty string if that was the last mission defined"""

    if not prev_mission:
        return get_first_mission_str()

    with open(MISSION_ORDER, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line[:-1] == prev_mission:
                break
        return f.readline()[:-1]


def get_next_scenario_str(curr_mission, prev_scenario):
    """takes in the previous scenario name and current mission, gives the next scenario
    empty string if that was the last scenario defined"""

    if not prev_scenario:
        return get_first_scenario_str()
    with open(os.path.join(MISSION_DIR, curr_mission, SCENARIO_FILE), 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line[:-1] == prev_scenario:
                break
        return f.readline()[:-1]


def get_next_mission(prev_mission):
    """takes in the previous mission name and gives the next mission object"""
    if not prev_mission:
        mstr = get_first_mission_str()
    else:
        mstr = get_next_mission_str(prev_mission)
    module = imp.load_source('Mission', os.path.abspath(os.path.join(MISSION_DIR, mstr, "mission.py")))
    return module.Mission()


def get_next_scenario(curr_mission, prev_scenario):
    """takes in the previous mission name and gives the next mission object"""
    sstr = get_next_scenario_str(curr_mission, prev_scenario)
    module = imp.load_source('Scenario', os.path.abspath(os.path.join(MISSION_DIR, curr_mission, 'scenarios', sstr, "scenario.py")))
    return module.Scenario()

if __name__ == '__main__':
    print "--"+get_first_mission_str()+"--"
    print "--"+get_first_scenario_str(get_first_mission_str())+"--"
    print "--"+get_next_scenario_str("mission_one", "ls_find_file")+"--"
    print "--"+get_next_mission_str("mission_one")+"--+"
    get_next_scenario("mission_one", "ls_find_file").print_prompt()
    print ""
    get_next_mission("mission_one").print_prompt()
    print ""
    get_scenario_by_str("mission_one", "ls_find_file").print_prompt()
    print ""
    get_first_mission().print_prompt()
    print ""
    get_first_scenario("mission_one").print_prompt()

