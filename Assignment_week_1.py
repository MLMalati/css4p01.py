# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:04:32 2024

@author: MLM
"""

import pandas as pd 
#retrieve file from known path
data = pd.read_csv("C:/Users/MLM/Desktop/Data Science/CHPC-2024/Test/Test_Assignement/movie_dataset.csv")
print(data)
print(data.info())
#there are missing rows on the imported data file, thus dropping is a good option
data.dropna(inplace = True)
data = data.reset_index(drop=True)
print(data)
print(data.info())

#to get the highest movie rating (we focus on the rating column)
#the filter command can be used for this work. 
HM3 = data['Rating'].max()
# above this cannot give me movie title. Thus, try below 
filter_HM1 = data[data['Rating'] == data['Rating'].max()]
print(filter_HM1[['Title', 'Rating']])

#Q2 calculating revenue, we can assume the average
avg_revenue = data['Revenue (Millions)'].mean()
print(avg_revenue)

#Q3 The year data requires formating, before calculations can be performed. 
data['Year'] = pd.to_datetime(data['Year'], format='%Y')
# Filter the DataFrame for movies released from 2015 to 2017
filtered_data = data[(data['Year'] >= '2015-01-01') & (data['Year'] <= '2017-12-31')]
#getting the average
avg_revenue_2015_to_2017 = filtered_data['Revenue (Millions)'].mean()
print(avg_revenue_2015_to_2017)

#Q4 number of movies in 2016 can be obtained via the filter function, the raw data was used since after date modification.
import pandas as pd
data_1 = pd.read_csv("movie_dataset.csv")
filter_movies_2016 = data_1[data_1['Year'] == 2016]
no_movies_2016 = len(filter_movies_2016)
print(filter_movies_2016)

#Q5 Chris Nolan Movies, using the filter function 
director_m = data[data['Director'] == "Christopher Nolan"]
no_movies_Nolan = len(director_m)
print(director_m)

#Q6 Movies with 8.0 rating, 
#importing from the transfoemed data the answer is 70, but from the raw data the answer is 70
movie_ratings = data_1[data_1['Rating'] >= 8.0]
print(movie_ratings)

#Q7 median rating of the work, 1-filter in director and calculate median.
director_m = data[data['Director'] == "Christopher Nolan"]
median_rating_Nolan = director_m['Rating'].median()
print(median_rating_Nolan)

#Q8  Calculate the average rating for the years and then filter by year 
avg_rat_year = data_1.groupby('Year')['Rating'].mean()
YHA_rating = avg_rat_year.idxmax()
HA_rating = YHA_rating.max()
print(HA_rating)

#Q9 percentage increase calculated from 2006 to 2016
import pandas as pd
data_1 = pd.read_csv("movie_dataset.csv")
filter_movies_2016 = data_1[data_1['Year'] == 2016]
no_movies_2016 = len(filter_movies_2016)
filter_movies_2006 = data_1[data_1['Year'] == 2006]
no_movies_2006 = len(filter_movies_2006)
percent_increase = ((no_movies_2016 - no_movies_2006) / no_movies_2006) * 100
print(percent_increase)

#Q10 To split the actors the .str.split command should be used and the seperator is a comma(,)
actors_data = data['Actors'].str.split(',', expand=True)
#to create a column entry for each actor 
actors_col = actors_data.values.flatten()
#to look for the frequency of the actors in the created entries
actors_freq = pd.Series(actors_col).value_counts()
#the common actor we need to look for the highest frequency
com_actor = actors_freq.idxmax()
print(com_actor)

#Q11 Similar to the previous command the .str.split command will be used
genres_data = data['Genre'].str.split(',', expand=True)
#to create a column entry for each actor 
genres_col = genres_data.values.flatten()
#count of unique generes 
genres_count = len(set(genres_col))
print(genres_count)


#Q12 Data abalysis 
#Numerical features for correlation Rank, year, runtime, rating, votes, revenue and metascore. 
#1. worked on transformed data
Numerical_feat = data[['Rank', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]
# correlation can be deduced by finding the correlation matrix 
matrix = Numerical_feat.corr()
print(matrix)
#2. worked on raw data
Numerical_feat = data_1[['Rank', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]
# correlation can be deduced by finding the correlation matrix 
matrix = Numerical_feat.corr()
print(matrix)

