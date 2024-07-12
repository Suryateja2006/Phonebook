contacts = []

while True:
    print("Enter 1 for adding a contact")
    print("Enter 2 for viewing contact list")
    print("Enter 3 for searching a contact")
    print("Enter 4 for updating the contact list")
    print("Enter 5 for deleting a contact")
    print("Enter 6 for Exiting...")
    
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        name = input("Enter name: ")
        phno = input("Enter contact no.: ")
        email = input("Enter email id: ")
        address = input("Enter address: ")
        contact = {"name": name, "phno": phno, "email": email, "address": address}
        contacts.append(contact)
        print("Contact added successfully!")
        print("\n\n\n")
        
    elif choice == 2:
        if contacts:
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phno']}")
        else:
            print("No contacts found.")
        print("\n\n\n")
        
    elif choice == 3:
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if search.lower() in contact["name"].lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phno']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                found = True
                break
        if not found:
            print("Contact not found.")
        print("\n\n\n")
        
    elif choice == 4:
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if search.lower() in contact["name"].lower():
                contact["name"] = input("Enter new name: ")
                contact["phno"] = input("Enter new phone number: ")
                contact["email"] = input("Enter new email id: ")
                contact["address"] = input("Enter new address: ")
                print("Contact updated successfully.")
                found = True
                break
        if not found:
            print("No such contact found.")
        print("\n\n\n")
        
    elif choice == 5:
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if search.lower() in contact["name"].lower():
                contacts.remove(contact)
                print("Deleted the contact successfully.")
                found = True
                break
        if not found:
            print("No such contact found.")
        print("\n\n\n")
        
    elif choice == 6:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice.")
        print("\n\n\n")
