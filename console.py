#!/usr/bin/python3
"""
 Program that contains the entry point of the command interpreter
"""

import cmd
import shlex
import re
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter implementation
    """
    prompt = '(hbnb) '
    classes = storage.class_dict()

    def do_create(self, arg):
        """
        Create command to create a new instance according Class name.
        Print the assigned id.
        Usage: create <class name>
        Classes: [BaseModel, User, Place, State, City, Amenity, Review]
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.classes[arg]()
            new.save()
            print(new.id)

    def do_update(self, arg):
        """
        Update command to update an instance based on the class name and id
        by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        inputs = shlex.split(arg)
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif len(inputs) < 3:
            print("** attribute name missing **")
        elif len(inputs) < 4:
            print("** value missing **")
        else:
            class_name = inputs[0]
            obj_id = inputs[1]
            attribute = inputs[2]
            obj_key = "{}.{}".format(class_name, obj_id)
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                try:
                    cast = type(getattr(storage.all()[obj_key], attribute))
                except AttributeError:
                    cast = type(inputs[3])
                # open to any attr, even those which are not defined
                value = cast(inputs[3])
                setattr(storage.all()[obj_key], attribute, value)
                storage.all()[obj_key].save()

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>
        """
        inputs = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(inputs[0], inputs[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[obj_key])

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        inputs = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(inputs[0], inputs[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[obj_key]
                storage.save()

    def do_all(self, arg):
        """
        All command to print all string representation of all instances
        based or not on the class name.
        Usage: all <class name (optional)>
        E.g. all               ---- Prints all instances
             all User          ---- Prints User instances
        """
        inputs = arg.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            if inputs[0] in HBNBCommand.classes:
                print([str(obj) for obj in objs.values()
                       if type(obj).__name__ == arg])
            else:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to quit and exit the program by EOF (CTRL+D).
        """
        return True

    def emptyline(self):
        """
        This command replaces default emptyline(), with
        an empty line + ENTER shouldn’t execute anything.
        """
        return False

    def count(self, arg):
        """
        Count command to retrieve the number of instances of a class.
        Usage: <class name>.count()
        """
        if arg in HBNBCommand.classes:
            c = 0
            for obj in storage.all().values():
                c += 1 if obj.__class__.__name__ == arg else 0
            print(c)
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """Executes line when it does not match any class command
        Arg <string>: <class name>.command("optional parameters")
        E.g. User.count()   --- <cls>.count() Must be used without parameters
             User.all()     --- <cls>.all() Must be used without parameters
             User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
             User.update("38f22813-2753-4d42-b37c-57a17f1e4f88",
                            {'first_name': "John", "age": 89})
        """
        met_rgx = re.search(r"^(\w+)\.(\w+)\(\)$", arg)
        arg_rgx = re.search(r"^(\w+)\.(\w+)\(([^)]+)\)$", arg)
        dic_rgx = re.search(r"^(\w+)\.(\w+)\(([^)]+)\,\s+(\{[^)]+\})\)$", arg)

        if met_rgx:
            # For methods self.count() and self.do_all()
            class_name = met_rgx.group(1)
            command = met_rgx.group(2)
            if command == 'all':
                self.do_all(class_name)
            elif command == 'count':
                self.count(class_name)
        elif dic_rgx:
            # Update instance's values from dictionary through console
            command = dic_rgx.group(2)
            class_name = dic_rgx.group(1)
            obj_id = dic_rgx.group(3).replace('"', '')
            try:
                obj_dic = json.loads(dic_rgx.group(4).replace("'", '"'))
            except Exception:
                print("** value missing **")
                return
            if class_name in HBNBCommand.classes and command == 'update':
                for key, value in obj_dic.items():
                    # 'line': input to execute through console onecmd method
                    line = '{} {} {} {} "{}"'.format(
                            command, class_name, obj_id, key, str(value))
                    self.onecmd(line)
            else:
                print("** class name missing **")
        elif arg_rgx:
            # Commands with arguments
            command = arg_rgx.group(2)
            class_name = arg_rgx.group(1)
            arguments = arg_rgx.group(3).replace(',', '')
            args_ls = shlex.split(arguments)
            # 'line': input to execute through console with onecmd command
            if command == 'update':
                try:
                    attribute = args_ls[1]
                    value = args_ls[2]
                except Exception:
                    print("** Attribute or Value missing **")
                    return
                line = '{} {} {} {} "{}"'.format(
                        command, class_name, args_ls[0], attribute, str(value))
            else:
                line = "{} {} {}".format(command, class_name, args_ls[0])
            # print("Line --->", line)
            self.onecmd(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
