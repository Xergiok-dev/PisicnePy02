import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def parse_pop(value: str) -> float:
    if isinstance(value, str):
        if value.endswith('B'):
            return float(value[:-1]) * 1_000_000_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('k'):
            return float(value[:-1]) * 1_000
    return float(value)

def load_pop (df : pd.DataFrame) -> None:
    
    rowFrance = (
        df[df['country'] == 'France'].iloc[0,1:].apply(parse_pop)
    )
    rowBelg = (
        df[df['country'] == 'Belgium'].iloc[0,1:].apply(parse_pop)
    )
    plt.plot(rowFrance.index.astype(int),
             rowFrance.values, 
             label='France')
    
    plt.plot(rowBelg.index.astype(int),
            rowBelg.values, 
            label='Belgium')
    
    plt.title('Population projections')
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.xlabel('Year')
    plt.yticks([20_000_000, 40_000_000, 60_000_000], ['20M', '40M', '60M'])
    plt.ylabel('Population')
    plt.legend()
    plt.show()

def main():
    df = load('population_total.csv')
    load_pop(df)


if __name__ == ("__main__"):
    main()