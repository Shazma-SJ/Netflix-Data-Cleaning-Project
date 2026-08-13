import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_cleaned.csv")
print(df)

###   to check correct file is opened

print(df.shape)
print(df.head())
print(df["Release Year"].dtype)


###   Organize content by release year and calculate yearly content

yearly_content=df["Release Year"].value_counts().sort_index()
print(yearly_content)

###   Growth and decline trends   ###

yearly_growth=yearly_content.pct_change()*100
print(yearly_growth.round(2))
print(df["Date Added"].max())

import matplotlib.ticker as ticker

###   Trend Visualization   ###
plt.figure(figsize=(12,8))
plt.plot(yearly_content.index, yearly_content.values, marker="o", markersize=4)
plt.title("Netflix Content Analysis by release year", size=20)
plt.xlabel("Release year", size=16)
plt.ylabel("Number of titles", size=16)

###   X-Axis: with gap of 10 years  ###
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))

###   Y-axis: with gap of 100 titles  ###
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(100))
plt.grid(True)
plt.show()

###   Netflix content arranged by yearly release in csv

# df_sorted=df.sort_values("Release Year")
# df_sorted.to_csv("netflix_yearly_summary.csv", index=False)