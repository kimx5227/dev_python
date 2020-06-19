import re

#program checks if user inputted a correct phone number

def isPhoneNumber(input):
    cleanedInput = "".join(re.split('[^0-9a-zA-Z]', input)) #strips non-alphanumeric characters
    phoneNumRegex = re.compile(r'\d{10}')
    return phoneNumRegex.search(cleanedInput).group()

def standardFormat(input):
    return input[0:3] + "-" + input[3:6] + "-" + input[6:]

def main():
    print("What is your phone number? ")
    find_number = input()
    while find_number != "":
        try:
            print("\nIs", standardFormat(isPhoneNumber(find_number)), "your phone number? \nType \"Y\" for Yes or \"N\" for No")
            correctInput = input()
            while correctInput != "Y" and correctInput != "N":
                print("\nPlease type \"Y\" for Yes or \"N\" for No")
                correctInput = input()
            if correctInput == "Y":
                print("Phone number has been accepted")
            print("\nEnter another phone number or press enter to quit:")
        except AttributeError:
            print("\nThat isn't a valid phone number. Please re-enter a phone number")
        find_number = input()

if __name__ == "__main__":
    main()
