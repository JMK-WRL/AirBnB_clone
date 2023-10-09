#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class represents the command line interpreter
    """
    prompt = "(hbnb) "

    def do_quir(self, args):
        """
        Quit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, args):
        """
        Quit the program.
        Usage: EOF
        """
        return True


# Starting the command interpretor and making it loop

if __name__ == '__main__':
    HBNBCommand().cmdloop()
