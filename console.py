#!/usr/bin/python3

""" Console for the freight website """

import cmd
from datetime import datetime
from models import storage
from models.shipment import Shipment
from models.offer import Offer
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Shipment": Shipment, "Offer": Offer, "User": User}


class FreightCommand(cmd.Cmd):
    """ Freight console """
    prompt = '(freight) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self, arg):
        """ Overwriting the emptyline method """
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
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    # Create commands for Shipment model

    def do_create_shipment(self, arg):
        """Creates a new shipment"""
        args = arg.split()
        if not args:
            print("** shipment details missing **")
            return
        new_dict = self._key_value_parser(args)
        user_id = new_dict.pop('user_id', None)  # Extract and validate user_id
        if not user_id:
            print("** user_id is required **")
            return
        if not storage.get(User, user_id):
            print("** Invalid user_id provided **")
            return
        shipment = Shipment(**new_dict)
        shipment.user_id = user_id
        shipment.save()
        print(f"Shipment created: {shipment.id}")

    def do_show_shipment(self, arg):
        """Shows a shipment based on its ID"""
        shipment = storage.get(Shipment, arg)
        if not shipment:
            print("** Shipment not found **")
            return
        print(shipment)

    def do_all_shipments(self, arg):
        """Prints all shipments"""
        shipments = storage.all(Shipment)
        if not shipments:
            print("** No shipments found **")
            return
        print("[", end="")
        print(", ".join(str(shipment) for shipment in shipments), end="")
        print("]")

    def do_update_shipment(self, arg):
        """Updates a shipment based on its ID and attributes"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** Insufficient arguments **")
            return
        shipment_id = args[0]
        shipment = storage.get(Shipment, shipment_id)
        if not shipment:
            print("** Shipment not found **")
            return
        for attr, value in zip(args[1::2], args[2::2]):
            if not hasattr(shipment, attr):
                print(f"** Invalid attribute: {attr} **")
                continue
            setattr(shipment, attr, value)
        shipment.save()
        print(f"Shipment {shipment_id} updated")

    def do_destroy_shipment(self, arg):
        """Deletes a shipment based on its ID"""
        shipment = storage.get(Shipment, arg)
        if not shipment:
            print("** Shipment not found **")
            return
        storage.delete(shipment)
        storage.save()
        print(f"Shipment {arg} deleted")

    # Create commands for Offer model (similar structure as Shipment)

    def do_create_offer(self, arg):
        """Creates a new offer for a shipment"""
        # ... (implement similar logic as create_shipment)
