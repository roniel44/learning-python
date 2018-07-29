import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
stats = pd.read_csv('files/DemographicData.csv')
plt.rcParams['figure.figsize'] = 8, 4


def rename_columns():
    stats.columns = ['CountryName', 'CountryCode', 'Birthrate', 'InternetUsers', 'IncomeGroup']


def display_displot():
    sns.distplot(stats['InternetUsers'])
    sns.distplot(stats['Birthrate'])
    plt.show()


def display_lmplot():
    sns.lmplot(data=stats, x='InternetUsers', y='Birthrate')
    plt.show()


def display_lmplot_fit_reg_false():
    sns.lmplot(data=stats, x='InternetUsers', y='Birthrate', fit_reg=False, hue='IncomeGroup')
    plt.show()


def display_boxplot():
    sns.boxplot(data=stats, x='IncomeGroup', y='Birthrate')
    plt.show()


def main():
    rename_columns()
    display_lmplot_fit_reg_false()


if __name__ == '__main__':
    main()
