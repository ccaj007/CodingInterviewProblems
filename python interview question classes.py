'''
Imagine you are designing a simple contact management system. Write two Python classes:
1.  Contact, which holds information about an individual contact (name, phone number, and email).
    •   It should include a constructor (__init__) that initializes these attributes.
    •   It should have a method (e.g., update_phone) to change the phone number.
2.  ContactBook, which stores multiple Contact objects.
    •   It should include a constructor that initializes an empty list of contacts.
    •   It should allow adding a new contact, but not allow duplicate contacts
    •   It should allow removing a contact by name.
    •   It should allow searching for a contact by name and returning the matching Contact (or None if not found).
'''


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def update_phone(self, new_phone):
        self.phone = new_phone

    def __str__(self):
        return f"Contact(Name: {self.name}, Phone: {self.phone}, email: {self.email})"

# from dataclasses import dataclass

# @dataclass
# class Contact:
#     name: str
#     phone: str
#     email: str

#     def update_phone(self, new_phone):
#         self.phone = new_phone



from dataclasses import dataclass
@dataclass
class ContactBook:
    contacts = []

    def add_contact(self, contact: Contact):
        if any(c.name == contact.name for c in self.contacts):
            print(f"Contact with name {contact.name} already exists")
        else:
            self.contacts.append(contact)

    def remove_contact(self, name: str):
        self.contacts = [c for c in self.contacts if c.name != name]

    def find_contact(self,name: str):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def __str__(self):
        return "\n".join(str(contact) for contact in self.contacts)

if __name__ == "__main__":
    # Create a contact book
    contact_book = ContactBook()

    # Add contacts
    contact1 = Contact(name="Alice", phone="123-456-7890", email="alice@example.com")
    contact2 = Contact(name="Bob", phone="987-654-3210", email="bob@example.com")

    contact_book.add_contact(contact1)
    contact_book.add_contact(contact2)
    contact_book.add_contact(contact1)  # Attempt to add a duplicate

    print("\nContact Book:")
    print(contact_book)

    # Remove a contact
    contact_book.remove_contact("Alice")

    print("\nContact Book after removal:")
    print(contact_book)

    # Find a contact
    found_contact = contact_book.find_contact("Bob")
    print("\nFound Contact:", found_contact)
