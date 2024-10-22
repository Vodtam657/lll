import pandas as pd
df = pd.read_csv("IMDB-Movie-Data.csv")
print(df.info())

df["Rating"] = df["Rating"].fillna(-1)









print(len(df[pd.isnull(df["Rating"])]))
def make_size(size):
    if size[-1] == "M":
        return float(size[:])
    elif size[-1] == "k":
        return float(size[:-1])/1024
    return 0
df["Size"] = df["Size"].apply(make_size)
print(df[df["Category"] == "TOOLS"]["Size"].max())
