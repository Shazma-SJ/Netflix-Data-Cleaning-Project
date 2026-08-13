# ============ COMBINED DASHBOARD (Tasks 1-4) ============
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

os.makedirs('outputs', exist_ok=True)

df=pd.read_csv("netflix_cleaned.csv")
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.3)

# Panel 1: Top 10 Countries (bar chart) — Task 3
ax1 = fig.add_subplot(gs[0, 0])
df['Country'].value_counts().head(10).plot(kind='bar', ax=ax1, color="black")
ax1.set_title('Top 10 Countries by Netflix Content', fontsize=11, fontweight='bold')
ax1.set_xlabel('')
ax1.set_ylabel('Number of Titles')
ax1.tick_params(axis='x', rotation=75, labelsize=7)

# Panel 2: Content by Release Year (line chart) — Task 4
ax2 = fig.add_subplot(gs[0, 1])
df['Release Year'].value_counts().sort_index().plot(kind='line', ax=ax2, marker='o', markersize=3)
ax2.set_title('Netflix Content by Release Year', fontsize=11, fontweight='bold')
ax2.set_xlabel('Release Year')
ax2.set_ylabel('Number of Titles')

# Panel 3: Movies vs TV Shows (pie chart) — Task 2
ax3 = fig.add_subplot(gs[1, 0])
df['Type'].value_counts().plot(kind='pie', ax=ax3, autopct='%1.1f%%', colors=['skyblue','orange'])
ax3.set_title('Distribution of Movies and TV Shows', fontsize=11, fontweight='bold')
ax3.set_ylabel('')

# Panel 4: Findings + Recommendations (text box)
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
summary_text = (
    "Key Business Findings\n"
    "• Movies dominate Netflix's by 69.7% of total content library\n"
    "• A few countries contribute the majority of content\n"
    "• Netflix content release increases streadily from 2013-2019\n"
    "• Recent years continue to add a significant number of titles\n\n"
    "Business Recommendations\n"
    "• Continue investing in high-performing content markets\n"
    "• Expand content acquisition in underreported regions\n"
    "• Maintain a balanced mix of Movies and TV Shows"
)
ax4.text(0, 1, summary_text, fontsize=10, va='top', ha='left', wrap=True)

# Title
fig.suptitle('Netflix Data Analysis Project', fontsize=16, fontweight='bold', y=0.98)

plt.savefig("outputs/task6_dashboard_tasks1to4.png", dpi=150, bbox_inches='tight')
plt.close()