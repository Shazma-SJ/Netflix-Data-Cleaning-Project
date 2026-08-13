import pandas as pd

df=pd.read_csv("netflix_cleaned.csv")
print(df['Country'].isnull().sum())
###  Clean Country information
df=df.dropna(subset=['Country'])
df["Country"]=df["Country"].str.split(", ")
df=df.explode("Country")
df["Country"]=df["Country"].str.strip()
print(df)
print(df["Country"])

### Calculate Content Count by Country
count_countries=df.groupby("Country").size().reset_index(name="Count_titles")
count_countries=count_countries.sort_values("Count_titles", ascending=False)
print(count_countries)

### Top Content Producings Countries
top10=count_countries.head(10)
print(top10)

###  Chart and rankings
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.bar(top10["Country"], top10["Count_titles"])
plt.title("Top10 Countries by Content On Netflix", size=20)
plt.xlabel("Top 10 Countries by Netflix", size=16)
plt.ylabel("Numbers of Titles", size=16)
# plt.gca().invert_yaxis()
plt.show()

total=count_countries["Count_titles"].sum()
top5_sum=count_countries.head(5)["Count_titles"].sum()
top5_percentage=(top5_sum/total)*100
print(f"Top 5 countries make up {top5_percentage:.1f}% of total.")


##   __BUSINESS INSIGHT__

"""
Business Insights: Country-Wise Netflix Content Analysis
        -- Top5 Countries account for 64.2% and United States leads global content volume
        with 3240 titles, followed by india(1057) and then UK(538).

        -- Netflix's content is heavily skewed toward the US market, which holds roughly 3x the content
        volume of the next-highest country, indicating US-first content strategy rather than balanced global investment
        
        -- Pakistan's content volume ranks above larger economies like Canada and France, which warrants validation
        
        -- There are 287 titles categorized as unknowns representing a noticeable gap in content volume.
        
        -- The remaining 81 countries share just  35.8% of total content, which is ranking higher than canada and Japan,
        revealing Netflix global footprints is wide but shadow   
"""