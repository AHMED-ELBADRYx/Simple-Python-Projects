# Changing attributes by adding them as parameters in a function

class Movie:
    def __init__(self, name, actor, hero, year, kind):
        self.name = name
        self.actor = actor
        self.hero = hero
        self.year = year
        self.kind = kind

    def display(self):
        print(f"Name: {self.name}")
        print(f"Actor: {self.actor}")
        print(f"Hero: {self.hero}")
        print(f"Year: {self.year}")
        print(f"Kind: {self.kind}\n")

    def change_actor_and_hero(self, actor, hero):
        self.actor = actor
        self.hero = hero

# Create movies
movies = [
    Movie("The Dark Knight", "Christian Bale", "Bruce Wayne", 2008, "Action"),
    Movie("John Wick", "Keanu Reeves", "John Wick", 2014, "Action Thriller"),
    Movie("Inception", "Leonardo DiCaprio", "Dom Cobb", 2010, "Sci-Fi"),
    Movie("Gladiator", "Russell Crowe", "Maximus", 2000, "Historical Drama")
]

print("🎬 Movies before editing:\n")
for movie in movies:
    movie.display()

# Change attributes
print("🎬 Editing actor and hero...\n")
movies[0].change_actor_and_hero("Rachel Dawes", "Maggie Gyllenhaal")
movies[1].change_actor_and_hero("Bridget Moynahan", "Helen Wick")
movies[2].change_actor_and_hero("Marion Cotillard", "Mal Cobb")
movies[3].change_actor_and_hero("Connie Nielsen", "Lucilla")

print("🎬 Movies after editing:\n")
for movie in movies:
    movie.display()