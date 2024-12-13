#You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
#Initialize these attributes in the constructor.

#Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - 
#Ensure that the setter methods include validation (e.g., budget should be a positive number).

#Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. -
# Validate the expense amount before making deductions from the budget.

#Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, 
# allocated budget, and remaining budget after expenses.


#Expected Outcomes: 
# A `BudgetCategory` class capable of storing category details securely. 
# Methods that allow controlled access and modification of the private attributes, with validation checks in place.
# Ability to track expenses per category and update the remaining budget safely.
# Users can view a summary of each budget category, showcasing encapsulation in action.

#Task 1:
class BudgetCategory:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget 
        self.expenses = 0

#Task 2: getters and setters

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_budget(self):
        return self.budget
    
    def set_budget(self, budget):
        if budget > 0:
            self.budget = budget
        else:
            print("Budget must be a positive number.")

#Task 3:add expenses 
    def add_expense(self, amount):
       
        if amount > 0:
            self.expenses += amount
        else:
            print("Expenses must be a positive number.")

    def display_category_summary(self):
        remaining_budget = self.budget - self.expenses

#Task 4: display the budget category details

        print(f"Category: {self.name}")
        print(f"Budget : ${self.budget}")
        print(f"Expenses: ${self.expenses}")
        print(f"Remaining budget: ${remaining_budget}")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
