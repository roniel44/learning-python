import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
stats = pd.read_csv('files/DemographicData.csv')
plt.rcParams['figure.figsize'] = 8, 4


def rename_columns():
    stats.columns = ['CountryName', 'CountryCode', 'Birthrate', 'Internetusers', 'IncomeGroup']


def seaborne_displot():
    sns.distplot(stats['Internetusers'])
    plt.show()


def seaborne_boxplot():
    sns.boxplot(data=stats, x='IncomeGroup', y='Birthrate')
    plt.show()


def main():
    rename_columns()
    seaborne_boxplot()


if __name__ == '__main__':
    main()
