import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from collections import defaultdict

columns_for_calc = ['Sales', 'Profit', 'Assets', 'Market Value']

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


def companys_per_country(df: pd.DataFrame):
    contry = input('input cuontry for check: ')
    df_spsific_country = df[df['Country'] == contry]
    return df_spsific_country


# def calc_statistic_by_companys(df: pd.DataFrame, columns_for_calc: list):
#     action_list = ['mean', 'median', 'mode', 'range', 'standard_deviation']
#     data_dickt = defaultdict(list)
#     for action in action_list:
#         data_dickt['action'].append(action)
#         data_dickt['sales'].append()
#         data_dickt['profit'].append()
#         data_dickt['assets'].append()
#         data_dickt['sales'].append()
#         data_dickt['market_value'].append()
#
#
#     return df_statistic

def calc_statistic_by_companys(df: pd.DataFrame, columns_for_calc: list):
    data_dickt = defaultdict(list)
    action_list = ['avg', 'median', 'str']
    for action in action_list:
        data_dickt['calc_action'].append(action)
    for column in columns_for_calc:
        avg = df[column].mean()
        median = df[column].median()
        std =df[column].std()


        data_dickt[column].append(avg)
        data_dickt[column].append(median)
        data_dickt[column].append(std)

    df = pd.DataFrame(data_dickt)
    return df


file_path = '/Users/yairbecher/Yair staf/Python_learning/2000_largest_companys_data/Top 2000 Companies Financial Data 2024.csv'
df = pd.read_csv(file_path)
df_prep = prep_df(df, columns_for_calc)
df_statistic = calc_statistic_by_companys(df_prep, columns_for_calc)
# df_spsific_country = companys_per_country(df)
df_by_country = biuld_df_by_country(df)
print(df.shape)









# Step 2: Count the number of companies per country
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
print("hii")



def merge_small_cuntry(df: pd.DataFrame):
    country_counts = df['Country'].value_counts()
    df['big_countrys'] = df['Country'].apply(lambda x: x if country_counts[x] >= 10 else 'Other')
    return df

