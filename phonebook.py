import sys

# Phonebook class
class Phonebook:
	def __init__(self):
		self.contacts = {}

	# adds a new contact to the dictionary
	def add_contact(self, name, number, **kwargs):
		self.contacts[name] = {"Number": number, "Email": kwargs.get("email"), "Category": kwargs.get("category")}
		print(f"\n*******{name} has been added successfully!*******")


	def delete_contact(self, name):
		print("\n*******")
		if name in self.contacts:
			del self.contacts[name]
			print(f"\n{name} has been deleted successfully!")
		else:
			print(f"\n{name} not found in the Phonebook\n*******")


	# searches for contacts that contains the specified string
	def search_contact(self, name):
		print("\n*******")
		for key, value in self.contacts.items():
			if name.lower() in key.lower():
				print(f"Name: {key}", end="\t")
				for k, v in value.items():
					print(f"{k}: {v}\t", end="\t")	
			print()			


	def display_all_contacts(self):
		print("\n*******\nAll Contacts\n*******\n")
		if self.contacts:
			for name, number in self.contacts.items():
				print(f"Name: {name}", end="\t")
				for k, v in number.items():
					print(f"{k}: {v}\t", end="\t")
				print()
		else:
			print("\n*******Phonebook is empty!!!\n*******")

	def edit_contact(self, name):
		print("\n*******")
		if name.title() in self.contacts:
			new_name = input("To change the current name, type a new name: ")
			new_number = input("To change the current number, type a new number: ")
			new_email = input("To change the current email, type a new email: ")
			new_category = input("To change the current category, type a new category: ")

			# if a new_* is not supplied, then we update it to the value of the previous one
			if not new_name:
				new_name = self.contacts.keys().get(name)
			if not new_number:
				var = self.contacts.values()
				new_number = var["Number"]
			if not new_email:
				var = self.contacts.values()
				new_email = var["Email"]
			if not new_category:
				var = self.contacts.values()
				new_name = var["Category"]

			del self.contacts[name]
			self.contacts[new_name] = {"Number": new_number, "Email": new_email, "Category": new_category}
		else:
			print(f"{name} not found in the Phonebook")




# an object
# figure out a way to ensure that only a single phonebook object can be made from it...
phonebook = Phonebook()


# ensures a value is supplied 
def valid(value):
	while True:
		if not value:
			value = input(f"{value}")
		else:
			break


# carries out the user's choice
def action(flag):
	if flag == "add":
		name = input("Name: ").strip().title()
		# name = valid(name)
		number = input("Number: ").strip()
		# valid(number)
		email = input("Email (If not available, input N/A): ").strip().lower()
		category = input("Category (If not available, input N/A): ").strip().title()
		phonebook.add_contact(name, number, email=email, category=category)

	elif flag == "delete":
		name = input("Name: ").strip().title()
		phonebook.delete_contact(name)

	elif flag == "search":
		name = input("Name: ").strip().title()
		phonebook.search_contact(name)

	elif flag == "display_all":
		phonebook.display_all_contacts()

	elif flag == "edit":
		name = input("Name: ").strip().title()
		phonebook.edit_contact(name)

	elif flag == "exit":
		sys.exit("Exiting the Phonebook System...")

	else:
		sys.exit("...")


# driver code
def main():
	userChoiceMap = {
		1: "add",
		2: "delete",
		3: "search",
		4: "display_all",
		5: "edit",
		6: "exit"
	}
	# checks for command-line args
	if len(sys.argv) == 2:
		action(sys.argv[1].lower())

	while True:
		print("\n*******Phonebook System*******")
		print("\n1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Display All Contacts\n5. Edit\n6. Exit")

		# ensures that the correct input is supplied
		try:
			user_choice = int(input("\nEnter your choice: "))
			if user_choice < 1 or user_choice > 6:
				raise ValueError("\nInput an integer between 1 and 5a")
			else:
				action(userChoiceMap.get(user_choice))
		except ValueError:
			print("\nInput an integer between 1 and 5b")


if __name__ == "__main__":
	main()

