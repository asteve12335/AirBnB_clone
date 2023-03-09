#!/usr/bin/python3
"""Module for the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """handles End Of File character"""
        print()
        return True

    def do_emptyline(self):
        """Doesn't do anything on Enter"""
        pass


if __name__ = '__main__':
    HBNBCommand().cmdloop()
