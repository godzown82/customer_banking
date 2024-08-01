# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("\nWhat is your savings account balance? "))
    print("\nYou entered:", savings_balance)
    savings_interest = float(input("\nPlease enter your bank's APR: "))
    print("\nYou entered:", savings_interest)
    savings_maturity = float(input("\nHow many months do you intend to save for? "))
    print("\nYou entered:", savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'\nYour updated savings account balance is: ${updated_savings_balance} with your earned interest rate of {interest_earned} for {savings_maturity} months')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("\nWhat is your CD account balance? "))
    print("\nYou entered:", cd_balance)
    cd_interest = float(input("\nPlease enter your CD bank's APR: "))
    print("\nYou entered:", cd_interest)
    cd_maturity = float(input("\nHow many months do you intend to save for in the CD account? "))
    print("\nYou entered:", cd_maturity)
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f'\nYour updated CD account balance is: ${updated_cd_balance} with your earned interest rate of {interest_earned} for {cd_maturity} months')

    # Call the main function.
if __name__ == "__main__":
    main()
