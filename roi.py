class Calculator:
    def __init__(self, monthly_income=0, monthly_expenses=0, total_investments=0, monthly_cf=0, annual_cash_cf=0, cash_on_cash_roi=0):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.total_investments = total_investments
        self.monthly_cf = monthly_cf
        self.annual_cash_cf = annual_cash_cf
        self.cash_on_cash_roi = cash_on_cash_roi

    def menu(self):
        print('-' * 50)
        print("WELCOME TO THE ROI CALCULATOR")
        print("""
        To begin please select your option:
        1. Use calculator
        2. View all
        3. To return to main menu
        0. To exit
        """)
        print('-' * 50)
        

    def income(self):
        rental_income = float(input("Rental income: "))
        laundry_income = float(input("Laundry income: "))
        storages_income = float(input("Storages income: "))
        misc_income = float(input("Miscellaneous income: "))
        self.monthly_income = rental_income + \
            laundry_income + storages_income + misc_income
        print('-' * 50)
        print(f"Your monthly income is {self.monthly_income}")
        print('-' * 50)

    def expenses(self):
        tax_expense = float(input("Tax expense: "))
        insurance_expense = float(input("Insurance expense: "))
        electric_expense = float(input("Electric expense: "))
        water_expense = float(input("Water expense: "))
        gas_expense = float(input("Gas expense: "))
        hoa_expense = float(input("Hoa expense: "))
        lawncare_expense = float(input("Lawncare expense: "))
        vacancy_expense = float(input("Vacancy expense: "))
        repairs_expense = float(input("Repairs expense: "))
        capitalex_expense = float(input("Capital expense: "))
        propertymgr_expense = float(input("Property manager expense: "))
        mortgage_expense = float(input("Mortgage expense: "))
        self.monthly_expenses = tax_expense + insurance_expense + electric_expense + water_expense + gas_expense + hoa_expense + \
            lawncare_expense + vacancy_expense + repairs_expense + \
            capitalex_expense + propertymgr_expense + mortgage_expense
        print('-' * 50)
        print(f"Your monthly expenses is {self.monthly_expenses}")
        print('-' * 50)

    def cash_flow(self):
        self.monthly_cf = self.monthly_income - self.monthly_expenses

        print('-' * 50)
        print(f"Your monthly cash flow is {self.monthly_cf}")
        print('-' * 50)

    def investments(self):
        down_payment = float(input("Down payment: "))
        closing_cost = float(input("Closing cost: "))
        rehab_cost = float(input("Rehab cost: "))
        misc = float(input("Miscellaneous: "))
        self.total_investments = down_payment + closing_cost + rehab_cost + misc
        print('-' * 50)
        print(f"Your total investments is {self.total_investments}")
        print('-' * 50)

    def annual_cash(self):
        self.annual_cash_cf = self.monthly_cf * 12
        print('-' * 50)
        print(f"Your annual cash flow is {self.annual_cash_cf}")
        print('-' * 50)

    def cash_on_cash(self):
        self.cash_on_cash_roi = (
            self.annual_cash_cf / self.total_investments) * 100
        roi = "{:.2f}".format(self.cash_on_cash_roi)

        print('-' * 50)
        print(f"""
        Your monthly income is {self.monthly_income}
        Your monthly expenses is {self.monthly_expenses}
        Your monthly cash flow is {self.monthly_cf}
        Your total investments is {self.total_investments}
        Your annual cash flow is {self.annual_cash_cf}
        """)
        
        print('-' * 50)

        print('-' * 50)
        print(f"""
        Your ROI is {roi}%
        """)
        print('-' * 50)
    def view_all(self):
        print('-' * 50)
        print(f"Your monthly income is {self.monthly_income}")
        print('-' * 50)
        print(f"Your monthly expenses is {self.monthly_expenses}")
        print('-' * 50)
        print(f"Your monthly cash flow is {self.monthly_cf}")
        print('-' * 50)
        print(f"Your total investments is {self.total_investments}")
        print('-' * 50)
        print(f"Your annual cash flow is {self.annual_cash_cf}")
        print('-' * 50)
        print(f"Your ROI is {self.cash_on_cash_roi}%")
        print('-' * 50)
    



def run_calculator():
    rental = Calculator()
    rental.menu()

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                rental.income()
                rental.expenses()
                rental.cash_flow()
                rental.annual_cash()
                rental.investments()
                rental.cash_on_cash()
            elif choice == 2:
                rental.view_all()
                 

            elif choice == 3:
                rental.menu()
            elif choice == 0:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a number")


run_calculator()
