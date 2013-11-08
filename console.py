import os
import cmd
import readline

DIR_SPECIALS = ['cd','pushd','popd']
SHELL_START = ' $: '
SHOW_ERROR = False



def error(msg):
    """if verbosity is turned on, log the error to the console, else do nothing"""
    if SHOW_ERROR:
        print(msg)



class BashED_Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = os.getcwd() + SHELL_START
        self.intro  = "Welcome to console!"  ## defaults to None
        self._root = os.getcwd()
        self._specials = {
            'cd' : self.chdir,
            'pushd' : self.pushd,
            'popd' : self.popd
        }

    def get_command(self,line):
        """get the command (arg[0]) from a input line, and return it"""
        if ' ' in line:
            return line[0:line.index(' ')]
        else:
            return line

    def get_path(self,line):
        """given a line (assumed to contain a cd command) return the path argument given."""
        try:
            path = line[line.index(' ')+1:]
        except:
            path = line

        return path

    def update_prompt(self):
        self.prompt = os.getcwd() + SHELL_START

    def get_hist(self, args):
        """return a list of commands that have been entered"""
        return self._hist

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    def completedefault(self, text, line, start_index, end_index):
        """auto complete as the shell would (for file names in current directory)"""

        if self.get_command(line) in self._specials.keys():
            path = self.get_path(line)
            try:
                os.listdir(path)
                search_dir = path
            except:
                search_dir = path[0:path.rindex('/')] if '/' in path else path

            text = text[text.rindex('/'):] if '/' in text else text
        else:
            search_dir = os.getcwd()

        return [x for x in os.listdir(search_dir) if x.startswith(text)]

    ## Override methods in Cmd object ##
    def preloop(self):
        """hook called before loop begins. Sets up buffers and hash maps to hold stuff needed to be persistent"""
        cmd.Cmd.preloop(self)   ## sets up command completion
        self._hist    = []      ## No history yet
        self._locals  = {}      ## Initialize execution namespace for user
        self._globals = {}
        self._dstack = [] ## stack used to hold directories for pushd and popd


    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)   ## Clean up command completion
        print "Exiting..."

    def precmd(self, line):
        """hook that gets called before the cmd is actually processed. Can manipulate the line as desired before passing it on"""
        self._hist += [ line.strip() ]


        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop

    def emptyline(self):    
        pass

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
        try:
            d = self._dstack.pop()
            self.chdir(d)
        except:
            error('popd error')

    def default(self, line):       
        """called when the command is not recognized as one of those defined above. 
        self.do_shell(line)"""
        shell_cmd = self.get_command(line)
        if shell_cmd in self._specials.keys():
            self._specials[shell_cmd](line)
        else:
            self.do_shell(line)

if __name__ == '__main__':
    console = BashED_Console()
    console.cmdloop() 
