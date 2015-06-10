# module for haneling command-line experiences
import cmd

# needed for running ks code
from definition.ksparser import parser as ksparser
from definition.ksinterpreter import interpret
from definition.ksinterpreter import global_env as ks_global_env
from definition.ksdatatypes import KS_Blank

############  INTERACTIVE MODE DEFINITION  ############

# custom command line handler
class KSInteractiveCMD(cmd.Cmd):
  # Text preceding user-entered code
  prompt = "> "
  command_queue = ""
  
  # Anything entered should be treated like code...
  def default(self, arg):
    """Enter KangaScript code to be evaluated"""
    ## Know what the script is
    # Tack on the latest line
    self.command_queue += arg
    
    # If line ends in an underscore
    if arg[-1] == "_":
      # That signals more is comming.
      self.prompt = ". "
      # Evaluate this later
      self.command_queue = self.command_queue[:-1] + "\n"
      return
    # end if line ends in an underscore
    # Else...
    else:
      ## Evaluate the script
      try:
        res = interpret( ksparser.parse(self.command_queue) , ks_global_env)
        # if printable, print the result
        if res != None and not isinstance(res, KS_Blank):
          # res will be a KS_DataType if anything, so safe to know __string__() is implemented
          print res.__string__()
      except SyntaxError:
        # syntax errors already taken care of by parser
        pass
      # end try-except handeling KangaScript syntax errors
      
      # clean the queue
      self.command_queue = ""
      self.prompt = "> "
    # end else, evaluating the script
  # end overridden member method default()
  
  # ... except the quit command
  def do_quit(self, arg):
    """Exit the interactive interpreter"""
    return True
  # end method do_quit(), responding to 'quit' command
  
  # ... oh, and blank lines too. Make those do nothing
  def emptyline(self):
    """Empty lines do not do anything!"""
    # don't do anything more than's on your plate
    # (empty the queue)
    self.default("\n")
    pass
  # end overridden member method emptyline()
# end subclass definition KSInteractiveCMD

def ks_interactive():
  # go and enter the loop
  try:
    # create new instance of CMD handler and run it until done
    KSInteractiveCMD().cmdloop()
    # exit calmly...
  # or maybe met with keyboard exit (like Ctrl+C)
  except KeyboardInterrupt:
    print("")
    pass
  # all with loop done!
# end function definition ks_interactive

