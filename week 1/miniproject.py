# Initialize an empty list to store user data
registered_users = []

def register_user():
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
    if not registered_users:
        print("\nNo users registered yet!")
        return

    print("\n--- Registered Users ---")
    for user in registered_users:
        print(f"ID: {user['ID']}, Name: {user['Name']}, Email: {user['Email']}, Role: {user['Role']}")

def main():
    while True:
        print("\n--- User Registration System ---")
        print("1. Register a User")
        print("2. Display All Users")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
