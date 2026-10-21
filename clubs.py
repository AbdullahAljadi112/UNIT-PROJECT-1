class Club:
    def __init__(self, name, country, stadium, founded, color):
        self.name = name
        self.country = country
        self.stadium = stadium
        self.founded = founded
        self.color = color

    def display_info(self):
        print(f"⚽ Club: {self.name}")
        print(f"🌍 Country: {self.country}")
        print(f"🏟️ Stadium: {self.stadium}")
        print(f"📅 Founded: {self.founded}")