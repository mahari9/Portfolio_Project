#!/usr/bin/python3

"""This module defines the entry point of the command interpreter/Console:
   Which ables to manage the objects of our Easy Freight project.
"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.carrier import Carrier
from models.user import User
from models.vehicle import Vehicle
import shlex 

classes = {"User": User,
           "Carrier": Carrier,
           "BaseModel": BaseModel,
           "Vehicle": Vehicle}


class FreightCommand(cmd.Cmd):
    """Command interpreter/Console for Easy Freight"""
    prompt = '(easy-freight) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self, arg):
        """Overwriting the emptyline method"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """Creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class (User, Shipment, Offer, Vehicle)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
            instance.save()
            print(f"{args[0]} created: {instance.id}")
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                instance = models.storage.get(classes[args[0]], args[1])
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                instance = models.storage.get(classes[args[0]], args[1])
                if instance:
                    models.storage.delete(instance)
                    models.storage.save()
                    print(f"{args[0]} deleted.")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for instance in obj_dict.values():
            obj_list.append(str(instance))
        print("[", end="")
        print(", ".join(obj_list), end="")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        floats = ["price_per_km"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Vehicle":
                                if args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
            

if __name__ == '__main__':
    FreightCommand().cmdloop()
