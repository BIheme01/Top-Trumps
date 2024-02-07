import random
from pip._vendor import requests
from pprint import pprint


print('*' * 5 + ' Welcome to Top Trumps! ' + '*' * 5)
print('*' * 5 + ' Have Fun!! ' + '*' * 5 + '\n')


# A function to get a random character from the Pokemon API
def get_random_pokemon():
    character_number = random.randint(1, 151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(character_number)
    response = requests.get(url)

    characters = response.json()
    pokemon_dict = {}  # Empty dictionary
    if characters: # Error handling in case the random ID doesn't exist
        pokemon_dict['name'] = characters['name']  # Adding the pokemon's stats to the dictionary
        pokemon_dict['id'] = characters['id']
        pokemon_dict['height'] = characters['height']
        pokemon_dict['weight'] = characters['weight']
        # pokemon_dict['base_experience'] = characters['base_experience']
    else:
        print("Pokemon doesnt exist")
    return pokemon_dict


# For loop to have 5 tries and add the wins to the variables
our_player_wins = 0
the_opponent_wins = 0

# Saving the winning scores in lists
opponents_highest_score = []
our_player_highest_score = []

for i in range(5):
    our_player = {
        'pokemon1': get_random_pokemon(),
        'pokemon2': get_random_pokemon(),
        'pokemon3': get_random_pokemon(),
        'pokemon4': get_random_pokemon()
    }

    the_opponent = get_random_pokemon()

    # print(our_player)

    chosen_pokemon = input(f'''Please choose the pokemon you want to play: 
{our_player["pokemon1"]["name"].capitalize()},
{our_player["pokemon2"]["name"].capitalize()}, 
{our_player["pokemon3"]["name"].capitalize()} or 
{our_player["pokemon4"]["name"].capitalize()}: \n''').lower()
    # print(chosen_pokemon)

    chosen_pokemon2 = next((v for k, v in our_player.items() if v['name'] == chosen_pokemon), None)

    # chosen_pokemon_data = None
    # for k, v in our_player.items():
    #     if v['name'] == chosen_pokemon:
    #         chosen_pokemon_data = v
    #         break
    # print(f"Chosen pokemon: {chosen_pokemon2}")


    # Requesting the stats they want to compare from user
    chosen_stats = input("Please select the stats to compare: id, height or weight: \n")


    # Using while loop to make sure the user input is valid
    while not chosen_stats in chosen_pokemon2 or not chosen_stats.isalpha():
        chosen_stats = input("Please enter valid stats: id, height or weight: \n")

    # Comparing the stats from the 2 dictionaries of the 2 players
    if chosen_pokemon2[chosen_stats] > the_opponent[chosen_stats]:
        our_player_wins += 1
        our_player_highest_score.append(chosen_pokemon2[chosen_stats])
        print(f"You have won! Your pokemon, {chosen_pokemon2['name']}, has higher {chosen_stats} then your opponent's!")
        print(f"Your pokemon's {chosen_stats} is {chosen_pokemon2[chosen_stats]}")
        print(f"Your opponent's {chosen_stats} is {the_opponent[chosen_stats]}")

    else:
        the_opponent_wins += 1
        opponents_highest_score.append(the_opponent[chosen_stats])
        print(f"You lost. Your opponent's pokemon, {the_opponent['name'].title()}, has higher {chosen_stats}.")
        print(f"Your pokemon's {chosen_stats} is {chosen_pokemon2[chosen_stats]}")
        print(f"Your opponent's {chosen_stats} is {the_opponent[chosen_stats]}")


# Printing how many times each player won and they player's highest scores
print(f"Our player won {our_player_wins} times, the opponent won {the_opponent_wins} times in the 5 tries")
print(f"The ops max score: {max(opponents_highest_score)}, Our player's max score: {max(our_player_highest_score)}")