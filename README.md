# NBA Second Round Picks Analysis

## Summary
This project analyzed the careers of second round picks, drafted from 2005-2014. This range was taken so there is adequate time to analyze the total career, as the careers of most of the players have been established and are not projected for leaps/drops in production outside of typical player development.

## Tools Used
* Language: Python

* I used [Jupyter Notebook](https://jupyter.org/ "Jupyter Notebook") to write the programs, making it easier to see the data I was using when working with Pandas DataFrames, DataScience Tables, and plots generated by the linear regression tools. 

* Python Packages: urllib, bs4, pandas, datascience, numpy, statistics, matplotlib, seaborn, sklearn

## Gathering Data
To access the [data](second_round_scraper.ipynb), I web-scraped [Basketball Reference](https://www.basketball-reference.com/ "Basketball Reference"). 

I used the draft archives from 2005 through 2014, and filtered the data to only access second-round picks and converted it to a [csv file](second_rounders_2005-14.csv).

## Basic Statistics
With the data, I started looking for some basic statistics/fun facts. Using the datascience module, I converted the csv into a table, so I proceeded to uncover some interesting statistics that can be found [here](basic_stats.ipynb).

## Simple Regression
I wanted to see the relationship between pick position and [value over replacement player (VORP)](http://sonicscentral.com/vorp.html), and advanced statistic I felt would summarize the career and effect of a player on the NBA. 

My method can be seen [here](simple_regression.ipynb).

As seen in the high error values, simple regression is not an accurate tool to predict draft position based on VORP.

## Multiple Regression
I proceeded to use multiple regression, to see whether draft position can be predicted using the tool by analyzing [value over replacement player (VORP)](http://sonicscentral.com/vorp.html), [BPM (box plus-minus)](https://www.basketball-reference.com/about/bpm.html), and total points scored in the player's career.

My method can be seen [here](multiple_regression1.ipynb).

As seen in the high error values, the model was not very accurate, and actually more inaccurate than the simple regression method aforementioned.

## Future Steps
As shown in the models, it is difficult to correlate draft position with a number of career statistics, so I want to change my approach to measure the relative worth of the draft picks (by position) over a five year period, possibly using the [CARMELO model by FiveThirtyEight](https://projects.fivethirtyeight.com/carmelo/).