print('''
Current Yield Calculator for stocks and bonds
=============================================
''')
restart = "y"
def cy_calc():
    annual_amount = input("Enter the annual interest/income in dollars: ")
    annual_amount = float(annual_amount)
    stock_value = input("Enter the current stock/bond price: ")
    stock_value = float(stock_value)
    
    print('''
    This is your current yield. Move the decimal point two spaces to the right to have your percentage:
    ''')
    print(annual_amount/stock_value * 100)
while restart == "y":
    cy_calc()
    continue_question = input('''
    Do you want to continue? Y/N: ''').lower()
    restart = continue_question
    if restart == "y":
     continue
else:
    print('''
            Goodbye!''')


