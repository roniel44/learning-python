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


def display_violin_plots_sample():
    f, axes = plt.subplots(2, 2, figsize={12, 6})
    sns.violinplot(data=movies, x='Genre', y='CriticRating', ax=axes[0, 0])
    sns.boxplot(data=movies, x='Genre', y='CriticRating',  ax=axes[0, 1])
    sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating', ax=axes[1, 0])
    sns.boxplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating',  ax=axes[1,  1])
    plt.show()


def display_facet_grid1():
    g = sns.FacetGrid(data=movies, row='Genre', col='Year', hue='Genre')
    kws = dict(s=50, linewidth=0.5, edgecolor='black')
    g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
    g.set(xlim=(0, 100), ylim=(0, 100))
    for ax in g.axes.flat:
        ax.plot((20, 60), (20, 60), c='gray', ls='--')

    g.add_legend()
    plt.show()


def main():
    rename_columns()
    display_facet_grid1()


if __name__ == '__main__':
    main()
