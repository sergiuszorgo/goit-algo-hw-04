contacts = {}

def parse_input(user_input: str):
	parts = user_input.strip().split()
	command = parts[0].lower() if parts else ""
	args = parts[1:]
	return command, args

def add_contact(name: str, phone: str):
	contacts[name] = phone
	print("Contact added.")

def change_contact(name: str, phone: str):
	if name in contacts:
		contacts[name] = phone
		print("Contact updated.")
	else:
		print("Contact not found.")

def show_phone(name: str):
	if name in contacts:
		print(contacts[name])
	else:
		print("Contact not found.")

def show_all():
	if contacts:
		for name, phone in contacts.items():
			print(f"{name}: {phone}")
	else:
		print("No contacts saved.")

def main():
	print("Welcome to the assistant bot!")
	while True:
		user_input = input("Enter a command: ")
		command, args = parse_input(user_input)

		if command in ["close", "exit"]:
			print("Good bye!")
			break

		elif command == "hello":
			print("How can I help you?")

		elif command == "add":
			if len(args) == 2:
				add_contact(args[0], args[1])
			else:
				print("Usage: add [name] [phone]")

		elif command == "change":
			if len(args) == 2:
				change_contact(args[0], args[1])
			else:
				print("Usage: change [name] [new phone]")

		elif command == "phone":
			if len(args) == 1:
				show_phone(args[0])
			else:
				print("Usage: phone [name]")

		elif command == "all":
			show_all()

		else:
			print("Invalid command.")

if __name__ == "__main__":
	main()