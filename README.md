# cleaning-task-IEEE

هعمله ب ai 
# Candy Hierarchy 2017 - Data Cleaning Task 🎃🍬

This repository contains the solution for the data cleaning and analysis task of the **Candy Hierarchy 2017** dataset.

## 📂 Project Structure

*   `candyhierarchy.pdf`: The original survey form from the University of British Columbia (UBC) showing the survey layout.
*   `candyhierarchy2017.xlsx`: The raw dataset containing original survey responses.
*   `doing.py`: The Python cleaning script using `pandas` to filter, clean, and encode the dataset.
*   `final_cleaned_candy_analysis.xlsx`: The final polished dataset containing clean demographics and encoded chocolate preferences.

## 🛠️ Cleaning & Processing Steps

1.  **Column Tidy Up**: Removed irrelevant feedback columns (e.g., 'REASON' columns).
2.  **Age Cleaning**: Filtered and restricted age inputs to a realistic range (5 - 100 years), dropping missing or invalid values.
3.  **Country Standardization**: Grouped and mapped inconsistent country names into clean categories (`USA`, `UK`, `Canada`, `Other`).
4.  **Chocolate Encoding**: Selected 37 specific chocolate columns, filled missing values, and encoded feelings to numeric scores:
    *   `JOY` ➔ `1`
    *   `MEH` ➔ `0`
    *   `DESPAIR` ➔ `-1`
5.  **Output Export**: Generated a clean, fully-formatted dataset consisting only of demographic details and the cleaned chocolate scores.

---
*Task completed as part of the IEEE recruitment/activities.*
