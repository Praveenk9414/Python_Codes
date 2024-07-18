# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 
# def add_new_country(country, visits, list_of_cities):
#   # travel_log.extend({travel_log["country"]: country, travel_log["visits"]:visits, travel_log["list_of_cities"]:list_of_cities})
#   travel_log.append({"country": country, "visits":visits, "cities":list_of_cities})
#   print(travel_log)
# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def auction_winner(auction_list):
    max = 0
    for i in range(len(auction_list)):
        if auction_list[i]["bid_amt"] > max:
            max = auction_list[i]["bid_amt"]
            name = auction_list[i]["user_name"]
    print(f"The winner is {name} with a bid of ${max}")

auction_list = []
max = 0
new_bid = 'yes'
while new_bid == 'yes':
    name = input("Enter your name? : ")
    bid = int(input("Enter your bid amount? : "))
    auction_list.append({"user_name": name, "bid_amt": bid})
    new_bid = input("Is there is anyone else who want to bid yes/no :").lower()
    clear_screen()

auction_winner(auction_list)

