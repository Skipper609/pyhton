from contact import Contact
from beautifultable import BeautifulTable

class InMemoryImpl:

    contact_list = []

    @classmethod
    def add_contact(cls):
        name = input("Enter the Name :")
        email = input("Enter the Email :")
        mobile = int(input("Enter the Mobile No. :"))
        address = input("Enter the Address :")
        cls.contact_list.append(Contact(name, email, mobile, address))
        print(f"Contact is added successfulla with name : {name}")
    
    @classmethod
    def delete_contact(cls):
        if len(cls.contact_list) > 0:
            name = input("Enter the name :")
            contact = InMemoryImpl.get_contact_by_name(name)
            if contact:
                cls.contact_list.remove(contact)
                print(f"The conatact with name {name} deleted")
            else:
                print(f"The contact with name {name} not found")
        else:
            print("The contact book is empty !!")

    @classmethod
    def view_contact(cls):
        InMemoryImpl._paint(cls.contact_list)
    
    @classmethod
    def search(cls):
        if len(cls.contact_list):
            name = print("Enter the name to be searched :")
            res_lst = list(filter(lambda x:name.lower() in x.get__name().lower(), cls.contact_list))
            if len(res_lst) > 0:
                InMemoryImpl._paint(res_lst)
                print("No.of contacts found is ",len(res_lst))
            else:
                print(f"No contact with name {name} found")
        else:
            print("Contact book is empty")

    @classmethod
    def update_contact(cls):
        if len(cls.contact_list) > 0:
            name = input("Enter the name to be updated :")
            contact = cls.get_contact_by_name(name)
            if contact:
                print("1.Name  2.Email  3.Mobile  4.Address")
                ch = int(input("Enter the choice :"))
                if ch == 1:
                    print("Old value of name :",contact.get__name())
                    name = input("Enter the new name :")
                    if name :
                        contact.set__name(name)

                elif ch == 2:
                    print("Old value of Email :",contact.get__email())
                    email = input("Enter the new Email :")
                    if contact :
                        contact.set__email(email)
                
                elif ch == 3:
                    print("Old value of mobile :",contact.get__mobile())
                    mobile = input("Enter the new mobile :")
                    if mobile :
                        contact.set__mobile(mobile)
                
                else:
                    print("Old value of address :",contact.get__address())
                    address = input("Enter the new address :")
                    if address :
                        contact.set__address(address)
            else:
                print(f"No contact with name {name} found !!")
        else:
            print("The Contact book is empty")
    
    @staticmethod
    def _paint(lst):

        table = BeautifulTable()
        if len(lst) != 0:
            table.column_headers = ["Name", "Email", "Mobile", "Address"]
            for c in lst:
                table.append_row([c.get__name(), c.get__email(), c.get__mobile(), c.get__address()])
            print(table)
        else:
            print("ContactBook is empty....")
    
    @classmethod
    def get_contact_by_name(cls, name):

        if len(cls.contact_list) > 0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
            if len(contact) > 0:
                return contact[0]
