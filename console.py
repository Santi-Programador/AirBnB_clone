#!/usr/bin/python3
"""
 Program that contains the entry point of the command interpreter
"""

import cmd
import shlex
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
            # print("-----", dir(storage.all()[obj_key]))
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                try:
                    cast = type(getattr(storage.all()[obj_key], attribute))
                    print("-------", cast)
                except AttributeError:
                    cast = type(inputs[3])
                # check all this if checker does not pass :c
                if attribute in dir(storage.all()[obj_key]):
                    value = cast(inputs[3])
                    setattr(storage.all()[obj_key], attribute, value)
                    storage.all()[obj_key].save()
                else:
                    return  # Attribute does not exist!

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
        Ex: all               ---- Prints all instances
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
