import argparse
import os
import json

from mission_scenario_manager import get_first_mission_str, get_first_mission, get_scenario_by_str, get_first_scenario_str, get_first_scenario, get_next_scenario_str, get_next_mission_str


STATE_FILE = os.path.join("bashED", "state.json")
MISSION_DIR = os.path.join("bashED", "missions")


def play():
    tup = load_state()
    scenario = tup[0]
    state = tup[1]
    if scenario.validate():
        scenario.print_correct()
        next_scenario_str = get_next_scenario_str(state['mission'], state['scenario'])
        print "next scenario is %s" % next_scenario_str
        if not next_scenario_str:
            #need to go to the next mission
            next_mission_str = get_next_mission_str(state['mission'])
            if not next_mission_str:
                print "GAME OVER!! IN THAT YOU WIN!! YOU BEAT ALL THE MISSIONS!!! WORLD SAVED!!!!!!!!!!!!!!!!!!!!!!!!"
                exit(0)
            else:
                next_mission = get_next_mission(state['mission'])
                next_mission.print_prompt()
                state['mission'] = next_mission_str
                next_scenario_str = get_first_scenario_str((state['mission']))
                next_scenario = get_scenario_by_str(next_mission_str, next_scenario_str)
                next_scenario.setup()
                next_scenario.print_prompt()
                state['scenario'] = next_scenario_str
                write_state(state)
        else:
            next_scenario = get_scenario_by_str(state['mission'], next_scenario_str)
            next_scenario.setup()
            next_scenario.print_prompt()
            state['scenario'] = next_scenario_str
            write_state(state)
    else:
        print "Not quite the correct solution. Run `bashed --hint` if you need more help, and `bashed --reset` to start over."
        scenario.print_prompt()


def hint():
    scenario = load_state()[0]
    scenario.print_hint()


def reset():
    scenario = load_state()[0]
    scenario.recover()
    pass


def write_state(state):
    with open(STATE_FILE, 'w') as f:
        f.write(json.dumps(state))


def load_state():
    """pretty shitty code:
        if this is the first time loading (and the state.initialized is False, then it will get the first mission,
        run setup, and get the first scenario, run setup, and then write the new state to the file, and exit hard.

        if it isn't the first time, it loads the mission and scenario defined in state, and returns a tuple,
        the first element of which is the scenario instance, the second element being the dict representing the state.
        good luck with thisone, and TODO: refactor this shit."""
    with open(STATE_FILE, 'r') as f:
        state = json.loads(f.readline())
        #current_mission a string, current_scenario a string, initialized a bool
        if not state['initialized']:
            mstr = get_first_mission_str()
            mission = get_first_mission()
            state['mission'] = mstr
            sstr = get_first_scenario_str(mstr)
            scenario = get_first_scenario(mstr)
            state['scenario'] = sstr
            state['initialized'] = True

            mission.print_prompt()
            scenario.setup()
            scenario.print_prompt()

            write_state(state)
            exit(0)
            #yeah this is probably a bad idea, but it's the "right" thing to do? right? it's only 3:35am...
        elif not state['mission']:
            raise "ERROR! The state says initialized, but there is no misison set."
        elif not state['scenario']:
            raise "ERROR! The state says initialized, but there is no scenario set."
        else:
            return (get_scenario_by_str(state['mission'], state['scenario']), state)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This is bashED, the interactive tutorial for the unix command line!')
    parser.add_argument(
        '-p', '--play', action='store_true', help="This is the default command. It will provide you with the scneario and check to see that you've done it correctly! Use this!")
    parser.add_argument(
        '--hint', action='store_true', help="This can give you a hint on how to complete the scenario. Use when you're stuck.")
    parser.add_argument(
        '-r', '--reset', action='store_true', help="This will reset your sandbox to how it was at the beginning of the scenario. Use this if you've mucked everything up and just want to start again.")
    args = parser.parse_args()
    if args.play:
        play()
    elif args.hint:
        hint()
    elif args.reset:
        reset()


    #need to store the current state somewhere.
    #like in some file that has hte mission and the current scenario
