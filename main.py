
import os
from validation import validate_menu_choice
from validation import validate_club_number
from clubs import Club
from football_api import get_club_info, get_club_matches
from design import (
    show_main_menu,
    show_clubs,
    show_favorites,
    show_club_info,
    show_upcoming_match,
    show_team_selection,

)


al_nassr = Club(
    "Al Nassr", "Saudi Arabia", "Al Awwal Park", 1955, "YELLOW"
)

al_hilal = Club(
    "Al Hilal", "Saudi Arabia", "Kingdom Arena", 1957, "BLUE"
)

al_ahli = Club(
    "Al Ahli", "Saudi Arabia", "King Abdullah Sports City", 1937, "GREEN"
)

al_ittihad = Club(
    "Al Ittihad", "Saudi Arabia", "King Abdullah Sports City", 1927, "YELLOW"
)

real_madrid = Club(
    "Real Madrid", "Spain", "Santiago Bernabeu", 1902, "WHITE"
)

barcelona = Club(
    "FC Barcelona", "Spain", "Spotify Camp Nou", 1899, "RED"
)

liverpool = Club(
    "Liverpool", "England", "Anfield", 1892, "RED"
)

man_city = Club(
    "Manchester City", "England", "Etihad Stadium", 1880, "CYAN"
)

man_united = Club(
    "Manchester United", "England", "Old Trafford", 1878, "RED"
)

juventus = Club(
    "Juventus", "Italy", "Allianz Stadium", 1897, "WHITE"
)


clubs = [
    al_nassr,
    al_hilal,
    al_ahli,
    al_ittihad,
    real_madrid,
    barcelona,
    liverpool,
    man_city,
    man_united,
    juventus,
]

favorites = []

def main_menu():

    team_ids = {
        "Real Madrid": 86,
        "FC Barcelona": 81,
        "Liverpool": 64,
        "Manchester City": 65,
        "Manchester United": 66,
        "Juventus": 109,
    }

    while True:

        show_main_menu()
        choice = input("\nEnter your choice: ")

        if not validate_menu_choice(choice, ["0" , "1" , "2" , "3" , "4"]):
            input("\npress Enter to try again...")
            continue

        if choice == "1":

            show_clubs(clubs)

        
            club_number = input("\nEnter club number: ")

            if validate_club_number(club_number, len(clubs)):
                club_number = int(club_number.strip())

                selected_club = clubs[club_number - 1]

                os.system("cls" if os.name == "nt" else "clear")

                print("\n========== CLUB INFORMATION ==========\n")
                selected_club.display_info()


            input("\nPress Enter to return to the main menu...")

        elif choice == "2":

            print("\n========== FAVORITE CLUBS ==========")
            print("1. ⭐ Add Favorite Club")
            print("2. 📋 View Favorite Clubs")
            print("3. ❌ Remove Favorite Club")
            print("0. 🔙 Back to Main Menu")

            favorite_choice = input("\nEnter your choice: ")

            if favorite_choice == "1":

                show_clubs(clubs)

                club_number = input("\nEnter club number: ")

                if club_number.isdigit():

                    club_number = int(club_number)

                    if 1 <= club_number <= len(clubs):

                        selected_club = clubs[club_number - 1]

                        if selected_club not in favorites:

                            favorites.append(selected_club)

                            print(
                                f"\n⭐ {selected_club.name} added to favorites!"
                            )

                        else:
                            print("This club is already in your favorites!")

                    else:
                        print("Invalid club number!")

                else:
                    print("Please enter a valid number!")

                input("\nPress Enter to return to the main menu...")

            elif favorite_choice == "2":

                show_favorites(favorites)

                input("\nPress Enter to return to the main menu...")

            elif favorite_choice == "3":

                show_favorites(favorites)

                if favorites:

                    club_number = input(
                        "\nEnter club number to remove: "
                    )

                    if (
                        club_number.isdigit()
                        and 1 <= int(club_number) <= len(favorites)
                    ):

                        removed_club = favorites.pop(
                            int(club_number) - 1
                        )

                        print(
                            f"\n❌ {removed_club.name} removed from favorites!"
                        )

                    else:
                        print("Invalid club number!")

                input("\nPress Enter to return to the main menu...")

            # BACK
            elif favorite_choice == "0":
                continue

            else:
                print("Invalid choice!")

        elif choice == "3":

            print("\n========== CLUB INFORMATION ==========")

            show_team_selection(team_ids)

            club_choice = input("\nEnter club number: ")

            if validate_club_number(club_choice, len(team_ids)):

                team_name = list(team_ids.keys())[
                    int(club_choice.strip()) - 1
                ]

                team_id = team_ids[team_name]

                data = get_club_info(team_id)

                if data:
                    show_club_info(data)

                else:
                    print("Could not load club information.")

            input("\nPress Enter to return to the main menu...")

        elif choice == "4":

            print("\n========== CLUB MATCHES ==========")

            show_team_selection(team_ids)

            club_choice = input("\nEnter club number: ")

            if validate_club_number(club_choice, len(team_ids)):

                team_name = list(team_ids.keys())[
                    int(club_choice.strip()) - 1
    ]

                team_id = team_ids[team_name]

                data = get_club_matches(team_id)

                if data is not None:

                    matches = data.get("matches", [])

                    if matches:

                        for match in matches:

                            home = match.get(
                                "homeTeam", {}
                            ).get("name", "Unknown")

                            away = match.get(
                                "awayTeam", {}
                            ).get("name", "Unknown")

                            date = match.get(
                                "utcDate", ""
                            )[:10]

                            status = match.get(
                                "status", "Unknown"
                            )

                            show_upcoming_match(
                                home,
                                away,
                                date,
                                status,
                            )

                    else:
                        print("No matches available.")

                else:
                    print("Could not load matches.")

            input("\nPress Enter to return to the main menu...")

        elif choice == "0":

            print("\n👋 Thank you for using Football Hub!")
            break

        else:
            print("\n❌ Invalid choice! Please try again.")
            input("\nPress Enter to continue...")
            
if __name__ == "__main__":
    main_menu()
