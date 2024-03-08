#!/usr/bin/python3
"""This is a new module"""
import cmd
from models import storage


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
        from models.base_model import  BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                    "City" : City, "Amenity" : Amenity, "Place": Place,
                    "Review" : Review}
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in a_classes:
            print("** class doesn't exist **")
        else:
            new_instance = a_classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """To print the string representation of an instance based
        on the class name and id"""
        from models.base_model import  BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                    "City" : City, "Amenity" : Amenity, "Place": Place,
                    "Review" : Review}
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in a_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            objs = storage.all()
            for obj in objs.values():
                if obj.to_dict()["id"] == args[1]:
                    obj_dict = obj.to_dict()
                    obj_dict.pop('__class__')
                    instance = eval(args[0])(**obj_dict)
                    print(str(instance))
                    return
                else:
                    print("** no instance found **")
                    return

    def do_destroy(self, line):
        """destroy command"""
        from models.base_model import  BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        args = line.split()

        a_classes = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                    "City" : City, "Amenity" : Amenity, "Place": Place,
                    "Review" : Review}
        obj_key = args[0] + '.' + args[1]
        if len(args) < 1:
            print("** class name missing **")
            return
        elif not args[0] in a_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif  obj_key not in storage.all().keys():
                print("** no instance found **")
                return
        else:
            storage.all().pop(obj_key)
            storage.save()

    def do_all(self, line):
        """all command"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                    "City" : City, "Amenity" : Amenity, "Place": Place,
                    "Review" : Review}
        args = line.split()

        if len(args) == 1:
            class_name = args[0]
            if class_name not in a_classes:
                print("** class doesn't exist **")
                return
            
            objects = storage.all().values()
            result = []
            class_inst = eval(class_name)
            for obj in objects:
                if isinstance(obj, class_inst):
                    result.append(str(str(obj)))

            if len(result) != 0:
                print(result)
            else:
                print("** no instance found **")
        else:
            objects = storage.all().values()
            _list = []
            for obj in objects:
                _list.append(str(str(obj)))
            print(_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel" : BaseModel, "User" : User, "State" : State,
                    "City" : City, "Amenity" : Amenity, "Place": Place,
                    "Review" : Review}
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
            
            if arg[2] in ['id', 'created_at', 'updated_at']:
                return

            attr_name = args[2]
            attr_value = args[3]
            obj_dict = storage.all()[obj_key].to_dict()
            obj_dict.pop("__class__")
            obj = eval(class_name)(**obj_dict)
            if hasattr(obj, attr_name):
                type_name = type(attr_name)
                attr_value = type_name(args[3])
            setattr(obj, attr_name, attr_value)
            storage.all()[obj_key] = obj
            obj.save()


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except (KeyboardInterrupt, EOFError):
        pass
