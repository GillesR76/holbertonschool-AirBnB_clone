#!/usr/bin/python3
"""This is a new module"""
import cmd
from models.base_model import BaseModel


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
    
    def do_create(self, line):
        """It creates and Serialize"""
        a_classes = ["BaseModel"]
        if line.split()[0] in a_classes:
            obj = BaseModel()
            obj.save()
            print("{}".format(obj.id))    
        elif not line.split()[0] in a_classes:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show command"""
        pass

    def do_destroy(self, line):
        """destroy command"""
        a_

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
