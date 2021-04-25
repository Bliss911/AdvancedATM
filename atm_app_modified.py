import random
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
print('\n\t\t\t\t\t\t\t %s' %dt_string)

database = {}
accountBalance = 0
accountBalance = random.randrange(1000,50000)

def init():

    print ("\nWelcome to Zuri Bank\n")

    while True:

        haveAccount = input("Do you have an account with us: 1(Yes) 2(No) \n")

        if (haveAccount == '1'):
            login()
        elif haveAccount == '2':
            register()
        else:
            print("You have selected an Invalid Option")
            init()

def login():

    print("******** Login ********")

    # isLoginSuccessful = False

    accountNumberFromUser = int(input("\nWhat is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                # accountBalance = generateAccountBalance()
                print(f"Your account balance is {accountBalance}")
                bankOperation(userDetails)
                # isLoginSuccessful = True

    print('Invalid account or password')
    
    login()

def register():

    print("************ Register **************")
    
    email = input("What is your Email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account number has been created")
    print("== ==== ======== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Ensure you keep this number safe")
    print("== ==== ======== ===== ===")

    login()

def bankOperation(user):
    print(f"\n***********Welcome {user[0]}, {user[1]}******************\n")

    selectedOption = input("What would you like to do? (1)Deposit (2)Withdrawal (3)Logout (4)Exit\n")

    if selectedOption == '1':
        depositOperation()

    elif selectedOption == '2':
        withdrawalOperation()

    elif selectedOption == '3':
        logout()

    elif selectedOption == '4':
        print("\nThanks for using our app today. Don't forget to give us an awesome grade \N{grinning face}")

        exit()

    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    print("******** Withdrawal ********")
    
    print(f"Your Account Balance is ${accountBalance}.00\n")

    withdrawalAmount = input("How much do you want to withdraw: \n")
    if int(withdrawalAmount) > accountBalance:
        print('\nInsufficient Funds. Please try again later\n\n')
    else:
        accountBalance -= withdrawalAmount
        print(f'\nTransaction Successful!!! \n\nYour remaining balance is ${accountBalance}.00\nPlease Take your Cash\n\n')

    
def depositOperation():
    print("******** Deposit Operation ********")
    print(f"Account balance is {accountBalance}")
    depositAmount = int(input("\nEnter the amount you want to deposit: \n"))
    deposit = 
    accountBalance += depositAmount
    print(f'\nTransaction Successful!!! \n\nYour balance is ${accountBalance}.00\n\n')
    
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

# def generateAccountBalance():
#     return random.randrange(1000,50000)

def logout():
    login()



init()
# generateAccountBalance()