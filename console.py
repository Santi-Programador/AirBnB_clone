#!/usr/bin/python3
"""
 Program that contains the entry point of the command interpreter
"""

import cmd
import shlex
import re
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
            obj_cls = inputs[0]
            obj_id = inputs[1]
            attribute = inputs[2]
            obj_key = "{}.{}".format(obj_cls, obj_id)
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
        based on the class name and id
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
        This method replaces default emptyline(), with
        an empty line + ENTER shouldn’t execute anything
        """
        return False

    def count(self, arg):
        """
        Count command to retrieve the number of instances of a class
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
        """Executes line when it does not match with any class method
        Arg <string>: <class name>.method("optional parameters")
        E.g. User.count()   --- <cls>.count() Must be used without parameters
             User.all()     --- <cls>.all() Must be used without parameters
             User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
        """
        s_rgx = re.search(r"^(\w+)\.(\w+)\(\)$", arg)
        a_rgx = re.search(r"^(\w+)\.(\w+)\(([^)]+)\)$", arg)
        if s_rgx:
            cls_arg = s_rgx.group(1)
            fnc_arg = s_rgx.group(2)
            if fnc_arg == 'all':
                self.do_all(cls_arg)
            elif fnc_arg == 'count':
                self.count(cls_arg)
        elif a_rgx:
            # print("----arg---->", arg)
            a = arg.replace('.', ',', 1)
            args_ls = re.split('[()",]', a)
            lst = [i for i in args_ls if i and i != ' ']
            lst[0], lst[1] = lst[1], lst[0]
            if lst[0] == 'update':  # update should be fixed
                line = " ".join(lst[0:-1]) + " " + "'" + lst[-1] + "'"
            else:
                line = " ".join(lst)
            # print("-------->", line)
            self.onecmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
