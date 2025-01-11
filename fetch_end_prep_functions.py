import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from collections import defaultdict


def prep_df(df: pd.DataFrame, columns_for_calc: list):
    for column in columns_for_calc:
        df[column] = df[column].str.replace('$', '', regex=False)
        df[column] = df[column].str.replace(',', '', regex=False)
        df[column] = df[column].apply(lambda x: float(x[:-1]) * 1_000_000_000 if x.endswith('b') else float(x[:-1]) * 1_000_000)
        df[column] = df[column].astype(int)
        # df[column] = pd.to_numeric(df[column], errors='coerce')
    return df



def biuld_df_by_country(df: pd.DataFrame):
    data_dict = defaultdict(list)
    country_list = df['Country'].unique()
    for country in country_list:
        df_small = df[df['Country'] == country]
        data_dict['country'].append(country)
        data_dict['num_of_companys'].append(df_small.shape[0])
        data_dict['sales'].append(round(sum(df_small['Sales']) / 1_000_000, 2))
        data_dict['profit'].append(round(sum(df_small['Profit']) / 1_000_000, 2))
        data_dict['assets'].append(round(sum(df_small['Assets']) / 1_000_000, 2))
        data_dict['market_value'].append(round(sum(df_small['Market Value']) / 1_000_000, 2))

    df = pd.DataFrame(data_dict)
    return df








country_counts = df['big_countrys'].value_counts()

# Step 3: Create the bar chart
plt.figure(figsize=(12, 6))
country_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# Customize the chart
plt.title('Number of Companies by Country', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Companies', fontsize=12)
plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()



def merge_small_cuntry(df: pd.DataFrame):
    country_counts = df['Country'].value_counts()
    df['big_countrys'] = df['Country'].apply(lambda x: x if country_counts[x] >= 10 else 'Other')
    return df

