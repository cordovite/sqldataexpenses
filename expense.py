import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create the expenses table 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )
""")
conn.commit()


def add_expense(amount, category, date, description):
    cursor.execute("INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?)",
                   (amount, category, date, description))
    conn.commit()
    print(" Expense added successfully.")


def update_expense(expense_id, new_amount, new_category, new_date, new_description):
    cursor.execute("UPDATE expenses SET amount = ?, category = ?, date = ?, description = ? WHERE id = ?",
                   (new_amount, new_category, new_date, new_description, expense_id))
    conn.commit()
    print(" Expense updated successfully.")

def delete_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print(" Expense deleted successfully.")


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if rows:
        print("\n📊 Expense Data:")
        print("=" * 50)
        print("{:<5} {:<10} {:<15} {:<12} {}".format("ID", "Amount", "Category", "Date", "Description"))
        print("=" * 50)
        for row in rows:
            print("{:<5} ${:<9} {:<15} {:<12} {}".format(*row))
    else:
        print("No expenses found.")


def main():
    print("Welcome to the Expense Tracker!\n")
    
    while True:
        print("\nSelect an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            add_expense(amount, category, date, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = int(input("Enter expense ID to update: "))
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")
            new_date = input("Enter new date (YYYY-MM-DD): ")
            new_description = input("Enter new description: ")
            update_expense(expense_id, new_amount, new_category, new_date, new_description)

        elif choice == '4':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)

        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Close the database connection when done
conn.close()
