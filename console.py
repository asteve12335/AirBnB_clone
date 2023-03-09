#!/usr/bin/python3
"""Module for the entry point of the command interpreter"""

import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """
        Creates a BaseModel instance,
        saves it (to the JSON file)
        and prints the id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all([key]))

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
