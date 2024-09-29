import json

def exp_addition(expenses, description, amount):
    expenses.append({"Description": description, "Amount":amount})
    print(f'Added expense: {description}, Amount: {amount}')

def get_balance(budget, expenses):
    return budget - budget_calc(expenses)

def show_budget(budget, expenses):
    print(f'Total Budget: {budget}')
    print("Expenses:")
    for expense in expenses:
       
        print(f"- {expense['Description']}: {expense['Amount']}")
    print(f'Total Spent: {budget_calc(expenses)}')
    print(f"Remaining Budget: {get_balance(budget, expenses)}")


def budget_calc(expenses):
    sum=0
    for expense in expenses:
        sum += expense['Amount']
    return sum

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["intial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []


def save_budget_details(filepath, intial_budget, expenses):
    data ={
        'intial_budget': intial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)



def main():
    print("Welcome to the Budget App")
    filepath ='budget_data.json'
    intial_budget, expenses = load_budget_data(filepath)
    if intial_budget ==0:
        intial_budget= float(input("Enter your initial budget: "))
    budget=intial_budget

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice==1:
            description= input("Enter expense description: ")
            amount= float(input("Enter expense amount: "))
            exp_addition(expenses,description,amount)
        
        elif choice==2:
            show_budget(budget, expenses)
        
        elif choice==3:
            save_budget_details(filepath, intial_budget,expenses)
            print("Exiting Budget App. Goodbye!")
            break

        else:
            print("Invalid, enter a number from (1-3)")
            return
            



if __name__ == "__main__":
    main()
