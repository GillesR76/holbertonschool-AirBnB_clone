#!/usr/bin/python3
"""This is a new module"""
import cmd
from models import storage
from models.base_model import BaseModel
from values import a_classes


class  HBNBCommand(cmd.Cmd):
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
        elif args[0] is not a_classes:
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

    def do_destroy(self, line):
        """destroy command"""
        if len(line.split()) == 0:
            print("** class name missing **")
        elif not line.split()[0] in a_classes:
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        else:
            save_dict = {}
            for obj_dict in storage.all():
                if "id" in obj_dict.keys() and obj_dict["id"] == line.split()[1]:
                    storage.pop("{}.{}".format(obj_dict["class"], obj_dict["id"]))
                    break
                else:
                    continue
                print("** no instance found **")

    def do_all(self, line):
        """all command"""
        pass

    def do_update(self, line):
        """update command"""
        pass




if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except (KeyboardInterrupt, EOFError):
        pass
