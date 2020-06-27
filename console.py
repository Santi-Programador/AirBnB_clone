#!/usr/bin/python3
"""
 Program that contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter implementation
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command that exits command interpreter"""
        return True

    def do_EOF(self, arg):
        """Command that exits command interpreter"""
        return True

    def emptyline(self):
        """This method replaces default emptyline(), with
        an empty line + ENTER shouldn’t execute anything"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
