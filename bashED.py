import argparse
import os

STATE_FILE = os.path.join("bashED", "state.py")
MISSION_DIR = os.path.join("bashED", "missions")


def play():
    scenario = load_scenario()
    if scenario.validate():
        scenario.print_correct()
        #somehow get the next scenario, load that in, and write to the STATE_FILE
        pass
    else:
        print "Not quite the correct solution. Run `bashed --hint` if you need more help, and `bashed --reset` to start over."


def hint():
    scenario = load_scenario()
    scenario.print_hint()


def reset():
    scenario = load_scenario()
    scenario.recover()
    pass


def load_scenario():
    state = {}
    execfile(STATE_FILE, state)
    #current_mission a string, current_scenario a string, initialized a bool
    if not state['initialized']:
        #GET THE FIRST SCENARIO OF SOME MISSION, AND THEN call the setup thingymabober
        pass
    elif not state['current_scenario']:
        raise "ERROR! The state says initialized, but there is no current_scenario set."
    else:
        return None
        #load up the scenario defined in state['current_scenario'] and return it!


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
