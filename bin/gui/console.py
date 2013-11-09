import os
import cmd
import sys
import subprocess

sys.path.append(os.path.abspath('../../'))
print sys.path

#import bashed_run


DIR_SPECIALS = ['cd','pushd','popd']
SHELL_START = ' $: '
SHOW_ERROR = True
BASHED = os.getcwd() + '/' + 'bashed_run.py'
DELIM = '[]'


def error(msg):
    """if verbosity is turned on, log the error to the console, else do nothing"""
    if SHOW_ERROR:
        print(msg)



class BashED_Console(cmd.Cmd):

    def __init__(self,stdin=None,stdout=None):
        cmd.Cmd.__init__(self,stdin=stdin,stdout=stdout)
        self.intro  = "Welcome to console!"  ## defaults to None
        self._root = os.path.abspath('../../../')
        self.prompt = self._root + SHELL_START
        self.stdout = stdout
        self._specials = {
            'cd' : self.chdir,
            'pushd' : self.pushd,
            'popd' : self.popd
        }
        self.preloop()

    def get_command(self,line):
        """get the command (arg[0]) from a input line, and return it"""
        if ' ' in line:
            return line[0:line.index(' ')].strip()
        else:
            return line

    def get_path(self,line):
        """given a line (assumed to contain a cd command) return the path argument given."""
        try:
            path = line[line.index(' ')+1:]
        except:
            path = line

        return path

    def closest_path(self,path):
        """given a potential path (such as /root/sys/almostaname), finds the closest directory in the tree"""
        path = os.path.abspath(path)
        while not os.path.isdir(path):
            try:
                path = path[0:path.rindex('/')]
            except:
                break

        return path


    def update_prompt(self):
        self.prompt = os.getcwd() + SHELL_START

    def get_prompt(self):
        self.update_prompt()
        return self.prompt.replace(self._root,'')

    def get_hist(self, args):
        """return a list of commands that have been entered"""
        return self._hist

    def next_hist(self):
        """traverse the history list to an earlier entry"""
        if len(self._hist)-1 > self._histidx+1:
            hist = self._hist[self._histidx+1]
            self._histidx+=1
        else:
            self._histidx = len(self._hist) - 1
            hist = self._hist[self._histidx]

        return hist

    def last_hist(self):
        """traverse the history list to a later entry"""

        if self._histidx-1 > 0:
            hist = self._hist[self._histidx-1]
            self._histidx-=1
        else:
            hist = self._hist[self._histidx]
            self._histidx = 0
        return hist

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        raw = ''
        for arg in args:
            raw += arg
        proc = subprocess.Popen(raw,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out,err = proc.communicate()
        print out,err


  

    def do_play(self,args):
        """calls the play script from the head game file"""
        #bashed_run.play()
        proc = subprocess.Popen(BASHED + ' --play',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out,err = proc.communicate()
        dialog = ''

        print(out,err)

        if err:
            print err
            return "Aye! looks like you got a shell error there!"

        for line in out:
            dialog+=line.replace('\\','')

        return dialog


    def do_reset(self,args):
        """resets the game state"""
        proc = subprocess.Popen(BASHED + ' --reset',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out,err = proc.communicate()

    def do_hint(self,args):
        """gives a scenario specific hint to the user"""
        proc = subprocess.Popen(BASHED + ' --hint',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out,err = proc.communicate()



    ## Override methods in Cmd object ##
    def preloop(self):
        """hook called before loop begins. Sets up buffers and hash maps to hold stuff needed to be persistent"""
        cmd.Cmd.preloop(self)   ## sets up command completion
        self._hist    = []      ## No history yet
        self._locals  = {}      ## Initialize execution namespace for user
        self._globals = {}
        self._dstack = [] ## stack used to hold directories for pushd and popd
        self._histidx = -1

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)   ## Clean up command completion
        print "Exiting..."

    def precmd(self, line):
        """hook that gets called before the cmd is actually processed. Can manipulate the line as desired before passing it on"""
        self._hist.insert(0,line.strip())
        self._histidx = -1

        for part in line.split(' '):
            if len(part) < 1:
                pass
            path = self.closest_path(part)
            if self._root not in os.path.abspath(part): 
                error('cant venture out of bounds')
                return ''

        return line

    def emptyline(self):    
        pass #default is to reenter most recent command. This overrides it.

    def chdir(self,line):
        """interpret the input line as a cd command, and perform the neccessary directory walking actions"""
        path = self.get_path(line)
        try:
            os.chdir(path)
            self.update_prompt()
        except:
            error('cd error') 

    def pushd(self,line):
        """interpret the input line as the pushd command. Move the user to the directory, and push the previous one onto the dstack."""
        self._dstack.insert(0,os.getcwd())
        self.chdir(line)

    def popd(self,line):
        """perform the popd command, and return to the directory at the top of the dstack (if one exists)"""
        try:
            d = self._dstack.pop()
            self.chdir(d)
        except:
            error('popd error')

    def completedefault(self, text, line, start_index, end_index):
        """auto complete as the shell would (for file names in current directory)"""
        if self.get_command(line) in self._specials.keys():
            search_dir = self.closest_path(self.get_path(line))
        else:
            search_dir = os.getcwd()

        matches = [x for x in os.listdir(search_dir) if x.startswith(text)]

        if len(matches) == 1: #just one, auto complete and fill in command name
            return [line.replace(text,'') + matches[0]]
        elif len(matches) > 1:
            return matches
        else:
            return []

    def tabcomplete(self,line):
        try:
            last = line.split(' ')
            last = last[len(last) - 1]
        except:
            last = line

        return self.completedefault(last,line,0,0)



    def default(self, line):       
        """called when the command is not recognized as one of those defined above. 
        self.do_shell(line)"""
        if not self.precmd(line):
            print 'fuck'
        shell_cmd = self.get_command(line)
        if shell_cmd in self._specials.keys():
            self._specials[shell_cmd](line)
        else:
            self.do_shell(line)

