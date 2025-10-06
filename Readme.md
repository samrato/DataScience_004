---

# FIFA 21 Data Wrangling & Tableau Preparation

## Project Overview

This project cleans and prepares the FIFA 21 raw dataset for analysis and visualization in Tableau. The goal is to transform messy raw data into a clean, structured format suitable for exploring player performance, market value, and club/nationality insights.

---

## Features

* Cleans categorical and numeric columns.
* Converts monetary values (Value, Wage) into numeric format.
* Handles missing and unrealistic values.
* Adds calculated fields like `Value_per_OVA`, `Wage_per_OVA`, and `Age_Group`.
* Produces a clean CSV ready for Tableau dashboards.

---

## Dataset

* **File:** `fifa21 raw data v2.csv`
* **Size:** 18,979 entries, 77 columns
* **Key Columns Used:**

  * Player Info: `Name`, `LongName`, `Nationality`, `Club`, `Positions`, `Preferred Foot`, `Best Position`
  * Ratings: `OVA`, `POT`, `PHY`, `PAC`, `SHO`, `PAS`, `DRI`, `DEF`
  * Financials: `Value`, `Wage`
  * Others: `Age`

---

## How It Works

### Steps Performed in `wrangle_fifa_data`:

1. **Load CSV**

   * Load the raw FIFA 21 dataset into a Pandas DataFrame.
   * Rename special columns (like `↓OVA`) for easier reference.

2. **Clean Categorical Columns**

   * Strip spaces and standardize capitalization.
   * Fill missing values with `'Unknown'`.

3. **Clean Numeric Columns**

   * Convert ratings, age, and skill stats to numeric.
   * Invalid entries are converted to NaN.

4. **Convert Monetary Columns**

   * Remove symbols and letters (`€`, `M`, `K`).
   * Convert to float and scale according to millions or thousands.

5. **Handle Missing and Unrealistic Data**
   * Drop rows missing `OVA`, `POT`, or `Age`.
   * Remove rows with impossible values (e.g., Age <16 or >49, OVA/POT ≤ 0).
6. **Add Calculated Fields**
   * `Value_per_OVA` → market value efficiency
   * `Wage_per_OVA` → wage efficiency
   * `Age_Group` → categorized player age groups for analysis
7. **Save Cleaned CSV**
   * Saves as `fifa21_cleaned.csv` for Tableau or other visualization tools.

---
## Usage

```python
from wrangle_fifa import wrangle_fifa_data
# Clean FIFA 21 dataset
df_cleaned = wrangle_fifa_data("fifa21 raw data v2.csv")
```

* The function returns a cleaned DataFrame.
* A new CSV `fifa21_cleaned.csv` is created for Tableau dashboards.
---
## Insights for Tableau
You can use the cleaned dataset to build dashboards on:
1. **Player Ratings & Potential**
   * Scatter plots of OVA vs POT
   * Histograms of OVA distribution
   * Boxplots per position
2. **Value & Wage Analysis**
   * Total value per club
   * Average value by nationality
   * Value_per_OVA and Wage_per_OVA comparisons
3. **Age & Demographics**
   * Age distribution histograms
   * Age group performance per position
   * Preferred foot distribution
4. **Position & Skill Stats**
   * Compare skill stats per position using radar or heatmap charts
   * Correlation of OVA with individual skill attributes
5. **Club & Nationality Insights**
   * Club strength comparison (Avg OVA/POT)
   * Tree map of nationality vs player count & avg rating
   * ROI of players by club using Value_per_OVA
---
## Requirements
* Python 3.x
* Pandas
* Jupyter Notebook (optional, recommended for visualization prep)
---
## Notes
* This project is designed for **data cleaning and preparation**. Tableau or Python visualizations can be built on the cleaned dataset.
* Ensure the raw CSV file `fifa21 raw data v2.csv` is in the same directory as the notebook or script.

---

