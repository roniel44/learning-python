import pandas as pd
movies = pd.read_csv('files/Movie-Ratings.csv')
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
print(movies.head())
print(movies.info())

print(movies.describe())

movies.Film = movies.Film.astype('category')
movies.Year = movies.Year.astype('category')
print(movies.info())

print(movies.Year.cat.categories)
