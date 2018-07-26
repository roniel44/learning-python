import pandas as pd


def main():
    stats = pd.read_csv('files/DemographicData.csv')
    print(len(stats))
    print(stats.columns)
    print(len(stats.columns))
    print(stats.head())  # top 5
    print(stats.head(6))  # top 6
    print(stats.tail())
    print(stats.info())
    print(stats.describe())
    print(stats.describe().transpose())


if __name__ == '__main__':
    main()
