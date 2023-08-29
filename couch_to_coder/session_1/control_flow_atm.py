# A Simple programme to simulate
# a bank machine

#Initialize the variables
balance = 10000
pin = 2324

#Ask the user to input their pin
userPin = int(input("Enter your Pin: "))

#Check if the user pin is correct
if pin == userPin:
    userAction= input("Would you like to make a Withdrawal (W), Deposit (D) or see your account Balance (B) : ")
    #Get user's preferred action and execute it
    if userAction == "W":
        amount = float(input("How much would you like to withdraw: ")) 
        balance = balance - amount
        print(f"Your updated account balance is £{balance}")
    elif userAction == "D":
        amount = float(input("How much would you like to Deposit: ")) 
        balance = balance + amount
        print(f"Your updated account balance is £{balance}")
    else:
        print(f"Your account balance is £{balance}")

else:
    print("You have entered the wrong pin. Would you like to try again? ")