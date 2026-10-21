from colorama import Fore, Style, just_fix_windows_console
just_fix_windows_console()
class Club:
    def __init__(self, name, country, stadium, founded, color):
        self.name = name
        self.country = country
        self.stadium = stadium
        self.founded = founded
        self.color = color

    def display_info(self):
        print(f"{getattr(Fore, self.color, Fore.WHITE)}⚽ Club: {self.name}{Style.RESET_ALL}")
        print(f"🌍 Country: {self.country}")
        print(f"🏟️ Stadium: {self.stadium}")
        print(f"📅 Founded: {self.founded}")