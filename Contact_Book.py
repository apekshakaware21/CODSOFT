import json
import os

class ContactBook:
    def __init__(self, filename='contacts.json'):
        """
        Initialize the contact book with a filename for storage.
        Load existing contacts from the file if available.
        """
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Load contacts from the JSON file. 
        If the file does not exist, return an empty list.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error reading contacts file. Starting with an empty contact book.")
                return []
        return []

    def save_contacts(self):
        """
        Save the current contact list to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def find_duplicate(self, phone, email, exclude_contact=None):
        """
        Check for duplicate phone numbers and email addresses in the contact list.
        Exclude a specific contact when checking (used during updates).
        """
        duplicate_messages = []

        for contact in self.contacts:
            if contact == exclude_contact:
                continue  # Skip the contact being updated
            if contact['phone'] == phone:
                duplicate_messages.append(f"Phone number '{phone}' already exists.")
            if contact['email'] == email:
                duplicate_messages.append(f"Email '{email}' already exists.")

        # Return combined message if there are duplicates
        return "\n".join(duplicate_messages) if duplicate_messages else None

    def view_contacts(self):
        """
        Display all contacts in the contact book.
        """
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, 1):
                print(f"{index}. Name: {contact['name']}")
                print(f"   Phone: {contact['phone']}")
                print(f"   Email: {contact['email']}")
                print(f"   Address: {contact.get('address', 'Not provided')}")
                print()

    def search_contact(self, query):
        """
        Search for contacts by name.
        Displays all matching results.
        """
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower()]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact.get('address', 'Not provided')}")
                print()
        else:
            print("No matching contacts found.")

    def add_contact(self):
        """
        Add a new contact to the contact book.
        Validates phone and email for duplicates before adding.
        """
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")

        # Check for duplicate phone/email
        duplicate_error = self.find_duplicate(phone, email)
        if duplicate_error:
            print(duplicate_error)
            return

        # Add the new contact
        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")

    def update_contact(self, name):
        """
        Update an existing contact by name.
        Allows updating phone, email, and address while checking for duplicates.
        """
        matches = [contact for contact in self.contacts if contact['name'].lower() == name.lower()]
        if not matches:
            print(f"No contacts found with the name '{name}'.")
            return

        # Show options to select contact
        print("\nMatching Contacts:")
        for index, contact in enumerate(matches, 1):
            print(f"{index}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact.get('address', 'Not provided')}")
            print()

        try:
            choice = int(input("Select the contact number to update (e.g., 1): ")) - 1
            if choice < 0 or choice >= len(matches):
                print("Invalid selection.")
                return
            selected_contact = matches[choice]
        except ValueError:
            print("Please enter a valid number.")
            return

        # Collect updated details
        new_phone = input(f"Enter new phone (or press Enter to keep '{selected_contact['phone']}'): ") or selected_contact['phone']
        new_email = input(f"Enter new email (or press Enter to keep '{selected_contact['email']}'): ") or selected_contact['email']
        new_address = input(f"Enter new address (or press Enter to keep '{selected_contact.get('address', 'Not provided')}'): ") or selected_contact.get('address', '')

        # Check for duplicates
        duplicate_error = self.find_duplicate(new_phone, new_email, exclude_contact=selected_contact)
        if duplicate_error:
            print(duplicate_error)
            return

        # Apply updates
        selected_contact['phone'] = new_phone
        selected_contact['email'] = new_email
        selected_contact['address'] = new_address
        self.save_contacts()
        print(f"Contact '{selected_contact['name']}' updated successfully!")

    def delete_contact(self, query):
        """
        Delete a contact by name.
        Displays matching contacts and allows selection for deletion.
        """
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower()]
        if not results:
            print("No matching contacts found.")
            return

        print("\nMatching Contacts:")
        for index, contact in enumerate(results, 1):
            print(f"{index}. {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact.get('address', 'Not provided')}")
            print()

        try:
            choice = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= choice < len(results):
                contact_to_delete = results[choice]
                self.contacts.remove(contact_to_delete)
                self.save_contacts()
                print(f"Contact {contact_to_delete['name']} deleted successfully!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main menu loop for the contact book.
    Provides options for viewing, searching, adding, updating, and deleting contacts.
    """
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Search Contact")
        print("3. Add Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            contact_book.view_contacts()
        elif choice == '2':
            query = input("Enter name to search: ")
            contact_book.search_contact(query)
        elif choice == '3':
            contact_book.add_contact()
        elif choice == '4':
            name = input("Enter name to update: ")
            contact_book.update_contact(name)
        elif choice == '5':
            query = input("Enter name to delete: ")
            contact_book.delete_contact(query)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
