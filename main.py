from clubs import Club

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
0
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
0
for club in clubs:
    club.display_info()
    print("-" * 35)