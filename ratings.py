"""Restaurant rating lister."""
import random
from secrets import choice

def print_rest_rating(rest_ratings):
    for rest in sorted(rest_ratings):
        print(f'{rest} is rated a {rest_ratings[rest]}.')

def read_rest_rating(filename, rest_ratings):
    with open('scores.txt') as f:    
        for line in f:
            line = line.rstrip('\n')
            rest, rating = line.split(':')
            rest_ratings[rest] = rating    
    f.close()

def create_rating():
    new_rating = int(input('Please enter the rating for the restaurant: '))
    while new_rating < 1 or new_rating > 5:
        new_rating = int(input('Please enter a rating between 1 and 5: '))
    return new_rating

rest_ratings = {}

read_rest_rating("scores.txt", rest_ratings)


print("What would you like to see?")
print("1: Seeing all the ratings")
print("2: Adding a new restaurant")
print("3: Update a Random Restaurant’s Rating")
print("q: Quitting")

while True:
    choice = input('Please print your choise: ')

    if choice == "1":
        print_rest_rating(rest_ratings)
    elif choice == "2":
        new_rest = input('Please enter a new restaurant name: ')
        rest_ratings[new_rest] = create_rating()
        print_rest_rating(rest_ratings)
    elif choice == "3":
        print(rest_ratings.keys())
        random_restaurant = random.choice(list(rest_ratings.keys()))
        print(random_restaurant)
        rest_ratings[random_restaurant] = create_rating() 
        print_rest_rating(rest_ratings)
    else:
        print("quit")
        break

    
