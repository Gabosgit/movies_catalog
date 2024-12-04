import json
from colors_library import *

def get_movies():
    """ Gets the data from the data.json file and serializes it. """
    with open('data.json', 'r') as data_file:
        data_json = data_file.read()
        data = json.loads(data_json)
        return data


dict_movies = get_movies()


def save_movies(movies):
    """ Gets all movies in "dict_movies" as an argument and saves them to the data.json file. """
    with open('data.json', 'w') as json_file:
        new_data = json.dumps(dict_movies)
        json_file.write(new_data)


def if_input_empty(prompt):
    """ This function is used in add_movie() to check if the input is empty. """
    while True:
        user_input = input(prompt)
        if user_input == '':
            print(red_on_black('Field is empty'))
        else:
            return user_input


def input_float_or_int(prompt):
    """ This function is used in add_movie() to check if the entered rating is int or float. """
    while True:
        user_input = input(prompt)
        try:
            float(user_input)
            if not 0 < float(user_input) <= 10:
                raise Exception(red_on_black("Expected a number (0.0 - 10.0)"))
        except ValueError:
            print(red_on_black("Expected a number (0.0 - 10.0)"))
        except Exception as error:
            print(error)
        else:
            return float(user_input)


def input_year(prompt):
    """ This function is used in add_movie() to check if the entered 'input_year' contains 4 digits. """
    while True:
        user_input = input(prompt)
        try:
            if not user_input.isdigit() or len(user_input) != 4:
                raise Exception(red_on_black("is not a valid year"))
        except Exception as error:
            print(error)
        else:
            return user_input


def add_movie():
    """ This function gets title, rating and year from user
    and adds a movie to the dictionary “dict_movie”.
    Then updates the data.json file with the save_movies() function. """
    movie_title = if_input_empty(f"\n{black_on_yellow(' Enter new movie name: ')}")
    movie_rating = input_float_or_int("Enter new movie rating (0-10): ")
    movie_year = input_year("Enter new movie release year: ")
    dict_movies[movie_title] = {"rating": movie_rating, "year": movie_year}
    save_movies(dict_movies)
    print(green_on_black(f"Movie '{movie_title}' successfully added"))


def delete_movie():
    """ This function prompts the user for a title and checks if it exists in the dictionary “dict_movies”.
    If it finds the title, it deletes the movie from “dict_movies”.
    It then updates the data.json file with the save_movies() function. """
    input_movie_to_delete = input(f"\n{black_on_yellow('Enter movie name to delete:')}")
    if input_movie_to_delete in dict_movies.keys():
        del dict_movies[input_movie_to_delete]
        save_movies(dict_movies)
        print(green_on_black(f"Movie '{input_movie_to_delete}' successfully deleted"))
    else:
        print(red_on_black(f"Movie '{input_movie_to_delete}' doesn't exist!"))


def update_movie():
    """ This function prompts the user for a title and a rating to update.
    If the movie exists in the dictionary dict_movies, it updates the movie's rating.
    It then updates the data.json file with the save_movies() function. """
    input_movie_to_update = input(f"\n{black_on_yellow('Enter movie name to update:')}")
    if input_movie_to_update in dict_movies.keys():
        input_new_movie_rating = float(input("Enter new movie rating (0-10): "))
        dict_movies[input_movie_to_update]["rating"] = input_new_movie_rating
        print(green_on_black(f"Movie '{input_movie_to_update}' successfully updated"))
        save_movies(dict_movies)
    else:
        print(red_on_black(f"Movie '{input_movie_to_update}' doesn't exist!"))
