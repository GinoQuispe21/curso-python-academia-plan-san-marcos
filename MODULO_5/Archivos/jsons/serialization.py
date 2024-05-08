import json

class Movie:

    def __init__(self, title, year, releassed, lenguage, run_time, in_theather, number_of_oscars) -> None:
        self.title = title
        self.year = year
        self.releassed = releassed
        self.lenguage = lenguage
        self.run_time = run_time
        self.in_theather = in_theather
        self.number_of_oscars = number_of_oscars

movie_robot_dreams = Movie(
    title = "Robot Dreams",
    year = "2023",
    releassed = "20 Noviembre 2023",
    lenguage = ["English"],
    run_time = 150,
    in_theather = False,
    number_of_oscars = None
)

movie_format_json = json.dumps(movie_robot_dreams.__dict__, indent = 2, sort_keys = True)
print(movie_format_json, type(movie_format_json))