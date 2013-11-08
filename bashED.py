import argparse
import os

STATE_FILE = os.path.join("bashED", "state.py")


def play():
    state = {}
    execfile(STATE_FILE, state)
    #current_scenario a string, initialized a bool

    if not state['initialized']:
        #GET THE FIRST SCENARIO OF SOME MISSION, AND THEN call the setup thingymabober
        pass
    elif not state['current_scenario']:
        raise "ERROR! The state says initialized, but there is no current_scenario set."
    else:
        #load up the current scenario object
        #call the "yo did it pass?" function from the current scenario
        pass


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


    #need to store the current state somewhere.
    #like in some file that has hte mission and the current scenario
