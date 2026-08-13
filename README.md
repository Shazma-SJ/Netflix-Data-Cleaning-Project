
#     Netflix Data Analysis Project

##  Overview:    
This project analyzes the Netflix titles dataset to uncover trends in content type, country-wise distribution, release patterns, ratings, and genres. It was completed as part of a data analytics internship at Auspify Technologies, using Python (pandas, matplotlib, seaborn) for data cleaning, exploratory analysis, and visualization.
##  Dataset
        source:Netflix-dataset.csv
        Rows:  8790        
        Columns: 10(show_id, type, title, director, country, date_added, 
        release_year, rating, duration, listed_in)

##  Project Structure
```
        netflix_Data_Analysis_Project/
├── data/
│ └── netflix_dataset.csv
├── scripts/
│ ├── task1_data_cleaning.py
│ ├── task2_content_type.py
│ ├── task3_country_analysis.py
│ ├── task4_trend_analysis.py
│ └── task6_dashboard.py
├── outputs/
│ ├── SS/Charts
│ └── dashboard/
├── README.md
└── requirements.txt
```

### Tasks Breakdown 

### Task 1: Data Cleaning
- Handled missing values in `Director` and `Country` column.
- Replace 'Unknowns' with 'Not Given'.
- Removed duplicates, standardized formats
- Capitalize the Initials of Column's Names
- Output: cleaned dataset ready for analysis

### Task 2: Content Type Analysis
- Calculate Total Number of Movies and TV Shows
- Compared distribution of Movies vs TV Shows in Pie Chart
- Key finding: e.g. 69.7% of content is Movies vs 30.3% TV Shows"

### Task 3: Country-wise Analysis
- Identified top countries producing Netflix content
- United States leads global content volume with 3240 titles
- 287 titles categorized as unknowns
- Key finding: e.g. "US, India, UK are top 3 contributors"

### Task 4: Trend Analysis
- Analyzed content additions over time (by year)
- Organize content by release year
- Identified growth and decline trends
- Created a line chart visualization 
- Key finding: e.g. "Content additions peaked in 2017-2018

### Task 6: Capstone Dashboard
- Combined all insights into a single multi-chart dashboard using gridspec
- See: `outputs/dashboard/`

## Key Insights
- Movies Dominates netflix y 69.7% of total Content Library.
- A few Countries Contribute the majority of content
- Netflix Content release increases steadily from 2013-2019
- Recent years continue to add a significant number of titles.

## Tools & Libraries
- Python
- pandas
- matplotlib
- VS Code

## How to Run
1. Clone this repository
https://github.com/Shazma-SJ/Netflix-Data-Cleaning-Project.git
2. Install dependencies
3. Run scripts in order (task1 through task6)

## Author
Shazma Shaheen -Data Analytics Intern at Auspify Technologies
Linkedin:
linkedin.com/in/shazma-shaheen
