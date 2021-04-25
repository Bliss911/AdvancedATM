from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
print('\t\t\t\t\t\t\t %s' %dt_string)

while (True):

    allowedUsers = ['cious','ann','john']
    allowedPassword = ['passwordcious','passwordann','passwordjohn']
    accountBalance = [200000, 300000, 100000]

    name = input('What is your name (Enter q to quit): ')
    if (name == 'q'):
        print('Thank you for banking with us')
        exit()
    
        
    if(name in allowedUsers):
        password = input("Enter your correct password (Enter q to quit): ")
        if (password == 'q'):
            print('Thank you for banking with us')
            exit()
        
        userId = allowedUsers.index(name)

        if(password == allowedPassword[userId]):
            print('\nWelcome\n')

            userBalance = accountBalance[userId]
            print('\n \t\t\t\t\tYour account balance is $%i.00' %userBalance)

            
            print("*************************")
            print("Option 1: Withdrawal")
            print("Option 2: Deposit")
            print("Option 3: Complaints")
            print("*************************\n")

            selectedOption = input("Please select an option: ")

            if(selectedOption == '1'):
                print('\nYou selected %s, Withdrawal \n' % selectedOption)
                
                
                withdrawalAmount = input("How much do you want to withdraw: \n")
                if(int(withdrawalAmount) > userBalance):
                    print('\nInsufficient Funds. Please try again later\n\n')
                else:
                    remainingBalance = userBalance - int(withdrawalAmount)
                    print('\nTransaction Successful!!! \n\nYour remaining balance is $%i.00\nPlease Take your Cash now\n\n' % remainingBalance)

            elif(selectedOption == '2'):
                print('\nYou selected %s, Deposit' % selectedOption)
            
                depositAmount = int(input("\nEnter the amount you want to deposit: \n"))
                userBalance += depositAmount
                print('\nTransaction Successful!!! \n\nYour balance is $%i.00\n\n' %userBalance)

            elif(selectedOption == '3'):
                print('\nYou selected %s Complaints' % selectedOption)
                complaint = input("You may report your complaint: \n")
                if(complaint != 'q'):
                    print("Thank you for contacting us.\n\n")
                else:
                    quit()
                      

            elif(selectedOption == 'q'):
                print('Thanks for banking with us')
                exit()

            else:
                print('Invalid Option selected, please try again\n')

        else:
            print('Password Incorrect, please try again\n')

    else:
        print('Name not found, please try again\n')
            

