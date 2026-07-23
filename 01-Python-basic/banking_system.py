account = {}


def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account created successfully!\n")


def check_balance():
    if account:
        print("Account Holder:", account["name"])
        print("Current Balance:", account["balance"])
    else:
        print("No account found.")


def deposit():
    if account:
        amount = float(input("Enter amount to deposit: "))
        account["balance"] += amount
        print("Amount deposited successfully!")
    else:
        print("No account found.")


def withdraw():
    if account:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= account["balance"]:
            account["balance"] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance.")
    else:
        print("No account found.")


while True:
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_account()
    elif choice == 2:
        check_balance()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        print("Thank you for using the Banking System!")
        break
    else:
        print("Choose number between 1 to 5")
