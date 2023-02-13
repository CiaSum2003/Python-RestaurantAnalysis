"""
Cianee Sumowalt
December 6, 2022
Homework 9: Restaurant Ratings

"""
import statistics as stat

def create_list():
    restaurant_file = open("restaurants.txt","r") # Read allows us to view the contents of the file but not edit them
    restaurant_list = restaurant_file.readlines()
    restaurant_list_2D = [[elem.lstrip( ).rstrip() for elem in x.split(",")] for x in restaurant_list]
    #print (restaurant_list_2D) # This removes the spaces in the the list
    return restaurant_list_2D

"""
I want to compare the names of the restaurants, the location, the price, the theme, the price, and the rating. To do that
I want to make a function that separates each element of the list to be compared in another function. So I will
make a loop where it goes through the entire list and takes the appropriate function and assigns them to the correct variable
Name = (0,0),(1,0)(2,0)(3,0)(...)cusine_dict
Location = (0,1),(2,1),(3,1),(4,1)

"""
def format_list(list2d):
    for i in range(len(list2d)):
        for j in range(len(list2d[i])):
            print (f"{list2d[i][j]}", end= "\n")
        print ()

def sort_cuisine_ratings(list2d): 
    """
    This function sorts the cuisines from the 2d list into a dictionary, sorts them so it's the correct rating, 
    then finds the highest mean/lowest mean
    """
    cuisine_dict = {}
    i = 0
    for n in range(len(list2d)):
        key = list2d[n][2]
        i+=1
        if key not in cuisine_dict:
            cuisine_dict[key] = []
            cuisine_dict[key].append(float(list2d[n][4]))
        if key in cuisine_dict and i != n:
            cuisine_dict[key].append(float(list2d[n][4]))

    for k in cuisine_dict:
        del cuisine_dict[k][0] # first value is always repeated, so i get rid of the first one for accuracy
        #print (cuisine_dict)

    highest_cuisine_rating = max(cuisine_dict.values())
    highest_cuisine = [k for k,v in cuisine_dict.items() if v == highest_cuisine_rating]
    highest_cuisine_rating = round(stat.mean(highest_cuisine_rating),2)
    
    lowest_cuisine_rating = min(cuisine_dict.values())
    lowest_cuisine = [k for k,v in cuisine_dict.items() if v == lowest_cuisine_rating]
    lowest_cuisine_rating = round(stat.mean(lowest_cuisine_rating),2)
    
    print (f"The cuisine with the highest rating of a {highest_cuisine_rating} is {highest_cuisine}.")
    print ()
    print (f"The cuisine with the lowest rating of a {lowest_cuisine_rating} is {lowest_cuisine}.")

def ratings_expenses__names_match(list2d):
    """
    This function uses the original 2dlist as an argument, makes the items separate list, then 
    pairs them based on index to determine which restauarant has the highest prices etc
    """
    ratings_list = []
    prices_list = []
    restaurant_names_list = []
    for i in range(len(list2d)):
        restaurant_names = list2d[i][0]
        restaurant_names_list.append(restaurant_names)

        ratings = list2d[i][4] 
        ratings_list.append(ratings) # changed to a float later, use the float list

        prices = list2d[i][3]
        prices_list.append(prices)
    
        float_ratings_list = [] # initialized float rating list
        for elem in ratings_list:
             elem = float(elem)
             float_ratings_list.append(elem) 
    #Find the highest/lowest ratings/prices

    highest_rating = max(float_ratings_list) # initialize the highest overall rating to be referenced later
    lowest_rating = min(float_ratings_list) # initalize the lowest overall rating to be referenced later
    expensive_restaurants = max(prices_list) # initalize the most expensive restaurant to be referenced laster
    expense_index = [] # initalize the name of the most expensive restauarants to be appended later
    price_indices = [i for i, x in enumerate(prices_list) if x == expensive_restaurants]
    #print (price_indices)
    for i in range(len(restaurant_names_list)): # This creates the list of the most expensive restauarants
        for k in price_indices:
            if restaurant_names_list[k] == restaurant_names_list[i]:
                 expense_index.append(restaurant_names_list[i])
    #print (expense_index)
    if highest_rating in float_ratings_list:
        highest_index = float_ratings_list.index(highest_rating) 
    if lowest_rating in float_ratings_list:
        lowest_index = float_ratings_list.index(lowest_rating)
    highest_rating_restaurant = restaurant_names_list[highest_index] # using the indeex from above, show the name of the restaurant
    lowest_rating_restaurant = restaurant_names_list[lowest_index] # ^

    print (f"The restaurant with the highest rating of a {highest_rating} is {highest_rating_restaurant}")
    print ()
    print (f"The restaurant with the lowest rating of a {lowest_rating} is {lowest_rating_restaurant}.")
    print ()
    print (f"The most expensive restaurants are {expense_index}")

def show_results():
    print ("""\tThis program analyzes 
        the restaurants.txt file 
        to determine the restauarant
         with the highest rating, 
         the restaurant with the lowest rating, 
         the cuisine with the highest rating,
         the cuisine with the lowest rating, 
         and the most expensive restaurants 
         in the Boston area.""")
    print ()
    restaurant_list_2D = create_list()
    print ("Here is the list of restaurants and their values")
    format = format_list(restaurant_list_2D)
    prices_and_ratings = ratings_expenses__names_match(restaurant_list_2D)
    cuisine_ratings = sort_cuisine_ratings(restaurant_list_2D)
    return 

main = show_results()