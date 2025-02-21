# OSIS Event Recommendation System

print("Welcome to the OSIS Event Recommendation System!")

while True:
    print("\nPlease enter the type of event you're interested in (sports, academic, social, leadership):")
    user_input = input().strip().lower()

    if user_input == "sports":
        print("Upcoming Event: 🏆 School Football Tournament on March 5th!")
    elif user_input == "academic":
        print("Upcoming Event: 📚 Math Olympiad Preparation on March 10th!")
    elif user_input == "social":
        print("Upcoming Event: 🎉 OSIS Charity Night on March 15th!")
    elif user_input == "leadership":
        print("Upcoming Event: 🏛 Student Council Workshop on March 20th!")
    else:
        print("⚠️ Invalid input. Please enter 'sports', 'academic', 'social', or 'leadership'.")

    # Ask the user if they want to check another event
    print("\nWould you like to check another event? (yes/no)")
    repeat = input().strip().lower()
    if repeat != "yes":
        break

print("\nThank you for using the OSIS Event Recommendation System! 🚀")
