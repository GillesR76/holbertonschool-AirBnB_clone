#!/usr/bin/python3
"""This is a new module"""
import cmd
from models.base_model import BaseModel
from models import storage


class MyCmd(cmd.Cmd):
    """This is a new module"""

    def preloop(self):
        """To display a prompt"""
        self.prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True

    def emptyline(self):
        """Defines what to do when there is no input"""
        pass

    def do_help(self, arg):
        """do_help function displays documantation"""
        words = "Documented commands (type help <topic>):"
        if arg:
            super().do_help(arg)
        else:
            print("\n{}".format(words), end='\n')
            print('=' * len(words), end='\n')
            for command in self.get_names():
                if command.startswith("do_"):
                    print("{}".format(command[3:]), end=" ")
            print("\n")

    def do_EOF(self, line):
        """To quit the program"""
        raise EOFError

    def do_create(self, arg):
        """To create a new instance of the class BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] is not "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """To print the string representation of an instance based
        on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] is not "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for dict in objs:
                if "id" in objs.keys and dict["id"] == args[1]:
                    instance = BaseModel(**dict)
                    print(instance)
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        from models.base_model import BaseModel
        from models.user import User
        a_classes = {'BaseModel': BaseModel, 'User': User}
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in a_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_id = args[1]
            obj_key = f"{class_name}.{class_id}"
            inst_keys = storage.all().keys()
            if obj_key not in inst_keys:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            obj = eval(class_name)(**storage.all()[obj_key])
            if hasattr(obj, attr_name):
                type_name = type(attr_name)
                attr_value = type_name(args[3])
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    try:
        MyCmd().cmdloop()
    except (KeyboardInterrupt, EOFError):
        pass
