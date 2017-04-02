""" Module containing function to operate with the Database """

# helping functions for the demo
def add_expense(user_name, expense_date, expense_amount, expense_description):
    """ Function to add a new expense to the DB """

    return "Expense added successfully!"

def get_all_expenses():
    """ Function to select all expenses from DB """

    return [
        {'user_name':'ivo', 'date':1, 'amount':1.34}
        , {'user_name':'ivo', 'date':2, 'amount':4.46}
        , {'user_name':'ivo', 'date':3, 'amount':6.30}
        , {'user_name':'aline', 'date':1, 'amount':1.64}
        , {'user_name':'aline', 'date':2, 'amount':3.78}
        , {'user_name':'aline', 'date':3, 'amount':2.20}
    ]

