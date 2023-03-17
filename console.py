#!/usr/bin/python3
""" """

import cmd
import models
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
	""" """
	prompt = "(hbnb) "
	__cls_list = ["BaseModel", "User", "State", "City",
		      "Amenity", "Place", "Review"]
	def do_EOF(self, arg):
		"""method for EOF"""
		print("")
		return True

	def do_quit(self, arg):
		"""method to quit"""
		return True
	
	def do_create(self, arg):
		"""create method"""
		if arg == "":
			print("** class name missing **")
			return False
		
		if arg not in self.__cls_list:
			print("** class doesn't exist **")
			return False
		a = eval(arg)()
		print(a.id)
		storage.save()

	def do_show(self, arg):
		"""show method"""
		if arg == "":
			print("** class name missing **")
		else:
			parts = arg.split()
			if parts[0] not in self.__cls_list:
				print("** class doesn't exist **")
				return False
			if len(parts) < 2:
				print("** instance id missing **")
				return False
			key_val = "{}.{}".format(parts[0], parts[1])
			objdict = storage.all()
			if key_val not in objdict.keys():
				print("** no instance found **")
				return False
			a = eval(parts[0])()
			print(a)

	def do_destroy(self, arg):
		"""destroy method"""
		if arg == "":
			print("** class name missing **")
		else:
			parts = arg.split()
			if parts[0] not in self.__cls_list:
				print("** class doesn't exist **")
				return False
			if len(parts) < 2:
				print("** instance id missing **")
				return False
			key_val = "{}.{}".format(parts[0], parts[1])
			objdict = storage.all()
			if key_val not in objdict.keys():
				print("** no instance found **")
				return False
			del objdict[key_val]
			storage.save()
	def do_all(self, arg):
		"""Print all method"""
		objdict = storage.all()
		my_list = []
#		parts = arg.split()
		if arg == "" or arg in self.__cls_list:
			for value in objdict.values():
				my_list.append(value.__str__())
			print(my_list)
			return
		if arg not in self.__cls_list:
			print("** class doesn't exist **")
			return False
#		for value in objdict.values():
#			if value.__class__.__name__ == parts[0]:
#				my_list.append(value.__str__())
#			print(my_list)

	def do_update(self, arg):
		"""update method"""
		if arg == "":
			print("** class name missing **")
		else:
			parts = arg.split()
			if parts[0] not in self.__cls_list:
				print("** class doesn't exist **")
				return False
			if len(parts) < 2:
				print("** instance id missing **")
				return False
			key_val = "{}.{}".format(parts[0], parts[1])
			objdict = storage.all()
			if key_val not in objdict.keys():
				print("** no instance found **")
				return False
			if len(parts) == 2:
			 	print("** attribute name missing **")
			 	return False
			if len(parts) == 3:
				print("** value missing **")
				return False
			if len(parts) >= 4:
				for key in objdict.keys():
					if key == key_val:
						old_model = objdict[key]
						setattr(old_model, parts[2], parts[3])
						old_model.save()
						storage.reload()
					else:
						pass
    def do_default(self, arg):
        """default method"""
         if arg == "User.all":
              return self.do_all(arg)

if __name__ == '__main__':
	HBNBCommand().cmdloop()
