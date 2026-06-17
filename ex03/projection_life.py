import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load



def load_pop (df : pd.DataFrame, df2 : pd.DataFrame) -> None:
    
    x_GPD = (
        df['1900']
    )

    y_life_expectancy = (
        df2['1900']

    )
    x = x_GPD
    y = y_life_expectancy
    plt.scatter(x, y)
    
    plt.title('1900')
    plt.yticks(range(20, 60, 5))
    plt.ylabel('Life Expectancy')
    plt.xscale('log')
    plt.xticks([300, 1000, 10_000], ['300', '1k', '10k'])
    plt.xlabel('Gross domestic product')
    plt.show()

def main():
    df = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df2 = load('life_expectancy_years.csv')
    load_pop(df,df2)
    # d = df['1900'].head()
    # d2 = df2['1900'].head()
    # print(d)
    # print(d2)
if __name__ == ("__main__"):
    main()