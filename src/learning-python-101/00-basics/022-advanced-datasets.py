import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

movies = pd.read_csv('files/Movie-Ratings.csv')


def rename_columns():
    movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']


def categorize_per_column():
    print(movies.head())
    print(movies.info())

    print(movies.describe())

    movies.Film = movies.Film.astype('category')
    movies.Year = movies.Year.astype('category')
    print(movies.info())

    print(movies.Year.cat.categories)


def display_joint_plot_sample():
    sns.jointplot(data=movies, x='CriticRating', y='AudienceRating', kind='hex')
    plt.show()


def main():
    rename_columns()
    display_joint_plot_sample()


if __name__ == '__main__':
    main()
