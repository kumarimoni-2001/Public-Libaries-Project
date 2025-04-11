import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/monis/Downloads/Public_Libraries (1).csv");
print(df.info())


#Cleaning the dataset
missing = df.isnull().sum()
print("Missing values:\n", missing[missing > 0])


#dropping column with 100% missing values
df.drop(columns=['Registrations Per Capita Served', 'Use of Public Internet Computers'], inplace=True, errors='ignore')

# Filling missing values with median
columns_to_fill = [
    'Population of Service Area',
    'Reference Questions',
    'Library Visits Per Capita Served',
    'Total Library Visits',
    'Total Program Attendance & Views Per Capita Served',
    'Total Program Attendance & Views',
    'Total Programs (Synchronous + Prerecorded)',
    'Wages & Salaries Expenditures',
    'Collection Per Capita Served',
    'Percent of Residents with Library Cards',
    'Tax Appropriation Per Capita Served',
    'AENGLC Rank',
    'Operating Income Per Capita',
    'Total Registered Borrowers',
    'Operating Expenditures Per Capita',
    'Library Materials Expenditures',
    'Total Collection',
    'Town Tax Appropriation for Library',
    'Circulation Per Capita Served',
    'Operating Expenditures',
    'Total Operating Income',
    'Total Circulation'
]

for col in columns_to_fill:
    df[col] = df[col].fillna(df[col].median())

print("Remaining missing values:\n", df.isnull().sum()[df.isnull().sum() > 0])

# Save cleaned data to a new CSV file
df.to_csv("C:/Users/monis/Downloads/Public_Libraries (1).csv", index=False);


df['Reference Questions Per Capita Served'] = df['Reference Questions Per Capita Served'].fillna(df['Reference Questions Per Capita Served'].median())


#Loading the cleaned dataset
df = pd.read_csv("C:/Users/monis/Downloads/Public_Libraries (1).csv");

# OBJECTIVE1:Scatter Plot: Relationship between Total Programs (Synchronous + Prerecorded) and Total Program Attendance & Views
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Total Programs (Synchronous + Prerecorded)', 
    y='Total Program Attendance & Views', 
    data=df,
    color='purple'
)
plt.title('Total Programs vs Total Attendance & Views')
plt.xlabel('Total Programs (Synchronous + Prerecorded)')
plt.ylabel('Total Program Attendance & Views')
plt.grid(True)
plt.tight_layout()
plt.show()





#OBJECTIVE-2: Relationship between Wages & Salaries Expenditures and Total Circulation
# Create bins for Total Circulation (example: divide into 4 categories)
bins = [0, 50000, 100000, 150000, 200000]
labels = ['0-50k', '50k-100k', '100k-150k', '150k-200k']
df['Circulation Range'] = pd.cut(df['Total Circulation'], bins=bins, labels=labels)

# Group by the bins and get the count
circulation_distribution = df['Circulation Range'].value_counts()

# Plotting pie chart
plt.figure(figsize=(8, 8))
colors = sns.color_palette("Set2", len(circulation_distribution))
plt.pie(
    circulation_distribution,
    labels=circulation_distribution.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors
)

# Styling
plt.title('Distribution of Total Circulation in Bins', fontsize=14)
plt.tight_layout()
plt.show()





#Objective 3: Top 10 Counties by Library Visits Per Capita
# Step 1: Group by County and calculate average visits per capita
visits_per_capita = df.groupby('County')['Library Visits Per Capita Served'].mean().reset_index()

# Step 2: Sort and pick top 10
top_visits = visits_per_capita.sort_values(by='Library Visits Per Capita Served', ascending=False).head(10)

# Step 3: Plot
plt.figure(figsize=(12, 6))
sns.barplot(
    x='Library Visits Per Capita Served',
    y='County',
    data=top_visits,
    palette='magma'
)
plt.title('Top 10 Counties by Library Visits Per Capita', fontsize=16)
plt.xlabel('Average Library Visits Per Capita')
plt.ylabel('County')
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()





#OBjective-4:Top 10 Counties by Total Library Visits
# Group and get top 10 counties
county_visits = df.groupby('County')['Total Library Visits'].sum().nlargest(10)

# Colors
colors = sns.color_palette("Set2", len(county_visits))

# Plotting donut chart
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    county_visits,
    labels=county_visits.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'width': 0.4}
)

# Styling
plt.setp(autotexts, size=12, weight='bold')
plt.title('Top 10 Counties by Total Library Visits (Donut Chart)', fontsize=14)
plt.tight_layout()
plt.show()


#Objective-5 Distribution of Collection Per Capita by County

# Create a box plot for Distribution of Collection Per Capita Served by County
plt.figure(figsize=(12, 6))
sns.boxplot(x='County', y='Collection Per Capita Served', data=df, palette='Set2')

# Styling and Titles
plt.title('Distribution of Collection Per Capita by County', fontsize=16)
plt.xlabel('County')
plt.ylabel('Collection Per Capita Served')
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to ensure everything fits
plt.tight_layout()

# Display the plot
plt.show()