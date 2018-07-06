#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 18:08:34 2018

@author: Chris
"""
"""
Statistics Assignment: Apartment Search tool

This assignment will help us solidify what we have learned so far about data
manipulation and statistics

Using the Airbnb dataset (located in data/airbnb.csv), we are going to make a script
with the following functionalities:
*******************************************************************************
Functionality 1: Neighbourhood information
- Given a neighbourhood, the tool will provide the following information to the user
  - Total number of available listings in the neighbourhood
  - Number of rooms broken down per listing type
  - Average Room Price
  - Price quartiles

For example if we run the script like;

"python statistics_assignment.py information Belém"

The script will print out information about Belem.

*******************************************************************************
Functionality 2: Apartment Search.
This functionality will help the user to find an appropriate listing. It will ask
the user different listing requirements:
- desired price range
- desired number of rooms (a range)
- a list of desired neighbourhoods
If the user doesnt specifiy any of the requirements (pressing enter without typing anything)
We will consider that the user is indiferent

It will also ask the user if he/she prefers the results sorted by price, by average score
or by number of reviews.

Finally the script will print out the top 10 results matching the desired requirements and sorted
by the desired sorting criteria.

If there are no listings that match the criteria, the script will tell the user that no
listings match the criteria.

For example if we run

"python statistics_assignment.py search"

The script will start prompting us for the requirements and finally print out the results
*******************************************************************************

There should be a main() function that serves as an entrypoint.

When we load the script it will load the dataset and it will be used as the data source.
"""

import pandas as pd
import scipy.stats as stats
import sys
#%%
def load_data():
    return pd.read_csv("./data/airbnb.csv")

def information(neighborhood):
    data = load_data()
 
    hood = data[data.neighborhood == neighborhood]
    
    num_home_apt = hood[hood.room_type == "Entire home/apt"].room_id.count()
    num_priv_room = hood[hood.room_type == "Private room"].room_id.count()
    num_other = hood.room_id.count()-num_priv_room-num_home_apt
    
    total = num_home_apt + num_priv_room+num_other
    
    quartiles  = stats.mstats.mquantiles(hood["price"])
   
    avg_price = hood["price"].mean()
    
    print("The total number of listings is: "+ str(total))
    print("The number of entire homes/apartments is: " + str(num_home_apt))
    print("The number of private rooms is: " + str(num_priv_room))
    print("The average room price is: " + str(avg_price))
    print("The price quartiles are: Q1: " + str(quartiles[0]) + " Q2: " + str(quartiles[1]) + " Q3: " + str(quartiles[2]))



#%%
def search():
   data = load_data()    
    
   requirements_str = input("Please input the desired price range,the room range and desired neighborhoods\
   as two numbers followed by a comma. \nAn example would be: \n\
   min_price,max_price,min_rooms,max_rooms,neighborhood,neighboorhood,etc: ")
   
   sort_type = input("Would you like these sorted by price, overall_satisfaction, or reviews. \
   \n (Please type the option in exactly as written above)")
   
   
   requirements = requirements_str.split(",")
   
   if len(requirements) == 0:
       print(data.sort_value(sort_type).head(10))
   else:
           price_range = [int(requirements[0]), int(requirements[1])]
           room_range = [int(requirements[2]), int(requirements[3])]
           neighborhoods = requirements[4:]
           
           hoods = data[(data.neighborhood.isin(neighborhoods)) & (data.price > price_range[0]) \
           & (data.price < price_range[1]) & (data.bedrooms > room_range[0]) & (data.bedrooms < room_range[1])]
           
           if hoods["room_id"].count == 0:
               print("No listings matching this criteria.")

           else:
               print(hoods.head(10))
#%%
def parse_arguments():
    functionality = sys.argv[1]
        
    if functionality == "information":
            return sys.argv[2]
            
    elif functionality == "search":
            return 0
            
    else:
            return ValueError("One of two functionalities must be selected, information or search")
            

def main(arguments):
    
    if(arguments == 0):
        search()
        
    elif(type(arguments) == type("string")):
        information(arguments)
        
    else:
        ValueError("User input is of wrong type")

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)