#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time

# url template for scraping
base_url = "http://www.basketball-reference.com/draft/NBA_{year}.html"

# initialize large DataFrame to append individual draft classes into
draft_df = pd.DataFrame()

# create a list of strings that indicate second round pick
pick_range = list(range(31,61))
pick_range = [str(x) for x in pick_range]

# append individual draft classes into DataFrame
for year in range(2005, 2015):
    # insert year into url to scrape by year
    url = base_url.format(year=year)

    # get the html for the url we use and create the soup object to parse the html
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html5lib')

    # parse through <tr> tag in html for the headers to have our DataFrame labels
    column_headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]

    # Rk does not get caught by player_data, so remove it for consistency
    column_headers.remove('Rk')

    # get our player data from <td> tag in html
    data_rows = soup.findAll('tr')[2:] 
    player_data = [[td.getText() for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]
    
    # replace empty string values with 0 
    for i in player_data:
        i[:] = [0 if x=='' else x for x in i]
    
    # remove empty data that was grabbed from scraping empty rows
    counter = 0
    length = len(player_data)
    while(counter<length):
        if(player_data[counter]==[]):
            player_data.remove(player_data[counter])
            # as an element is removed
            # so decrease the length by 1
            length = length - 1  
            # run loop again to check element
            # at same index, when item removed 
            # next item will shift to the left 
            continue
        counter = counter + 1
    
    # only access 2nd rounders
    player_data = [x for x in player_data if x[0] in pick_range]
        
    # insert data into pandas DataFrame
    year_df = pd.DataFrame(player_data, columns=column_headers)

    # make draft classes distinct by inserting new column into DataFrame
    year_df.insert(0, 'Draft Year', year)

    # Append to the original DataFrame
    draft_df = draft_df.append(year_df, ignore_index=True)

    # Pause program in order to not overload servers and get blacklisted
    time.sleep(45)

# Convert data to proper data types (strings to int/float)
draft_df = draft_df.infer_objects()

# Get rid of the rows full of null values
draft_df = draft_df[draft_df.Player.notnull()]

# Replace NaNs with 0s
draft_df = draft_df.fillna(0)

# Rename Columns
draft_df.rename(columns={'WS/48': 'WS_per_48'}, inplace=True)

# Change % symbol
draft_df.columns = draft_df.columns.str.replace('%', '_Perc')

# Add per_G to per game stats
draft_df.columns.values[15:19] = [draft_df.columns.values[15:19][col] + 
                                  "_per_G" for col in range(4)]

draft_df.infer_objects()

# download the csv file
draft_df.to_csv("second_rounders_2005-14.csv")

