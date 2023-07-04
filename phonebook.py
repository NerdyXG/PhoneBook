import sys

# Phonebook class
class Phonebook:
	def __init__(self):
		self.contacts = {}

	# adds a new contact to the dictionary
	def add_contact(self, name, number, **kwargs):
		self.contacts[name.title()] = {"Number": number, "Email": kwargs.get("email"), "Category": kwargs.get("category")}
		print(f"\n*******{name} has been added successfully!*******")


	def delete_contact(self, name):
		print("\n*******")
		if name.title() in self.contacts:
			del self.contacts[name.title()]
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
			...




# an object
# figure out a way to ensure that only a single phonebook object can be made from it...
phonebook = Phonebook()


# carries out the user's choice
def action(flag):
	if flag == "add":
		name = input("Name: ")
		number = input("Number: ")
		email = input("Email (If not available, input N/A): ")
		category = input("Category (If not available, input N/A): ")
		phonebook.add_contact(name, number, email=email, category=category)

	elif flag == "delete":
		name = input("Name: ")
		phonebook.delete_contact(name)

	elif flag == "search":
		name = input("Name: ")
		phonebook.search_contact(name)

	elif flag == "display_all":
		phonebook.display_all_contacts()

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
		5: "exit"
	}
	# checks for command-line args
	if len(sys.argv) == 2:
		action(sys.argv[1].lower())

	while True:
		print("\n*******Phonebook System*******")
		print("\n1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Display All Contacts\n5. Exit")

		# ensures that the correct input is supplied
		try:
			user_choice = int(input("\nEnter your choice: "))
			if user_choice < 1 or user_choice > 5:
				raise ValueError("\nInput an integer between 1 and 5a")
			else:
				action(userChoiceMap.get(user_choice))
		except ValueError:
			print("\nInput an integer between 1 and 5b")


if __name__ == "__main__":
	main()

