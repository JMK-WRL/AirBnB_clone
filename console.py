"""The console"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class represents the command interpreter for the AirBnB project.
    """

    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Create a new instance of BaseModel, save it to the JSON file, and print its id.

        Usage: create <class name>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Print the string representation of an instance based on the class name and id.

        Usage: show <class name> <id>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id (save the change into the JSON file).

        Usage: destroy <class name> <id>
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print all string representations of instances based on the class name or all instances.

        Usage: all [<class name>]
        """
        args = shlex.split(line)
        obj_list = []
        if not args:
            for obj_id, obj in storage.all().items():
                obj_list.append(str(obj))
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        else:
            for obj_id, obj in storage.all().items():
                if obj_id.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """
        Update an instance based on the class name and id by adding or updating an attribute
        (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
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
