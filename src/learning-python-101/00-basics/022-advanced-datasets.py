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


def display_distplot_sample():
    sns.set_style('darkgrid')
    sns.distplot(movies.AudienceRating, bins=15)
    plt.show()


def display_pyplot_hist():
    sns.set_style('white')
    plt.hist(movies.AudienceRating)
    plt.show()

def display_lmplot_sample():
    sns.lmplot(data=movies, x='CriticRating',
               y='AudienceRating', fit_reg=False, hue='Genre',
               aspect=1, size=7)
    plt.show()


def display_kde_sample():
    sns.kdeplot(movies.CriticRating,
               movies.AudienceRating, shade=True)
    plt.show()


def display_kde_with_subplot_sample():
    sns.set_style('dark')
    f, axes = plt.subplots(4, 4, figsize={12, 6}, sharex=True, sharey=True)

    sns.kdeplot(movies.BudgetMillions, movies.CriticRating, shade=True, ax=axes[0, 2])  # y, x
    sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, shade=True, ax=axes[2, 1]).set(xlim=(-20, 160))  # y, x
    plt.show()


def main():
    rename_columns()
    display_kde_with_subplot_sample()


if __name__ == '__main__':
    main()
