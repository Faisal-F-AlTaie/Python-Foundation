# Project Requirments:
# 1. Be able to add a new contact
# 2. View All conatcts
# 3. Search for contact by name
# 4. Delete a contact

contacts = []

def display_options():
    print("Welcome to the contact managment system")
    print("1. Add New Contact")
    print("1. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact has now been added to the data base :)")
    
def view_contacts():
    if not contacts:
        print("Sorry no conatcts were found in our data base")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        
def search_contact():
    name = input("Enter the name to serach data base: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found.")
        
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        display_options()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
