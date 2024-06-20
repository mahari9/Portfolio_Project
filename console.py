#!/usr/bin/python3

"""This module defines the entry point of the command interpreter/Console:
   Which ables to manage the objects of our Easy Freight project.
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.shipment import Shipment
from models.offer import Offer
from models.vehicle import Vehicle
import shlex  # for splitting the line along spaces except in double quotes

classes = {"User": User,
           "BaseModel": BaseModel,
           "Shipment": Shipment,
           "Offer": Offer,
           "Vehicle": Vehicle}


class FreightCommand(cmd.Cmd):
    """Commmand interpreter/Console for Easy Freight"""
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
