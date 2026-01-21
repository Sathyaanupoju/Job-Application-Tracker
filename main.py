import pandas as pd
import os

FILE_NAME = "job_applications.csv"

# Load existing data or create new DataFrame
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns=[
            "Company Name",
            "Job Role",
            "Location",
            "Application Date",
            "Status"
        ])

# Save data to CSV
def save_data(df):
    df.to_csv(FILE_NAME, index=False)

# Add new job application
def add_application(df):
    company = input("Enter Company Name: ")
    role = input("Enter Job Role: ")
    location = input("Enter Location: ")
    date = input("Enter Application Date (YYYY-MM-DD): ")
    status = input("Enter Status (Applied / Interview / Rejected / Selected): ")

    new_data = {
        "Company Name": company,
        "Job Role": role,
        "Location": location,
        "Application Date": date,
        "Status": status
    }

    df.loc[len(df)] = new_data
    save_data(df)
    print("✅ Job application added successfully!")

# View all applications
def view_applications(df):
    if df.empty:
        print("⚠️ No job applications found.")
    else:
        print("\n📄 Job Applications:")
        print(df)

# Main menu
def main():
    df = load_data()

    while True:
        print("\n--- Job Application Tracker ---")
        print("1. Add Job Application")
        print("2. View All Applications")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_application(df)
        elif choice == "2":
            view_applications(df)
        elif choice == "3":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.")
main()
