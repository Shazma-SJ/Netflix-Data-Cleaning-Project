import pandas as pd

##       step1 Import dataset using python and pandas

df=pd.read_csv("netflix-dataset.csv")
print(df.head())
print(df.info())

##   Step2: identify and handle missing values
##   first count "NOT GIVEN"
not_given_count= (df=="Not Given").sum()
print(not_given_count)
print(df.replace("Not Given", pd.NA, inplace=True))

#      #Director has highest 'Not Given" rows. Replace it with "Unknown"

df["director"]=df["director"].fillna("Unknown")
print(df["director"])

##    Country; Replace "Not Given" wth "Unknown"
df["country"]=df["country"].fillna('Unknown')
print(df["country"])
print(df.isnull().sum())

##             check For duplicate rows
count_duplicates=df.duplicated().sum()
print(f"Duplicate rows:{count_duplicates}")           ## No Duplicate row in that dataset

##  Standarize/formatting inconsistencies
##  check case and whitespace in 'Country" column

df["country"]=df["country"].str.strip().str.title()
print(df["country"])

df["country"]=df["country"].replace({"USA": "United States", "US": "United States"})
print(df["country"])

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns)


df["type"]=df["type"].str.strip()
print(df["type"])

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
print(df["date_added"])

df["duration_minutes"]=df.loc[df["type"]== "Movie", "duration"].str.extract(r'(\d+)').astype(float)
print(df["duration_minutes"])

df["duration_seasons"]=df.loc[df["type"]=="TV Show","duration"].str.extract(r'(\d+)').astype(float)
print(df["duration_seasons"])

###       to check is there any other column format
print(sorted(df["country"].unique())) 
print(sorted(df["type"].unique()))
print(sorted(df["rating"].unique()))         ## they are clean

print(df.dtypes)

df= df.rename(columns={
    "show_id": "Show ID",
    "type": "Type",
    "title": "Title",
    "director": "Director",
    "country": "Country",
    "date_added": "Date Added",
    "release_year": "Release Year",
    "rating": "Rating",
    "duration": "Duration",
    "listed_in": "Listed In",
    "duration_minutes": "Duration Minutes",
    "duration_seasons": "Duration Seasons"
})
df.to_csv("netflix_cleaned.csv", index=False)