["""KNORFIXX PROPERTY"""]
import sys
from time import sleep
import json


print("Adress Book!\nversion: [1.0]\n")
print("""You can: \n *Add* for adding new contact;\n
					*View* for checking your list of contacts;\n
					*Delete* for deleting one of the contacts from the list;\n
					*Change* for changing contact's information;\n
					""")
contacts = {}
try:
	f = open("data.json", "r")
except FileNotFoundError:
	pass
else:
	data = json.load(f)
	contacts = data.copy()
	f.close()




def del_process():
	quest = str(input("Name of the contact you want to delete: "))
	if quest:
		print("Deleting...")
		contacts.pop(quest)
		sleep(2)
		print("Complete!")
	else: 
		print("Unknown error! Please, try again.")


def change_number():
	name_check = str(input("Which contact you want to change?: "))
	change_number = str(input("New number for the contact [leave for saving previous number]: "))
	if not change_number:
		return
	contacts.update({name_check : change_number})
	print("Changing...")
	sleep(2)
	print("Complete!")


def add():
	name = str(input("Name for a new contact: "))
	number = str(input("Number of the contact: "))
	print("Adding new contact...")
	sleep(2)
	contacts.update({name : number})
	print("Complete!")



while 1:
	quest = ''
	answer = str(input(">>>"))
	if answer.startswith("A"):
		add()
	elif answer.startswith("V"):
		if contacts:
			print("Your list:\n", contacts)
		else:
			print("Your list is empty...")
	elif answer.startswith("C"):
		change_number()
	elif answer.startswith("D"):
		del_process()

	elif answer.startswith("Q"):
		quest = str(input("Do you want to quit? [Y/n]: "))
		if quest:
			if quest.startswith("Y"):
				with open("data.json", "wt") as file:
					json.dump(contacts, file)
				sys.exit("Quitting...")
			elif quest.startswith("N"):
				pass
		else:
			print("Unknown error. Please, try again!")
