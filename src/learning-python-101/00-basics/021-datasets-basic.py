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
    stats.columns = ['CountryName', 'CountryCode', 'Birthrate', 'Internetusers', 'IncomeGroup']


def subset_by_rows():
    print(stats[21:26])
    print(stats[2:3])
    print(stats[0:10])


def reverse_dataframe():
    print(stats[::-1])


def get_only_twentieth_country():
    print(stats[::20])


def subset_by_columns():
    print(stats['CountryName'].head())
    print(stats.CountryName.head())
    print(stats[['CountryName']].head())
    print(stats[['CountryName', 'CountryCode']].head())  # this follow on order you specified


def subset_by_row_cols():
    print(stats[::-1]['CountryName'].head())


def main():
    rename_columns()
    subset_by_row_cols()


if __name__ == '__main__':
    main()
