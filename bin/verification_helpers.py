import os.path
import filecmp

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
BASHED_DIR = os.path.join(THIS_DIR, "..", "bashED")
SANDBOX_DIR = os.path.join(BASHED_DIR, "sandbox")

def dir_exists(path):
    return os.path.isdir(os.path.join(SANDBOX_DIR, path))


def file_exists(path):
    return os.path.isfile(os.path.join(SANDBOX_DIR, path))


def file_matches(attempt, goal):
    """returns true if the attempt file matches the goal file for the scenario

    Args:
        attempt: path of the attempt file (relative to the sandbox)
        goal: path of the goal file full plath, unfortunately, fix this later...

    Returns:
        True if the goal matches the attempt(and both exist), else False.
    """
    print goal
    print os.path.join(SANDBOX_DIR, attempt)
    if os.path.isfile(goal) and os.path.isfile(os.path.join(SANDBOX_DIR, attempt)):
        print 'turns out that they do exist'
        return filecmp.cmp(goal, os.path.join(SANDBOX_DIR, attempt))
    print 'they dont exist'
    return False


def prompt(message, goal):
    return raw_input(message) == goal


if __name__ == '__main__':
    print dir_exists("durr")
    print file_exists("test_file.txt")
    print file_matches("test_file.txt", "test_file.txt", "test_scenario")
