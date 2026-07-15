import pandas as pd
import numpy as np

df = pd.read_excel("candyhierarchy2017.xlsx")
df.columns = df.columns.str.strip()

columns_to_drop = [col for col in df.columns if 'REASON' in col.upper()]
df = df.drop(columns=columns_to_drop)

df.dropna(subset=['Q3: AGE', 'Q4: COUNTRY'], inplace=True)

def clean_age(age):
    try:
        age = float(str(age).strip())
        if 5 <= age <= 100:
            return age
        else:
            return np.nan
    except:
        return np.nan

df['Q3: AGE'] = df['Q3: AGE'].apply(clean_age)
df.dropna(subset=['Q3: AGE'], inplace=True)

def clean_country(country):
    country = str(country).lower().strip()
    if 'us' in country or 'america' in country or 'united states' in country:
        return 'USA'
    elif 'uk' in country or 'united kingdom' in country or 'england' in country:
        return 'UK'
    elif 'canada' in country:
        return 'Canada'
    else:
        return 'Other'

df['Q4: COUNTRY'] = df['Q4: COUNTRY'].apply(clean_country)

chocolates_list = [
    '100 Grand Bar', 'Any full-sized candy bar', 'Butterfinger', 'Cadbury Creme Eggs',
    'Caramellos', 'Coffee Crisp', 'Dove Bars', 'Goo Goo Clusters', 'Heath Bar',
    "Hershey's Dark Chocolate", 'Hershey’s Milk Chocolate', "Hershey's Kisses",
    'Kinder Happy Hippo', 'Kit Kat', 'Lindt Truffle', 'Mars', 'Milk Duds',
    'Milky Way', 'Regular M&Ms', 'Peanut M&M’s', "Blue M&M's", "Red M&M's",
    "Green Party M&M's", "Independent M&M's", 'Mr. Goodbar', 'Nestle Crunch',
    'Reese’s Peanut Butter Cups', "Reese's Pieces", 'Reggie Jackson Bar', 'Rolos',
    'Snickers', 'Take 5', 'Three Musketeers', 'Tolberone something or other',
    'Twix', 'Whatchamacallit Bars', 'York Peppermint Patties'
]

chocolate_cols = [col for col in df.columns if col.replace('Q6 | ', '') in chocolates_list]
df[chocolate_cols] = df[chocolate_cols].fillna('MEH')

def encode_feeling(val):
    mapping = {'JOY': 1, 'MEH': 0, 'DESPAIR': -1}
    return mapping.get(val, 0)

for col in chocolate_cols:
    df[col] = df[col].apply(encode_feeling)

chocolate_scores = df[chocolate_cols].sum().sort_values(ascending=False)
chocolate_scores.index = [idx.replace('Q6 | ', '') for idx in chocolate_scores.index]

top_10_loved = chocolate_scores.head(10)
top_10_hated = chocolate_scores.tail(10).sort_values(ascending=True)

print("Top 10 Loved Chocolates:")
print(top_10_loved)

print("\nTop 10 Hated Chocolates:")
print(top_10_hated)

base_cols = ['Internal ID', 'Q1: GOING OUT?', 'Q2: GENDER', 'Q3: AGE', 'Q4: COUNTRY', 'Q5: STATE, PROVINCE, COUNTY, ETC']
final_cols = base_cols + chocolate_cols
df_final = df[final_cols]

df_final.to_excel("final_cleaned_candy_analysis.xlsx", index=False)