class Movie:
    def __init__(self):
        self.movie = input("What is movie name? ")
        self.actor = input("Who is Actor? ")
        self.actoress = input("Who is Actress? ")
        self.year = input("Year? ")

    def display(self):
        print("----- Movies detail -----")
        print("Movie :", self.movie)
        print("Actor :", self.actor)
        print("Actoress :", self.actoress)
        print("Year :", self.year)

movies = []

while True:
    movies.append(Movie()) 
    choice = input("Do you want to Insert More movies (Y/N): ").lower()
    if(choice == 'n'):
        break

for i in range(len(movies)):
    movies[i].display()