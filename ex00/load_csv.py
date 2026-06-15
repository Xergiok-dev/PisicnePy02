import pandas as pd

def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # lit le csv
    print(f"Loading dataset of dimensions {df.shape}")
    print(df.head(1).to_string(max_cols=10))
    # print une seule ligne et 10 collones 
    return df

def main():
    load('life_expectancy_years.csv')

if __name__ == ("__main__"):
    main()