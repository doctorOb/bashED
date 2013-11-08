import os.path
import filecmp

SANDBOX_DIR = os.path.join("bashED", "sandbox")
SCENARIO_DIR = os.path.join("bashED", "scenarios")


def dir_exists(path):
    return os.path.isdir(os.path.join(SANDBOX_DIR, path))


def file_exists(path):
    return os.path.isfile(os.path.join(SANDBOX_DIR, path))


def file_matches(attempt, goal, scenario):
    """returns true if the attempt file matches the goal file for the scenario

    Args:
        attempt: path of the attempt file (relative to the sandbox)
        goal: path of the goal file (relative to the particular scenario)
        scenario: the name of the scenario

    Returns:
        True if the goal matches the attempt(and both exist), else False.
    """
    if os.path.isfile(os.path.join(SCENARIO_DIR, scenario, goal)) and os.path.isfile(os.path.join(SANDBOX_DIR, attempt)):
        return filecmp.cmp(os.path.join(SCENARIO_DIR, scenario, goal), os.path.join(SANDBOX_DIR, attempt))
    return False


def prompt(message, goal):
    return raw_input(message) == goal


if __name__ == '__main__':
    print dir_exists("durr")
    print file_exists("test_file.txt")
    print file_matches("test_file.txt", "test_file.txt", "test_scenario")
