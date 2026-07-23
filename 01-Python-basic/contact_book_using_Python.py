contacts = {}       #create dict


def add_cont(): 

    name = (input("Enter name: "))
    pho_num = input("Enter Mobile Number: ")
    while len(pho_num) != 10 or not pho_num.isdigit():
        print("Error: Number must be exactly 10-digit.")
        pho_num = input("Enter Mobile Number: ")
    contacts[name] = pho_num
    print("Contact adding Successfully.")
def view_cont():
    if not contacts:
        print("No contacts founds.")
    else:
        for i in contacts:
            print(f"{i} - {contacts[i]}")
def search_cont():
    check_name = (input("Enter a name to search: ")).lower()
    found = False
    for name in contacts:
        if name.lower() == check_name:
            print(f"{name} - {contacts[name]}")      
            found = True
            break
        if not found:
            print("Contact not found!")  
def update():
    name_update = input("Enter the name to update: ")
    if name_update in contacts:
        new_num = input("Enter new Number: ")
        contacts[name_update] = new_num
        print("Contact updated successfully.")
    else:
        print("Contact not found.") 

def delete():
    del_name = input("Enter name to delete: ")
    if del_name in contacts:
        del contacts[del_name]
        print("Contact deleted successfully.")
    else:
        print("No contact found.")    


while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    option = int(input("Choose your choise: "))

    if option == 1:
        add_cont()
    elif option == 2:  
        view_cont()
    elif option ==3:
       search_cont()
    elif option == 4:
        update()   
    elif option == 5:
        delete()
    elif option == 6:
        break
    else:
        print("Choose between 1 to 6")
