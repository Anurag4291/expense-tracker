# Personal Expense Tracker 🧾

A simple and interactive Python CLI application to track your daily expenses, categorize them, and monitor monthly budgets.

## 🔧 Features

- ✅ Add and store daily expenses
- ✅ Categorize expenses (Food, Travel, etc.)
- ✅ Set and track monthly budget
- ✅ Save and load expenses from a CSV file
- ✅ Menu-driven interface

## 🗃 Expense Format

Each expense contains:
- `Date` (YYYY-MM-DD)
- `Category` (e.g., Food, Travel)
- `Amount` (numeric)
- `Description` (short text)

Example:
```json
{
  "date": "2024-09-18",
  "category": "Food",
  "amount": 15.50,
  "description": "Lunch with friends"
}
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Anurag4291/expense-tracker.git
   cd expense-tracker
   ```

2. Run the script:
   ```bash
   python src/expense_tracker.py
   ```

3. Follow the interactive menu!

## 📁 Files

- `expense_tracker.py`: Main CLI application.
- `expenses.csv`: Auto-created CSV file for saving expenses.

## 📝 Future Improvements

- GUI support using Tkinter or PyQt
- Monthly/weekly summary reports
- Export to PDF or Excel
- Cloud storage option

---

## 🧑‍💻 Author

Developed with 💡 by [Anurag Sharma]

