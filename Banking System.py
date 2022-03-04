class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)
    
    def displayInfo(self):
        print()
        print(f"Details for {self.first_name} {self.last_name}:"
              f"\nGender: {self.gender}"
              f"\nAddress: {self.street_address}, {self.city}"
              f"\nEmail: {self.email}"
              f"\nCC-Number: {self.cc_number}"
              f"\nCC-Type: {self.cc_type}"
              f"\nBalance: ${self.balance}"
              f"\nAccount Number: {self.account_no}")


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5],
                 line[6], line[7], float(line[8][1:]), line[9])

def findUser():
    print("------------------------------------------------")
    print()
    search_user_fn = input("Enter the first name: ").title()
    search_user_ln = input("Enter the last name: ").title()
    user_found = False
    for user in userList:
        if user.first_name == search_user_fn \
                and user.last_name == search_user_ln:
            user.displayInfo()
            user_found = True

    if not user_found:
        print("Oops, something went wrong! Nobody has that name")


    
def overdrafts():
    overdraft_count = 0
    overdraft_total = 0
    print("------------------------------------------------")
    print()
    for user in userList:
        if user.balance < 0:
            user.displayInfo()
            overdraft_count += 1
            overdraft_total += user.balance

    print()
    print(f"{overdraft_count} users were overdraft"
          f"\nTotal overdraft: ${overdraft_total:.2f}")

    
def missingEmails():
    mis_email_count = 0
    print("------------------------------------------------")
    print()
    print("Here is a list of names for users without an email")
    for user in userList:
        if not user.email:
            print(f"{user.first_name} {user.last_name}")
            mis_email_count += 1
    print()
    print(f"Total number of users without an email address: {mis_email_count}")


def bankDetails():
    t_user_count = len(userList)
    t_balance = 0
    highest_balance = 0
    h_b_user = ""
    lowest_balance = 99999999
    l_b_user = ""
    for user in userList:
        t_balance += user.balance
        if user.balance > highest_balance:
            highest_balance = user.balance
            h_b_user = user
        if user.balance < lowest_balance:
            lowest_balance = user.balance
            l_b_user = user

    print("------------------------------------------------")
    print()
    print(f"Total number of users: {t_user_count}"
          f"\nTotal Bank worth: ${t_balance:.2f}"
          f"\n"
          f"\nHighest balance:"
          f"\n{h_b_user.first_name} {h_b_user.last_name}"
          f"\n${h_b_user.balance:.2f}"
          f"\n"
          f"\nLowest Balance:"
          f"\n{l_b_user.first_name} {l_b_user.last_name}"
          f"\n${l_b_user.balance:.2f}")
    print()
    print("------------------------------------------------")

    
def transfer():
    transaction = False
    print("------------------------------------------------")
    print()
    acc_no = input("Enter your account number: ")
    for user in userList:
        if user.account_no == acc_no:
            print(f"Name: {user.first_name} {user.last_name}"
                  f"\nBalance: ${user.balance:.2f}")
            print()
            amount_trans = int_check("Enter the amount to transfer: $",
                                     user.balance)
            print()
            acc_trans = input("Enter the account number for transfer: ")
            for user_trans in userList:
                if user_trans.account_no == acc_trans:
                    print(f"Name: {user_trans.first_name} "
                          f"{user_trans.last_name}"
                          f"\nBalance: ${user_trans.balance:.2f}")
                    print()
                    confirm = input(f"Enter 'Y' to confirm this transaction"
                                    f"\n${amount_trans} into the account of "
                                    f"{user_trans.first_name} "
                                    f"{user_trans.last_name} : ").upper()
                    if confirm == "Y":
                        user_trans.balance += amount_trans
                        user.balance -= amount_trans
                        print()
                        print(f"Transaction completed."
                              f"\n"
                              f"\nNew Balances:"
                              f"\n{user.first_name} {user.last_name}: "
                              f"${user.balance}"
                              f"\n{user_trans.first_name} "
                              f"{user_trans.last_name}: ${user_trans.balance}")
                        transaction = True
                    else:
                        print("Transaction cancelled")
                        transaction = True
    if not transaction:
        print("Oops, something went wrong!")


def int_check(question, max):
    valid = False
    error = "Please enter a valid amount"
    while not valid:
        try:
            response = int(input(question))
            # If not a valid number
            if response <= 0 or response > max:
                print(error)
            else:
                return response
        # if not a number print error
        except ValueError:
            print(error)


userList = []          
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print()
    print("------------------------------------------------")
    print()
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ").upper()
    print()
    
    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()      
    print()
