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


def subset_by_rows():
    print(stats[21:26])
    print(stats[2:3])
    print(stats[0:10])


def reverse_dataframe():
    print(stats[::-1])


def get_only_twentieth_country():
    print(stats[::20])


def main():
    get_only_twentieth_country()


if __name__ == '__main__':
    main()
