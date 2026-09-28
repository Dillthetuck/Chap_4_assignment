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
        expense = int(input("Enter an expense or 0 to finish: "))
        if expense != 0:
            expense_list.append(expense)
        else:
            break

# #validate the list 
# # for loop to iterate thr list
# check for negative numbers, if negative print error message and remove from list
# simmultaneously categorize the list into small, moderate, and large expenses

# displays summary
#     - Total count of expenses entered
#     - Total sum of all expenses
#     - Average expense amount
#     - Minimum (smallest) expense
#     - Maximum (largest) expense
#     - Frequency count per tier (small, moderate, large)




if __name__ == "__main__":
#     #take inputs and create the list
    expense_list = []
    take_inputs(expense_list)
    print(expense_list)
#     #Validate the list

#     # categorize list

#     #displays summary


