🏆 World Cup 2018 Squads Data Cleaner

This project contains a Python function to load, clean, and prepare the 2018 FIFA World Cup squads data for use in analysis tools like Tableau.

📄 File: wrangle_world_cup_squads.py
Function: wrangle_world_cup_squads(file_path)
Purpose

Preprocess the 2018 World Cup squads dataset to ensure it is clean, standardized, and ready for visualization or analysis.

✅ Features

📥 Loads data from an Excel file

🧹 Cleans and standardizes string fields (e.g. team names, player names)

📆 Parses dates and calculates player ages

🔢 Ensures numeric fields like caps and goals are properly typed

🧮 Creates age group categories for better grouping in visual tools

📤 Exports cleaned data to CSV: world_cup_2018_squads_cleaned.csv

📊 Output

The output CSV will include the following cleaned and enriched fields:

Type

Team

Group

Position

Name

Country and Club

DOB

Age

Caps

Goals

Age_Group (<20, 20-24, 25-29, 30+)

🧪 Example Usage
from wrangle_world_cup_squads import wrangle_world_cup_squads

# Load and clean the data
df_cleaned = wrangle_world_cup_squads("world_cup_2018_squads.xlsx")

⚠️ Notes

Rows with missing or invalid DOB, Caps, or Goals will be removed.

Age is calculated based on the current year, which may slightly differ from the exact tournament age.

Make sure the Excel file contains columns named exactly as expected: Type, Team, Group, Position, Name, Country and Club, DOB, Caps, Goals.

🗂️ Files
File	Description
wrangle_world_cup_squads.py	Python script for cleaning the dataset
world_cup_2018_squads.xlsx	Input Excel file with raw data (not included)
world_cup_2018_squads_cleaned.csv	Output CSV file with cleaned data
📈 Suggested Use in Tableau

Once you have the world_cup_2018_squads_cleaned.csv, you can:

Import it into Tableau

Use Team, Group, Position, and Age_Group for filtering/grouping

Visualize age distribution, goals per age group, caps per team, etc.

📌 Requirements

Python 3.7+

pandas

openpyxl (required for reading .xlsx files)

Install dependencies:

pip install pandas openpyxl
