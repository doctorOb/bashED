BashED
=========

BashED is a fun way for new computer programmers to learn and interact with terminal windows. The bash window can be very intimidating for new people. BashED players have to solve simple puzzles by using the bash command set. For example, the first few puzzles ask the user to navigate to a directory, and submit the name of the only file that exists there. The program is built to make learning bash fun and easy. By the end of the puzzle sets, players will know how to navigate, search, and manipulate theirs files through terminal windows.


There are only three commands you have to use in order to be off on your way to learning! play, hint, reset!

Run this to play from the terminal:

```bash
python bashed_run.py --play
```

Run this when you get stuck and need a hint:

```bash
python bashed_run.py --hint
````

Run this if you REALLY messed up and need to reset everything:

```bash
pyhton bashed_run.py --reset
```

For users already proficient in using the terminal, they can easily add their own tasks to missions! Steps:
# create a folder in bashED/missions/<some_mission>/scenarios/, for example, you might call it "new_task"
# add "new task to the list bashED/mission/<some_mission>/scenario_order.txt
# in your new_task folder, add a folder setup which contains the files your task has to add to setup the sandbox
# finally, make a subclass of base_scenario, (called Scenario) and define your own strings representing the messages, tasks, and verification conditions!

Have fun, and hopefully this makes the unix command line interface much less terrifying!
