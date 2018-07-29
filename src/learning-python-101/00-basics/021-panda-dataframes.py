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


def arithmetic_operations():
    result = stats.Birthrate * stats.Internetusers
    print(result.head())


def add_columns():
    stats['CustomCalc'] = stats['Birthrate'] * stats['Internetusers']
    print(stats.head())
    new_stats = stats.drop('CustomCalc', 1)
    print(new_stats.head())


def access_individual_elements():
    print(stats.iat[0, 1])  # get by column key
    print(stats.iat[3, 2])
    print(stats.iat[15, 3])
    print(stats.iat[22, 4])
    print(stats.at[22, 'Birthrate'])  # get by label
    print(stats.at[55, 'CountryName'])
    sub10 = stats[::10]
    print(sub10.iat[10, 0])  # iat retrieves from the new object sub10
    print(sub10.at[10, 'CountryName'])  # at retrieves from the original 10


def filtering():
    internet_users_filter = stats.Internetusers < 2
    print(stats[internet_users_filter])

    print(stats[stats.Birthrate > 40])

    print(stats[(stats.Birthrate > 40) & stats.Internetusers < 2])

    print(stats[stats.IncomeGroup == 'High income'])
    print(stats.IncomeGroup.unique())

    print(stats[stats.CountryName == 'Malta'])


def main():
    rename_columns()
    access_individual_elements()


if __name__ == '__main__':
    main()
