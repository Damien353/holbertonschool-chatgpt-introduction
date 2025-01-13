class Checkbook:
    """
    Class description:
    A class representing a simple checkbook system. It allows deposits, withdrawals,
    and balance checks.

    Attributes:
    balance (float): The current balance in the checkbook. Starts at 0.0.
    """
    def __init__(self):
        """
        Function description:
        Initializes a Checkbook instance with a balance of 0.0.

        Parameters:
        None

        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
        Deposits a given amount into the checkbook and prints the updated balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
        Withdraws a given amount from the checkbook if sufficient funds are available.
        Prints the updated balance or an error message if there are insufficient funds.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
        Prints the current balance of the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function description:
    Main function that runs an interactive checkbook program allowing the user to deposit,
    withdraw, check balance, or exit. The program continues until the user decides to exit.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()  # Create a new Checkbook instance
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    """
    Function description:
    Calls the main function to run the checkbook program.

    Parameters:
    None

    Returns:
    None
    """
    main()

