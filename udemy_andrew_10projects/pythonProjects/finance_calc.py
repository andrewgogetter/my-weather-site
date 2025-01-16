def calc_finances_expenses(month_income: float, tax_rate: float, currency: str):
    month_tax: float=month_income*(tax_rate/100)
    month_net_income: float=month_income-month_tax
    year_salary: float=month_income*12
    year_tax: float=month_tax*12
    year_net_income: float=year_salary-year_tax

    print("-"*50)
    print(f"Monthly income: {currency}{month_income:.2f}")
    print(f"Tax rate: {tax_rate}%")
    print(f"Monthly tax: {currency}{month_tax:.2f}")
    print(f"Monthly net income: {currency}{month_net_income:.2f}")
    print(f"Yearly salary: {currency}{year_salary:.2f}")
    print(f"Yearly tax paid: {currency}{year_tax:.2f}")
    print(f"Yearly net income: {currency}{year_net_income:.2f}")
    print("-"*50)

    year_income=year_net_income
    month_clear_income=year_income/12
    month_data=[]
    for month in range(1,13):
        print(f"Month {month}")
        expenses=[]
        while True:
            try:
                expense=float(input("Enter your expense for a month or type '0' to finish: "))
                if expense==0:
                    break
                else:
                    expenses.append(expense)
            except ValueError:
                print("Please enter a NUMBER!")

        total_expenses=sum(expenses)
        remaining_balance=month_clear_income-total_expenses
        month_data.append({"total_expenses": total_expenses,"remaining_balance": remaining_balance})

    print("\nSummary of 12 months")
    for month,data in enumerate(month_data,start=1):
        print(f"Month: {month} | Total expenses: {data['total_expenses']:.2f}, Remaining balance: {data['remaining_balance']:.2f}")


def call_calc():
    try:
        month_income: float = float(input("Enter your monthly salary: "))
        tax_rate: float = float(input("Enter your tax rate (%): "))
    except ValueError:
        print("You have to enter a number")
        return call_calc()
    calc_finances_expenses(month_income,tax_rate,currency="USD")


if __name__=="__main__":
    call_calc()