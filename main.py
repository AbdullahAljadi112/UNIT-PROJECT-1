import os
from clubs import Club
from football_api import get_club_info

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
            print("\n========== CLUB INFORMATION ==========")
        
            for index, club in enumerate(clubs, start=1):
                print(f"{index}. {club.name}")
        
            club_number = input("\nEnter club number: ")
        
            if club_number.isdigit():
                club_number = int(club_number)
        
                if 1 <= club_number <= len(clubs):
                    selected_club = clubs[club_number - 1]
                    os.system("cls" if os.name == "nt" else "clear")

                    print("========== CLUB INFORMATION ==========\n")
                    selected_club.display_info()
                else:
                    print("Invalid club number!")
            else:
                print("Please enter a valid number!")
        
            input("\nPress Enter to return to the main menu...")

        elif choice == "2":
                print("\n========== FAVORITE CLUBS ==========")
                print("1. Add Favorite Club")
                print("2. View Favorite Clubs")
                print("3. Remove Favorite Club")
                print("0. Back to Main Menu")

                favorite_choice = input("\nEnter your choice: ")
                if favorite_choice == "1":
                    print("\n========== SELECT CLUB ==========")

                    for index, club in enumerate(clubs, start=1):
                        print(f"{index}. {club.name}")

                    club_number = input("\nEnter club number: ")

                    if club_number.isdigit():
                        club_number = int(club_number)

                        if 1 <= club_number <= len(clubs):
                            selected_club = clubs[club_number - 1]

                            if selected_club not in favorites:
                                favorites.append(selected_club)
                                print(f"{selected_club.name} added to favorites! ⭐")
                            else:
                                print("This club is already in your favorites!")
                        else:
                            print("Invalid club number!")
                    else:
                        print("Please enter a valid number!")

                    input("\nPress Enter to return to the main menu...")

                elif favorite_choice == "2":
                    print("\n========== MY FAVORITE CLUBS ==========")

                    if not favorites:
                        print("You have no favorite clubs yet!")
                    else:
                        for index, club in enumerate(favorites, start=1):
                            print(f"{index}. {club.name}")

                    input("\nPress Enter to return to the main menu...")
                elif favorite_choice == "3":
                    print("\n========== REMOVE FAVORITE CLUB ==========")

                    if not favorites:
                        print("You have no favorite clubs to remove!")
                    else:
                        for index, club in enumerate(favorites, start=1):
                            print(f"{index}. {club.name}")

                        club_number = input("\nEnter club number to remove: ")

                        if club_number.isdigit() and 1 <= int(club_number) <= len(favorites):
                            removed_club = favorites.pop(int(club_number) - 1)
                            print(f"{removed_club.name} removed from favorites!")
                        else:
                            print("Invalid club number!")

                    input("\nPress Enter to return to the main menu...")
        elif choice == "3":
            print("\n========== CLUB INFORMATION ==========")
            print("1. Real Madrid")

            club_choice = input("\nEnter club number: ")

            if club_choice == "1":
                data = get_club_info(86)

                if data:
                    print(f"\nClub: {data.get('name')}")
                    print(f"Founded: {data.get('founded')}")
                    print(f"Stadium: {data.get('venue')}")
                    print(f"Website: {data.get('website')}")
                else:
                    print("Could not load club information.")
            else:
                print("Invalid club number!")

            input("\nPress Enter to return to the main menu...")

        elif choice == "4":
            print("Club Matches - Coming Soon")

        elif choice == "0":
            print("Thank you for using Football Hub!")
            break

        else:
            print("Invalid choice! Please try again.")  


al_nassr = Club("Al Nassr", "Saudi Arabia", "Al Awwal Park", 1955, "YELLOW")

al_hilal = Club("Al Hilal", "Saudi Arabia", "Kingdom Arena", 1957, "BLUE")

al_ahli = Club("Al Ahli", "Saudi Arabia", "King Abdullah Sports City", 1937, "GREEN")

al_ittihad = Club("Al Ittihad", "Saudi Arabia", "King Abdullah Sports City", 1927, "YELLOW")

real_madrid = Club("Real Madrid", "Spain", "Santiago Bernabeu", 1902, "WHITE")

barcelona = Club("FC Barcelona", "Spain", "Spotify Camp Nou", 1899, "RED")

liverpool = Club("Liverpool", "England", "Anfield", 1892, "RED")

man_city = Club("Manchester City", "England", "Etihad Stadium", 1880, "CYAN")

man_united = Club("Manchester United", "England", "Old Trafford", 1878, "RED")

juventus = Club("Juventus", "Italy", "Allianz Stadium", 1897, "WHITE")

clubs = [
    al_nassr, al_hilal, al_ahli, al_ittihad,
    real_madrid, barcelona, liverpool,
    man_city, man_united, juventus
]

favorites = []

main_menu()