import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def load_graph(df: pd.DataFrame) -> None:

    row = df[df['country'] == 'France'].iloc[0, 1:]
    plt.plot(row.index.astype(int), row.values)
    plt.ylabel('France life expectancy projections')
    plt.xticks(range(1800, 2101, 40))
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()

def main():
    df = load('life_expectancy_years.csv')
    load_graph(df)


if __name__ == ("__main__"):
    main()