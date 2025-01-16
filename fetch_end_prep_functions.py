import pandas as pd
import numpy as np
import seaborn as sns
import statistics as st
import matplotlib.pyplot as plt
from collections import defaultdict
from scipy.stats import norm


def prep_df(df: pd.DataFrame, columns_for_calc: list):
    df.columns = df.columns.str.lower()
    df.rename(columns={'market value': 'market_value'}, inplace=True)
    for column in columns_for_calc:
        df[column] = df[column].str.replace('$', '', regex=False)
        df[column] = df[column].str.replace(',', '', regex=False)
        df[column] = df[column].apply(lambda x: float(x[:-1]) * 1_000_000_000 if x.endswith('b') else float(x[:-1]) * 1_000_000)
        df[column] = df[column].astype(int)
        # df[column] = pd.to_numeric(df[column], errors='coerce')
    return df



def calc_statistic_by_companys(df: pd.DataFrame, columns_for_calc: list):
    data_dickt = defaultdict(list)
    action_list = ['avg', 'median', 'str']
    for action in action_list:
        data_dickt['calc_action'].append(action)
    for column in columns_for_calc:
        avg = df[column].mean()
        median = df[column].median()
        std = df[column].std()

        data_dickt[column].append(avg / 1_000_000)
        data_dickt[column].append(median / 1_000_000)
        data_dickt[column].append(std / 1_000_000)

    df = pd.DataFrame(data_dickt)
    return df


def bell_curve_for_statistic(df: pd.DataFrame):
    mean = float(df['sales'].iloc[0])
    std_dev = float(df['sales'].iloc[2])
    num_companys = 2000

    x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, num_companys)
    y = norm.pdf(x, mean, std_dev)

    # Plot the bell curve
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Normal Distribution', color='blue')
    plt.title('Bell Curve')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.axvline(mean, color='red', linestyle='--', label='Mean')
    plt.legend()
    plt.grid()
    plt.show()


def companys_per_country(df: pd.DataFrame):
    contry = input('input cuontry for check: ')
    df_spsific_country = df[df['country'] == contry]
    return df_spsific_country




def biuld_df_by_country(df: pd.DataFrame):
    data_dict = defaultdict(list)
    country_list = df['country'].unique()
    for country in country_list:
        df_small = df[df['country'] == country]
        data_dict['country'].append(country)
        data_dict['num_of_companys'].append(df_small.shape[0])
        data_dict['sales'].append(round(sum(df_small['sales']) / 1_000_000, 2))
        data_dict['profit'].append(round(sum(df_small['profit']) / 1_000_000, 2))
        data_dict['assets'].append(round(sum(df_small['assets']) / 1_000_000, 2))
        data_dict['market_value'].append(round(sum(df_small['market_value']) / 1_000_000, 2))

    df = pd.DataFrame(data_dict)
    return df







def plot_function(df: pd.DataFrame):

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
    return print('hii')





def merge_small_cuntry(df: pd.DataFrame):
    country_counts = df['country'].value_counts()
    df['big_countrys'] = df['country'].apply(lambda x: x if country_counts[x] >= 10 else 'other')
    return df



def distribution_by_country(df: pd.DataFrame):

    plt.figure(figsize=(30, 6))

    sns.kdeplot(df['num_of_companys'], fill=True, color='blue', alpha=0.5)
    plt.xticks(range(1, max(df['num_of_companys']), 10))
    # plt.xticks(df['num_of_companys'], df['country'], rotation=90, fontsize=10)

    # Add country names as annotations
    # for i, row in df.iterrows():
    #     plt.text(row['num_of_companys'], 0.005, row['country'], rotation=90, ha='center', fontsize=10)

    plt.title('Density of Companies Across Countries')
    plt.xlabel('Number of Companies')
    plt.ylabel('Density')
    plt.show()


    # country_counts.sort_values(ascending=False).plot(kind='bar', figsize=(12, 6), color='skyblue')
    # plt.title('Number of Companies by Country')
    # plt.xlabel('Country')
    # plt.ylabel('Number of Companies')
    # plt.show()
