import pandas as pd
import os
import matplotlib.pyplot as plt

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "habits.csv")

def init_data():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["habit", "date"])
        df.to_csv(DATA_FILE, index=False)

def add_habit(habit: str, date: str):
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = [habit, date]
    df.to_csv(DATA_FILE, index=False)
    print(f"Habit '{habit}' added for {date}!")

def view_habits():
    df = pd.read_csv(DATA_FILE)
    print(df)

def plot_habits():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("No habits tracked yet.")
        return
    counts = df.groupby("habit")["date"].count()
    counts.plot(kind="bar")
    plt.title("Habit Frequency")
    plt.xlabel("Habit")
    plt.ylabel("Days Completed")
    plt.show()

def main():
    init_data()
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Plot Habits")
        print("4. Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            habit = input("Enter habit name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_habit(habit, date)
        elif choice == "2":
            view_habits()
        elif choice == "3":
            plot_habits()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
