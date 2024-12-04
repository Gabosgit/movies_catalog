""" Phase 2 of the Movie project """
import statistics
import random
from rapidfuzz import fuzz
from colors_library import *
import movie_storage
from movie_storage import dict_movies

def list_movies():
    """ This function prints the list of movies by iterating over the keys "titles"
    and obtaining values "year" and "rating"""
    number_of_movies = len(dict_movies)
    print(f"\n{black_on_yellow(f' *** {number_of_movies} MOVIES IN TOTAL *** ')}")
    for title in dict_movies.keys():
        rating = dict_movies[title]['rating']
        year =dict_movies[title]['year']
        print(f"{title} ({year}): {yellow_on_black(f' {rating} ')}")


def calc_average(movies_dictionary):
    """ This function calculates the average of the ratings of a list of ratings. """
    number_of_movies = len(movies_dictionary)
    sum_ratings = 0
    for title in dict_movies.keys():
        rating = dict_movies[title]['rating']
        sum_ratings = sum_ratings + rating
    average_ratings = sum_ratings / number_of_movies
    return average_ratings


def calc_median(movies_dictionary):
    """ This function calculates the median of the list of ratings using the library statistics (median). """
    list_of_ratings = []
    for title in movies_dictionary.keys():
        rating = dict_movies[title]['rating']
        list_of_ratings.append(rating)
    rating_median = statistics.median(list_of_ratings)
    return rating_median


def get_best_and_worst_movie(movies_dictionary):
    """ This function returns lists of the best and worst rated movies and their respective ratings. """
    max_rating = 0
    min_rating = 10
    list_best_movies = []
    list_worse_movies = []
    for title in movies_dictionary.keys(): # get max and min rating
        rating = dict_movies[title]['rating']
        if rating > max_rating:
            max_rating = rating
        elif rating < min_rating:
            min_rating = rating
    for title in movies_dictionary.keys(): # get list of respective movies
        rating = dict_movies[title]['rating']
        if rating == max_rating:
            list_best_movies.append(title)
        if rating == min_rating:
            list_worse_movies.append(title)

    return list_best_movies, max_rating, list_worse_movies, min_rating


def stats():
    """This function prints the best and worst movie(s) returned by "get_best_and_worst_movie" function
    and prints the average and median returned by the "calc_average" and "calc_median" functions. """
    print(f"\n{black_on_yellow(' *** STATS *** ')}\n")
    average = calc_average(dict_movies)
    median = calc_median(dict_movies)

    list_best_movies = get_best_and_worst_movie(dict_movies)[0]
    max_rating = get_best_and_worst_movie(dict_movies)[1]
    list_worst_movie = get_best_and_worst_movie(dict_movies)[2]
    min_rating = get_best_and_worst_movie(dict_movies)[3]
    print(lightblue_on_black(" Average rating: "), black_on_lightblue(f" {average:.2f} "),"\n")
    print(green_on_black(" Median rating: "), black_on_green(f" {median:.2f} "), "\n")
    for best_movie in list_best_movies:
        print(yellow_on_black(" Best movie: "), f" {best_movie}", black_on_yellow(f" {max_rating} "), "\n")
    for worst_movie in list_worst_movie:
        print(red_on_black(" Worst movie: "), f" {worst_movie}", black_on_red(f" {min_rating} "),"\n")


def random_movie():
    """ This function uses the “random” library by choosing a number in the range of the length of the movie list
    and prints the movie pointed at the index of this number. """
    number_of_movies = len(dict_movies)
    random_num = random.randrange(1, number_of_movies)
    selected_random_movie = list(dict_movies)[random_num]
    random_movie_rating = dict_movies[selected_random_movie]['rating']
    random_movie_year = dict_movies[selected_random_movie]['year']
    print(f"\n{black_on_yellow(' YOUR MOVIE FOR TONIGHT ')}")
    print(f"{selected_random_movie} ({random_movie_year}), it's rated", lightblue_on_black(f" {random_movie_rating} "))


def get_title_year_rating_from_dict(list_of_movies):
    """ This function is used to get title, year and rating more easily with Unpacking tuple. """
    for title in list_of_movies.keys():
        rating = list_of_movies[title]['rating']
        year = list_of_movies[title]['year']
        return title, year, rating


def search_movie():
    """ This function gets a string (title) from the user and iterates the movie dictionary
    checking if it contains this string. If the string is found, it prints the movie title.
    In addition, it uses the "rapidfuzz library" to search for alternative movies. """
    input_movie_to_search = input(f"\n{black_on_yellow('Enter a part of the movie name:')}")
    input_lowercase = input_movie_to_search.lower()
    dic_string_found = {}
    dic_others_found = {}
    for title in dict_movies.keys():
        rating = dict_movies[title]['rating']
        year = dict_movies[title]['year']
        movie_lowercase = title.lower()
        if input_lowercase in movie_lowercase:
            dic_string_found[title] = {'rating': rating, 'year': year}
        else:
            fuzz_ratio = fuzz.ratio(input_lowercase, movie_lowercase)
            #print(f"simple ratio: {fuzz_ratio}")
            fuzz_token_sort_ratio = fuzz.token_sort_ratio(input_lowercase, movie_lowercase)
            #print(f"fuzz_token_sort_ratio: {fuzz_token_sort_ratio}")
            fuzz_partial_ratio = fuzz.partial_ratio(input_lowercase, movie_lowercase)
            #print(f"fuzz_partial_ratio: {fuzz_partial_ratio}")
            if fuzz_ratio >= 60:
                dic_others_found[title] = {'rating': rating, 'year': year}
                #print(f"ratio: {fuzz_ratio}: {title}")
            elif fuzz_token_sort_ratio >= 60:
                dic_others_found[title] = {'rating': rating, 'year': year}
                #print(f"fuzz_token_sort_ratio: {fuzz_token_sort_ratio}: {title}")
            elif fuzz_partial_ratio >= 90:
                dic_others_found[title] = {'rating': rating, 'year': year}
                #print(f"fuzz_partial_ratio: {fuzz_partial_ratio}: {title}")

    print(f"\n{black_on_green(' FOUND MOVIE(S) ')}")
    if not dic_string_found:
        print(red_on_black(f" The movie '{input_movie_to_search}' was not found."))
    else:
        for movie in dic_string_found:
            rating = dic_string_found[movie]['rating']
            year = dic_string_found[movie]['year']
            print(f"{movie} ({year}), {green_on_black(f' {rating} ')}")

    print(f"\n{black_on_lightblue(' OTHER FOUND MOVIE(S) ')}")
    if not dic_others_found:
        print(red_on_black(" No movie was found."))
    else:
        for movie in dic_others_found:
            rating = dic_others_found[movie]['rating']
            year = dic_others_found[movie]['year']
            print(f"{movie} ({year}), {lightblue_on_black(f' {rating} ')}")


def get_rating(title):
    """ Function used as KEY to sort movies in sort_movies_by_rating function """
    rating = float(dict_movies[title]['rating'])
    return rating


def sort_movies_by_rating():
    """ This function sorts the movies by rating and iterates the resulting list to print the sorted movies. """
    sorted_by_rating_list= sorted(dict_movies, key=get_rating, reverse=True)
    print("\n" + black_on_magenta(" *** MOVIES SORTED BY RATING *** "))
    for title in sorted_by_rating_list:
        year = dict_movies[title]['year']
        rating = dict_movies[title]['rating']
        print(f"{title} ({year}): " + magenta_on_black(f' {rating} '))


def input_yes_or_no(prompt):
    """ This is a function to prompt the user for YES or NO in "sort_movies_by_years" """
    while True:
        input_user = input(prompt)
        input_user.lower()
        if input_user == "y":
            return True
        elif input_user == "n":
            return False
        else:
            print('Please enter "Y" or "N"')


def get_year(title):
    """ Function used as KEY to sort the movies in the "sort_movies_by_years" function. """
    year = int(dict_movies[title]['year'])
    return year


def sort_movies_by_years():
    """ This function sorts the movies by year and iterates the resulting list to print the sorted movies. """
    latest_first = input_yes_or_no(green_on_black(" Do you want the latest movies first? (Y/N) "))
    sortd_by_year_list= sorted(dict_movies, key=get_year, reverse=latest_first)
    print("\n" + black_on_green(" *** MOVIES SORTED BY YEAR *** "))
    for title in sortd_by_year_list:
        year = dict_movies[title]['year']
        rating = dict_movies[title]['rating']
        print(f"{title} " + green_on_black(f"({year})") + f": {rating}")


def input_min_rating(prompt):
    """ This function prompts the user for a minimum rating and returns 0 if the user doesn't enter an answer. """
    while True:
        user_input = input(prompt)
        if user_input == '':
            return 0
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


def input_start_end_year(prompt):
    """ This function is used in the function filter_movies to prompt the user for a year """
    while True:
        user_input = input(prompt)
        if user_input == '':
            return 0
        try:
            if not user_input.isdigit() or len(user_input) != 4:
                raise Exception(red_on_black("is not a valid year"))
        except Exception as error:
            print(error)
        else:
            return int(user_input)


def filter_movies():
    """ This function gets 'min_rating' from the function "input_min_rating",
    gets 'start_year' and 'end_year' from the function "input_start_end_year".
    Then delete the movies in a dictionary "copy_dict_movies" using these criteria and prints the result """
    min_rating = input_min_rating(f"Enter {red_on_black(' minimum rating ')} (leave blank for no minimum rating): ")
    start_year = input_start_end_year(f"Enter {green_on_black(' start year ')} (leave blank for no start year): ")
    end_year = input_start_end_year(f"Enter {lightblue_on_black(' end year ')} (leave blank for no end year): ")
    if end_year == 0:
        end_year = float('inf')
    copy_dict_movies = dict_movies.copy()
    for title in dict_movies.keys():
        rating = float(copy_dict_movies[title]['rating'])
        year = int(copy_dict_movies[title]['year'])
        if rating < min_rating or year < start_year or year > end_year:
            del copy_dict_movies[title]
    print(f"\n{black_on_red(' *** FILTERED MOVIES *** ')}")
    for title in copy_dict_movies:
        rating = copy_dict_movies[title]['rating']
        year = copy_dict_movies[title]['year']
        print(f"{title} ({year}): {rating}")


def menu(print_menu):
    """ This function prompts the user to choose one option of the menu.
    Valid option calls a function pointed to in the dictionary "options_menu". 0 exits the application.
     Invalid option raises an exception.  """
    options_menu = {
        '1': list_movies,
        '2': movie_storage.add_movie,
        '3': movie_storage.delete_movie,
        '4': movie_storage.update_movie,
        '5': stats,
        '6': random_movie,
        '7': search_movie,
        '8': sort_movies_by_rating,
        '9': sort_movies_by_years,
        '10': filter_movies
    }

    while True:
        print(print_menu)
        input_menu_option = input(f"{lightblue_on_black(' Choose an option (1-10) and press ENTER: ')}\n")
        if input_menu_option == '0':  # 0 exit the app
            print("\n", yellow_on_black(" Bye Bye! "))
            break
        try:
            if input_menu_option not in options_menu: # Invalid input raises exception
                raise Exception(red_on_black(f" '{input_menu_option}' is not a valid option."))
        except Exception as error:
            print(error)
        else:
            options_menu[input_menu_option]() # Valid input calls a function
        input(f"\n{lightblue_on_black(' press ENTER to continue ' )}\n")


def main():
    """ This function contains the menu "menu_to_print" as a string, passing it as an argument
    to be printed in the while loop in menu(print_menu) """
    print(black_on_yellow("  *** My Movies Database ***   "))
    menu_to_print = (f"\n {black_on_yellow(' MENU ')} \n "
            f" 0. Exit \n "
            f" 1. List movies \n "
            f" 2. Add movie \n "
            f" 3. Delete movie \n "
            f" 4. Update movie \n "
            f" 5. Stats \n "
            f" 6. Random movie \n "
            f" 7. Search movie \n "
            f" 8. Movies sorted by rating \n "
            f" 9. Movies sorted by year \n "
            f"10. Filter movies \n ")
    menu(menu_to_print)


if __name__ == "__main__":
    main()
