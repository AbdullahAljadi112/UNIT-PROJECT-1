from colorama import Fore, Style, init

init(autoreset=True)


def show_header():
    print(Fore.CYAN + Style.BRIGHT)
    print("=" * 45)
    print("        ⚽ FOOTBALL HUB ⚽")
    print("=" * 45)
    print(Style.RESET_ALL)


def show_main_menu():
    show_header()

    print(Fore.GREEN + "1. 🏟️  Browse Clubs")
    print(Fore.YELLOW + "2. ⭐ Favorite Clubs")
    print(Fore.CYAN + "3. ℹ️  Club Information")
    print(Fore.MAGENTA + "4. 📅 Club Matches")
    print(Fore.RED + "0. 🚪 Exit")

    print(Fore.WHITE + "\n" + "=" * 45)


def show_section(title, emoji="⚽"):
    print(Fore.CYAN + Style.BRIGHT)
    print("\n" + "=" * 45)
    print(f"        {emoji} {title}")
    print("=" * 45)
    print(Style.RESET_ALL)


def show_upcoming_match(home, away, date, status):
    print(Fore.YELLOW + f"\n⏳ {date}")
    print(Fore.WHITE + Style.BRIGHT + f"⚽ {home} VS {away}")
    print(Fore.GREEN + f"📅 Status: {status}")
    print(Fore.CYAN + "-" * 45)



def show_clubs(clubs):
    show_section("BROWSE CLUBS", "🏟️")

    for index, club in enumerate(clubs, start=1):
        print(
            Fore.GREEN + f"{index}. ⚽ " +
            Fore.WHITE + Style.BRIGHT + club.name +
            Fore.YELLOW + f"  🌍 {club.country}"
        )

    print(Fore.CYAN + "-" * 45)

def show_favorites(favorites):
    show_section("FAVORITE CLUBS", "⭐")

    if favorites:
        for index, club in enumerate(favorites, start=1):
            print(
                Fore.YELLOW + f"{index}. ⭐ " +
                Fore.WHITE + Style.BRIGHT + club.name
            )
    else:
        print(Fore.RED + "💔 No favorite clubs yet!")

    print(Fore.CYAN + "-" * 45)


def show_club_info(data):
    show_section("CLUB INFORMATION", "🏟️")

    print(Fore.CYAN + f"⚽ Club: {data.get('name')}")
    print(Fore.YELLOW + f"📅 Founded: {data.get('founded')}")
    print(Fore.GREEN + f"🏟️ Stadium: {data.get('venue')}")
    print(Fore.BLUE + f"🌐 Website: {data.get('website')}")

    coach = data.get("coach")

    if coach:
        print(Fore.MAGENTA + f"👨‍💼 Coach: {coach.get('name')}")
    else:
        print(Fore.RED + "👨‍💼 Coach information not available")

    squad = data.get("squad", [])

    print(Fore.YELLOW + "\n👕 PLAYERS")

    if squad:
        for player in squad[-11:]:
            print(Fore.WHITE + f"⚽ {player.get('name')} - {player.get('position')}")
    else:
        print(Fore.RED + "Players information not available")

    competitions = data.get("runningCompetitions", [])

    print(Fore.YELLOW + "\n🏆 COMPETITIONS")

    if competitions:
        for competition in competitions:
            print(Fore.GREEN + f"🏆 {competition.get('name')}")
    else:
        print(Fore.RED + "Competitions information not available")