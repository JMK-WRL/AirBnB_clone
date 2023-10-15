#!/usr/bin/python3
"""The console"""

import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class represents the command interpreter.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, line):
        """
        Create a new instance of BaseModel, save it to the JSON file.

        Usage: create <class name>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Print the string representation of an instance.

        Usage: show <class name> <id>
        """
        args = shlex.split(line)
        objdict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objdict:
                print(objdict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = shlex.split(line)
        objdict = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in objdict:
                del objdict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representations of instances.

        Usage: all [<class name>]
        """
        args = shlex.split(line)
        objdict = storage.all()
        obj_list = []

        if not args:
            for obj_id, obj in objdict.items():
                obj_list.append(str(obj))
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            for obj_id, obj in objdict.items():
                if obj_id.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """
        Update an instance based on the class name and id

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(line)
        objdict = storage.all()

        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in objdict:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = objdict[key]
        attribute_name = args[2]
        attribute_value = args[3].strip('"')
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_EOF(self, args):
        """
        Quit the program.

        Usage: EOF
        """
        return True

    def do_quit(self, args):
        """
        Quit the program.

        Usage: quit
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
