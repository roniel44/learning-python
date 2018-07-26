import pandas as pd
stats = pd.read_csv('files/DemographicData.csv')


def basic_functions():
    print(len(stats))
    print(stats.columns)
    print(len(stats.columns))
    print(stats.head())  # top 5
    print(stats.head(6))  # top 6
    print(stats.tail())
    print(stats.info())
    print(stats.describe())
    print(stats.describe().transpose())


def rename_columns():
    print(stats.columns)
    stats.columns = ['CountryName', 'CountryCode', 'Birthrate', 'Internetusers', 'IncomeGroup']
    print(stats.head())


def main():
    rename_columns()


if __name__ == '__main__':
    main()
