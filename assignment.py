"""
Personal Expense Tracker & Analyzer
===================================
Description:
    Prompts the user to repeatedly enter positive expense amounts until '0'
    is entered to terminate input. Stores entries in a list, validates against
    negative numbers, categorizes each expense by tier, and displays summary
    statistics formatted as currency.

Categorization Tiers:
    - Small Expense:    Less than $25.00
    - Moderate Expense: $25.00 to $100.00 (inclusive)
    - Large Expense:    Greater than $100.00

Summary Output:
    - Total count of expenses entered
    - Total sum of all expenses
    - Average expense amount
    - Minimum (smallest) expense
    - Maximum (largest) expense
    - Frequency count per tier (small, moderate, large)

Sample Run:
    Enter an expense or 0 to finish: 12.50
    Enter an expense or 0 to finish: 48.75
    Enter an expense or 0 to finish: 1250
    Enter an expense or 0 to finish: 0

    Expense Summary
    ---------------
    Number of expenses: 3
    Total: $1,311.25
    Average: $437.08
    Smallest expense: $12.50
    Largest expense: $1,250.00
    Small expenses: 1
    Moderate expenses: 1
    Large expenses: 1
"""


def take_inputs(expense_list):
# while loop, if input == 0 end
# append every input to a list

    while True:
        expense = float(input("Enter an expense or 0 to finish: "))
        if expense != 0:
            expense_list.append(expense)
        else:
            break

# #validate the list 
def validate_list(expense_list):
# # for loop to iterate thr list
    large_expenses = []
    medium_expenses = []
    small_expenses = []
    valid_expenses = []
    for expense in expense_list:

# check for negative numbers, if negative print error message and remove from list
        if expense < 0:
            print()
            print(f'{expense} is invalid, no negative numbers')

# simmultaneously categorize the list into small, moderate, and large expenses
        else:
            valid_expenses.append(expense)
            if expense > 100:
                large_expenses.append(expense)
            elif expense >= 25:
                medium_expenses.append(expense)
            else:
                small_expenses.append(expense)
    return large_expenses, medium_expenses, small_expenses, valid_expenses




# displays summary
def create_summary(valid_expenses, large_expenses, medium_expenses, small_expenses):
    print()
    print("Expense Summary")
    print("---------------")
#     - Total count of expenses entered
    print(f'Number of expenses: {len(valid_expenses)}')
#     - Total sum of all expenses
    print(f'Total: ${sum(valid_expenses):,.2f}')
#     - Average expense amount
    print(f'Average: ${sum(valid_expenses)/ len(valid_expenses):,.2f}')
#     - Minimum (smallest) expense
    print(f'Minimum: ${min(valid_expenses):,.2f}')
#     - Maximum (largest) expense
    print(f'Maximum: ${max(valid_expenses):,.2f}')
#     - Frequency count per tier (small, moderate, large)
    print(f'Small Expense count: {len(small_expenses)}')
    print(f'Medium Expense count: {len(medium_expenses)}')
    print(f'Large Expense count: {len(large_expenses)}')


def main():
#take inputs and create the list
    expense_list = []
    take_inputs(expense_list)

#Validate the list
    large_expenses, medium_expenses, small_expenses, valid_expenses = validate_list(expense_list)
    print (valid_expenses, large_expenses, medium_expenses, small_expenses)

##displays summary
    create_summary(valid_expenses, large_expenses, medium_expenses, small_expenses)


if __name__ == "__main__":
    main()