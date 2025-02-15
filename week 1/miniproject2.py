import json

# Initialize an empty list to store user data
registered_users = []

def register_user():
    """Function to register a new user"""
    print("\n--- User Registration ---")
    name = input("Enter your name: ").strip().title()
    email = input("Enter your email: ").strip()
    role = input("Enter your role (Admin/Student/Teacher): ").strip().capitalize()

    if not name or not email or not role:
        print("Error: All fields are required!")
        return

    if "@" not in email or "." not in email:
        print("Error: Invalid email address!")
        return

    valid_roles = ["Admin", "Student", "Teacher"]
    if role not in valid_roles:
        print(f"Error: Role must be one of {valid_roles}!")
        return

    user_id = len(registered_users) + 1
    user = {"ID": user_id, "Name": name, "Email": email, "Role": role}
    registered_users.append(user)
    print("\nUser registered successfully!")

def display_users():
    """Function to display all registered users"""
    if not registered_users:
        print("\nNo users registered yet!")
        return

    print("\n--- Registered Users ---")
    for user in registered_users:
        print(f"ID: {user['ID']}, Name: {user['Name']}, Email: {user['Email']}, Role: {user['Role']}")

def delete_user():
    """Function to delete a user by ID"""
    user_id = int(input("Enter the user ID to delete: "))
    global registered_users
    registered_users = [user for user in registered_users if user["ID"] != user_id]
    print(f"User with ID {user_id} deleted successfully!")

def update_user():
    """Function to update user details"""
    user_id = int(input("Enter the user ID to update: "))
    for user in registered_users:
        if user["ID"] == user_id:
            user["Name"] = input("Enter new name: ").strip().title() or user["Name"]
            user["Email"] = input("Enter new email: ").strip() or user["Email"]
            user["Role"] = input("Enter new role (Admin/Student/Teacher): ").strip().capitalize() or user["Role"]
            print("User updated successfully!")
            return
    print("User not found!")

def search_user():
    """Function to search for a user by name or email"""
    search_term = input("Enter name or email to search: ").strip().lower()
    results = [user for user in registered_users if search_term in user["Name"].lower() or search_term in user["Email"].lower()]
    if results:
        for user in results:
            print(f"ID: {user['ID']}, Name: {user['Name']}, Email: {user['Email']}, Role: {user['Role']}")
    else:
        print("No users found.")

def save_users():
    """Function to save users to a JSON file"""
    with open("users.json", "w") as file:
        json.dump(registered_users, file, indent=4)
    print("User data saved successfully!")

def load_users():
    """Function to load users from a JSON file"""
    global registered_users
    try:
        with open("users.json", "r") as file:
            registered_users = json.load(file)
        print("User data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")

def main():
    """Main function to handle the menu"""
    load_users()
    while True:
        print("\n--- User Registration System ---")
        print("1. Register a User")
        print("2. Display All Users")
        print("3. Delete a User")
        print("4. Update User Information")
        print("5. Search for a User")
        print("6. Save Users")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            search_user()
        elif choice == "6":
            save_users()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
