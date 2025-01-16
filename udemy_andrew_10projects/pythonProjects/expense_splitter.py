#Simplified version of the program!

# def calc_split(total_amount: float,people_num: int,currency: str) -> None:
#     if people_num<=1:
#         raise ValueError("Number of people must be greater than 1")
#
#     person_share: float = total_amount/people_num
#
#     print(f"Total expense: {currency}{total_amount:,.2f}")
#     print(f"Number of people: {people_num}")
#     print(f"Each person should pay: {currency}{person_share:,.2f}")
#
#
# def call_splitter():
#     try:
#         total_amount:float=float(input("Enter the expense amount: "))
#         people_num:int=int(input("Enter the number of people: "))
#     except ValueError:
#         print("Error: Please enter a number")
#         return call_splitter()
#     calc_split(total_amount,people_num,currency="USD")
#
#
# if __name__=="__main__":
#     call_splitter()


#2 Advanced version of the program!

def calc_splits(expenses):
    total_expenses=sum(expenses)
    splits=[]
    for user_expense in expenses:
        share=(user_expense/total_expenses)*100
        splits.append(share)

    return splits

def display_splits(expenses):
    splits=calc_splits(expenses) #we need to call this func to tally splits
    for i,(user_expense,split) in enumerate(zip(expenses,splits)):
        print(f"Person {i+1} spent ${user_expense:.2f}, which is {split:.2f}% of the total expenses")

def get_user_expenses():
    expenses=[]
    while True:
        try:
            user_expense=float(input("Enter your expense or type '0' to finish the program: "))
            if user_expense==0:
                break
            elif user_expense>0:
                expenses.append(user_expense)
            else:
                print("Enter 0 or a greater number!")
                get_user_expenses()
        except ValueError as e:
            print(f"{e}. You must to enter a NUMBER! And it have to be 0 or greater!")

    return expenses


if __name__=="__main__":
    print("Welcome to the Expense Splitter!")
    expenses=get_user_expenses()
    if expenses:
        display_splits(expenses)
    else:
        print("No expenses entered")