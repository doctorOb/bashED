import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This is bashED, the interactive tutorial for the unix command line!')
    parser.add_argument(
        '-p', '--play', type=bool, action='store_true', help="This is the default command. It will provide you with the scneario and check to see that you've done it correctly! Use this!")
    parser.add_argument(
        '--hint', type=bool, action='store_true', help="This can give you a hint on how to complete the scenario. Use when you're stuck.")
    parser.add_argument(
        '-r', '--reset', type=bool, action='store_true', help="This will reset your sandbox to how it was at the beginning of the scenario. Use this if you've mucked everything up and just want to start again.")
    args = parser.parse_args()
    if args.play:
        #load up the current scenario, then check if it's done,
        #if it's done, print that done message, then update the current scenario
        pass


    #need to store the current state somewhere.
    #like in some file that has hte mission and the current scenario
