# Build-in Module
import sys

import pandas as pd
import random


def main():
    print()
    print("//Note: Input the options serial number you want to choose!//\n")
    print("What you want to watch today??!!")
    print("****************")
    print("[1] Movies\n[2] Tv-Series\n[3] Animes")
    print("****************\n")
    choice = input_check(1, 3)

    match choice:
        case 1:
            movies_and_tv_series(1)
        case 2:
            movies_and_tv_series(2)
        case 3:
            animes()


# Suggest a movie or tv-series based on user preference.
def final_result(choice, rating, prefer, movie_list, tv_shows_list):
    # choice 1-> Movie, choice 2-> TV-Shows
    # Making a list based on the user likes
    if choice == 1:
        new_movie_list = preference(rating, prefer, movie_list)
    else:
        new_movie_list = preference(rating, prefer, tv_shows_list)

    # if found any movies or tv-series then print a random suggestion.
    if new_movie_list:
        suggestion = random.choice(new_movie_list)
        if choice == 1:
            print(
                f"\nYou should try {suggestion[0]}\nRating: {suggestion[1]}\nDuration: {suggestion[2]}\nReleased Year: {suggestion[3]}"
            )
        else:
            print(
                f"\nYou should try {suggestion[0]}\nRating: {suggestion[1]}\nSeasons: {suggestion[2]}\nReleased Year: {suggestion[3]}"
            )
    else:
        print("Oops!! Can't find any!")
        print("1. Return to Home\n2. End the process")
        c = input_check()
        if c == 1:
            main()
        else:
            sys.exit()


# Taking data from csv file
def movies_and_tv_series(choice):
    # Taking user preference and rating to suggest something based on this.
    rating, prefer = movie_tv_series_input(choice)

    df = pd.read_csv("netflix_titles.csv")

    contents = df[["type", "title", "rating", "duration", "release_year"]]

    m_s = pd.DataFrame(contents).values.tolist()

    # Making a movie list and tv-shows list with [title, rating, duration, released_year]
    movie_list = [
        [movie[1], movie[2], movie[3], movie[4]] for movie in m_s if movie[0] == "Movie"
    ]
    tv_shows_list = [
        [tv_show[1], tv_show[2], tv_show[3], tv_show[4]]
        for tv_show in m_s
        if tv_show[0] == "TV Show"
    ]

    final_result(choice, rating, prefer, movie_list, tv_shows_list)


def movie_tv_series_input(name):
    rating = -1
    print("Do you prefer rating!!")
    print("0.Home\n1.Yes \n2.Skip")
    r_choice = input_check(0, 2)
    if r_choice == 1:
        if name == 2:
            print(
                "1. TV-Y7 2. nan 3. TV-Y 4. TV-PG 5. TV-G\n6. NR 7. TV-14 8. R 9. TV-Y7-FV 10. TV-MA"
            )
            rating = input_check(1, 10)
        else:
            print(
                "1. PG 2. TV-MA 3. PG-13 4. TV-PG 5. R 6. TV-14\n7. G 8. TV-Y 9. UR 10. TV-Y7 11. NR 12. TV-G"
            )
            rating = input_check(1, 12)
    elif r_choice == 0:
        main()

    print("Watch Preference!!")
    print("0. Home 1. Back\n\n2. Latest \n3. 20's\n4. 90's")
    p_choice = input_check(0, 4)
    if p_choice == 0:
        main()
    elif p_choice == 1:
        return movie_tv_series_input(name)
    else:
        return rating, p_choice


# creates a list based on rating and prefer and returns it
def preference(rating, prefer, m_tvs_list):
    # movie[0] = m_name, movie[1] = rating, movie[2] = duration/seasons, movie[3] = released_year

    # nested list of movie and tv-shows rating.
    movie_rating_list = [
        ["PG", "Tv-Y7"],
        ["TV-MA", "nan"],
        ["PG-13", "TV-Y"],
        ["TV-PG", "TV-PG"],
        ["R", "TV-G"],
        ["TV-14", "NR"],
        ["G", "TV-14"],
        ["TV-Y", "R"],
        ["UR", "TV-Y7-FV"],
        ["TV-Y7", "TV-MA"],
        ["NR", None],
        ["TV-G", None],
    ]

    # if user don't choose rating means rating = - 1 then return a list based on preference
    # else return a list based on rating and preference

    if prefer == 1:
        year = [2020, 2021, 2022]
        if rating == -1:

            movie_tvs_list = [movie for movie in m_tvs_list if movie[3] in year]
        else:

            movie_tvs_list = [
                movie
                for movie in m_tvs_list
                if movie[3] in year and movie[1] in movie_rating_list[rating - 1]
            ]

    elif prefer == 2:
        if rating == -1:
            movie_tvs_list = [movie for movie in m_tvs_list if 2000 <= movie[3] <= 2019]
        else:
            movie_tvs_list = [
                movie
                for movie in m_tvs_list
                if 2000 <= movie[3] <= 2019
                and movie[1] in movie_rating_list[rating - 1]
            ]

    else:
        if rating == -1:
            movie_tvs_list = [movie for movie in m_tvs_list if 1925 <= movie[3] <= 1999]
        else:
            movie_tvs_list = [
                movie
                for movie in m_tvs_list
                if 1925 <= movie[3] <= 1999
                and movie[1] in movie_rating_list[rating - 1]
            ]
    return movie_tvs_list


# converting a nested list to a flat last
def strip(list):
    n = []
    for i in range(len(list)):
        new = list[i][1].lstrip("[").rstrip("]").split(",")
        new = [i.strip().lstrip("'").rstrip("'") for i in new]
        n.append(new)
    return n


# check for valid input
def input_check(min, max):

    while True:
        try:
            p = int(input("--> "))
            if not min <= p <= max:
                raise ValueError
            else:
                return p
        except ValueError:
            print("Invalid Input!! Choose a valid number!!")
            pass


def anime_input():
    print("Choose a category: ")
    print("0. Return To Home\n\n")
    print(
        "1. Drama 2. Sports 3. Comedy 4. Magic\n"
        "5. Fantasy 6. Action 7. Adventure 8. Sci-Fi\n"
        "9. Vampire 10. Historical 11. Mystery\n"
        "12. Physiological 13. Demons 14. Kids"
    )

    category = input_check(0, 14)
    # if user input 0 return to main() function
    if category == 0:
        main()

    print("0. Home 1. Back\n\n2. Select by popularity\n3. Select anything\n")
    p_select = input_check(0, 3)

    if p_select == 2:
        print(
            "0. Home 1. Back\n\n2. Select the top anime\n3. Choose a value for top amount of anime"
        )
        t_select = input_check(0, 3)
        if t_select == 0:
            main()
        elif t_select == 1:
            return anime_input()
        else:
            return category, p_select, t_select

    elif p_select == 0:
        main()

    elif p_select == 1:
        return anime_input()

    else:
        return category, p_select


def animes():
    t_select = 0
    a_input = anime_input()
    if len(a_input) == 3:
        category, p_select, t_select = a_input[0], a_input[1], a_input[2]

    else:
        category, p_select = a_input[0], a_input[1]

    # data type = uid,title,synopsis,genre,aired,episodes,members,popularity,ranked,score,img_url,link
    df = pd.read_csv("animes.csv")
    # creating a nested list with title, genre, episodes, link and popularity
    contents = df[["title", "genre", "episodes", "link", "popularity"]]
    animes = pd.DataFrame(contents).values.tolist()

    genres_list = [
        "Drama",
        "Sports",
        "Comedy",
        "Magic",
        "Fantasy",
        "Action",
        "Adventure",
        "Sci-Fi",
        "Vampire",
        "Historical",
        "Mystery",
        "Psychological",
        "Demons",
        "Kids",
    ]

    # striping any space or punctuation for the genre list in the nested list
    genre = strip(animes)

    list = [
        [animes[i][0], animes[i][2], animes[i][3], animes[i][4]]
        for i in range(len(animes))
        if genres_list[category - 1] in genre[i]
    ]

    if p_select == 3:
        anime = random.choice(list)
        print(f"You should try {anime[0]}\nLink: {anime[2]}")

    else:
        list.sort(key=lambda x: x[3], reverse=True)
        if t_select == 2:
            print(f"Top anime is {list[0][0]}\nLink: {list[0][2]}")
        else:
            while True:
                try:
                    maximum = max(list)[3]
                    top = int(input("Enter the Value: "))
                    if top > maximum:
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print(f"Range Exceed!! '//Range: {maximum}")
                    pass
            anime = random.choice(list[:top])
            print(f"\nYou should try {anime[0]}\nLink: {anime[2]}")


if __name__ == "__main__":
    main()

