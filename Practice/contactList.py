from isPhoneNumber import isPhoneNumber, standardFormat
import csv

def add():
    contact_name = input("\nType the name of the new contact or press Enter to return to contact options: ")
    while contact_name != "":
        with open("contacts.csv") as f:
            fileContentStr = f.read().replace('\n', '')
        if contact_name in fileContentStr:
            print(contact_name + " is already in the list")
        else:
            name_confirm = input("\nIs " + contact_name + " correct? \"Y\" or \"N\": ")
            while name_confirm != "Y" and name_confirm != "N":
                name_confirm = input("\nPlease type \"Y\" for Yes or \"N\" for No: ")
            if name_confirm == "Y":
                phoneNumber = input("\nInput " + contact_name + "\'s phone number or press Enter to start over: ")
                validPhoneNumber = False
                while phoneNumber != "" and validPhoneNumber == False:
                    try:
                        phoneNumber = isPhoneNumber(phoneNumber)
                        correctPhoneNum = input("\nIs " + standardFormat(phoneNumber) + " correct? \"Y\" or \"N\": ")
                        while correctPhoneNum != "Y" and correctPhoneNum != "N":
                            correctPhoneNum = input("\nPlease type \"Y\" for Yes or \"N\" for No: ")
                        if correctPhoneNum == "Y":
                            validPhoneNumber = True
                            continue
                    except AttributeError:
                        print("That is not a valid phone number")
                    phoneNumber = input("\nInput " + contact_name + "\'s phone number or press Enter to start over: ")
                if validPhoneNumber:
                    with open("contacts.csv", "a") as f:
                        writer = csv.writer(f, lineterminator = '\n')
                        writer.writerow([contact_name, phoneNumber])
                    print("\nAdded " + contact_name + " to contacts list")
        contact_name = input("\nType the name of the new contact or press Enter to return to contact options:" )
    print()

def contactList():
    with open("contacts.csv") as f:
        contacts = map(lambda x: x.split(',')[0], f.readlines())
    return list(contacts)

def viewContacts():
    with open("contacts.csv") as f:
        maxLength = len(sorted(contactList(), key=len)[-1])
        table = "{0:>" + str(maxLength) + "}: {1:>9}"
        print("\nFull contact information: ")
        for line in f.readlines():
            row = line.split(",")
            print(table.format(row[0], row[1]), end='')
        print()

def main():
    print(
        "\nType \'V\' to view all people listed in contacts\n" +
        "Type \'L\' to view contact's and their information\n" +
        "Type \'A\' to add a new contact\n" +
        "Type \'E\' to edit a contact's phone number\n" +
        "Type \'D\' to delete a contact\n" +
        "Press 'Enter' to end the program"
    )
    user_input = input("\nWhat would you like to do?: ")
    while user_input != "":
        if user_input == "V":
            print("\nThe contacts in the list are: ")
            for contact in sorted(contactList()):
                print(contact)
            print()
        elif user_input == "L":
            viewContacts()
        elif user_input == "A":
            add()
        elif user_input == "E":
            #work In-progress
        elif user_input == "D":
            #work In-progress
        else:
            print("\nPlease type a valid action\n")
        print(
            "Type \'V\' to view all people listed in contacts\n" +
            "Type \'L\' to view contact's and their information\n" +
            "Type \'A\' to add a new contact\n" +
            "Type \'E\' to edit a contact's phone number\n" +
            "Type \'D\' to delete a contact\n" +
            "Press 'Enter' to end the program"
        )
        user_input = input("\nWhat would you like to do?: ")

if __name__ == "__main__":
    main()
