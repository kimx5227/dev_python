import pandas as pd

anime_df = pd.read_csv(r'D:\dev_python\DataAnalysis\Excel\anime.csv')
rating_df = pd.read_csv(r'D:\dev_python\DataAnalysis\Excel\rating.csv')
print(anime_df.dtypes)
print(anime_df.iloc[0:5, 0])
print(anime_df.loc[0, "anime_id": "type"])
# input to .loc is a boolean array of all rows where truth denotes anime w/ 1 episode
print(anime_df.loc[anime_df["episodes"] == "1"])
# note syntax of filtering multiple columns
print(anime_df.loc[(anime_df["episodes"] == "1") & (anime_df["rating"] == 7.3)])
anime_df["Should I watch"] = anime_df["rating"].apply(
    lambda x: "Yeah" if 7.0 <= x else "sucks big balls")
print(anime_df)
to_drop = ['Should I watch']
anime_df.drop(columns=to_drop, inplace=True)
print(anime_df)
anime_df['Good'] = False
anime_df.loc[anime_df['rating'] > 7.0, 'Good'] = True
print(anime_df)
