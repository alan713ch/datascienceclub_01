# Author: Alan Izar
# 08/01/2016

# Goal: to read a CSV file and extract data from it

import pandas as pd  # import pandas and assign it the name pd

path = r'C:\Users\izara\PycharmProjects\reading csv data\SRC\CSV data\pokemon.csv'  # specifying path for pokemon file
pokemon = pd.read_csv(path)  # Extracting the data into an array

print(pokemon.head())  # print first three observations

print('\n' + pokemon.at[0, 'identifier'])  #how to extract a specific data point

'\n'
print(pokemon['height'].mean()) #mean height
print(pokemon['weight'].mean()) #mean weight
'\n'
print(pokemon['height'].__class__())  #data type of height
print(pokemon['identifier'].__class__())  #data type of identifier
'\n'
print(pokemon['height'].min())  #descriptive statistics: min, max, mean, median, variance
print(pokemon['height'].max())
print(pokemon['height'].mean())
print(pokemon['height'].median())
print(pokemon['height'].var())