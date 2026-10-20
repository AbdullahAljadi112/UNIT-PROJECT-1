def main_menu():
    while True:
        print("\n========== FOOTBALL HUB ==========")
        print("Welcome to Football Hub!")
        print("1. Browse Clubs")
        print("2. Search Club")
        print("3. Club Information")
        print("4. Club Matches")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("Browse Clubs - Coming Soon")

        elif choice == "2":
            print("Search Club - Coming Soon")

        elif choice == "3":
            print("Club Information - Coming Soon")

        elif choice == "4":
            print("Club Matches - Coming Soon")

        elif choice == "0":
            print("Thank you for using Football Hub!")
            break

        else:
            print("Invalid choice! Please try again.")


main_menu()