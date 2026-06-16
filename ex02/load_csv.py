import pandas as pd

def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # lit le csv
    # print une seule ligne et 10 collones 
    return df

