import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_cleaned.csv")
count_type=df["Type"].value_counts()
print("Data counts: ",count_type)


###      Bar chart (Number of movies vs tv shows)

plt.figure(figsize=(6,5))

##       Pie Chart (proportion of movies vs tv shows)

count_type.plot(kind='pie', autopct='%1.1f%%')

plt.title('Proportion of Movies vs TV Shows', fontsize=14, fontweight='bold')
plt.ylabel('') # Hides the default 'Type' column label on the side
plt.show()

percentage=df["Type"].value_counts(normalize=True)*100
print("Percentages: ", percentage, "%")

## ------------------------------------------------------------- ##


