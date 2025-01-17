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
        df[column] = df[column].replace({'\$': '', ',': '', ' B': 'e9', ' M': 'e6'}, regex=True).astype(float).astype(int)
    df["profit_percentage"] = (df["profit"] / df["sales"]) * 100
    return df



def calc_df_statistic(df: pd.DataFrame, columns_for_calc: list):
    data_dickt = defaultdict(list)
    action_list = ['avg', 'median', 'str']
    for action in action_list:
        data_dickt['calc_action'].append(action)
    for column in columns_for_calc:
        avg = df[column].mean()
        median = df[column].median()
        std = df[column].std()

        data_dickt[column].append(avg)
        data_dickt[column].append(median)
        data_dickt[column].append(std)

    df = pd.DataFrame(data_dickt)
    return df



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
        data_dict['sales'].append(sum(df_small['sales']))
        data_dict['profit'].append(sum(df_small['profit']))
        data_dict['assets'].append(sum(df_small['assets']))
        data_dict['market_value'].append(sum(df_small['market_value']))

    df = pd.DataFrame(data_dict)
    return df



def merge_small_cuntry(df: pd.DataFrame):
    country_counts = df['country'].value_counts()
    df['big_countrys'] = df['country'].apply(lambda x: x if country_counts[x] >= 10 else 'other')
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


    # # # graphs # # #

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




def distribution_by_country(df: pd.DataFrame):

    plt.figure(figsize=(30, 6))

    sns.kdeplot(df['num_of_companys'], fill=True, color='blue', alpha=0.5)
    plt.xticks(range(1, max(df['num_of_companys']), 10))
    # plt.xticks(df['num_of_companys'], df['country'], rotation=90, fontsize=10)


    plt.title('Density of Companies Across Countries')
    plt.xlabel('Number of Companies')
    plt.ylabel('Density')
    plt.show()


def Trend_graph_by_country(df: pd.DataFrame, columns_for_calc: list):
    for column in columns_for_calc:
        df[column] = df[column] / df['num_of_companys']
    df = df.drop(columns=["num_of_companys"])

    df_long = df.melt(id_vars="country", var_name="Indicator", value_name="Value")

    # Plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_long, x="country", y="Value", hue="Indicator", marker="o")

    # Add labels and title
    plt.title("Economic Indicators by Country \n normalized by company average", fontsize=16)
    plt.xlabel("country", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    plt.xticks(rotation=90)
    plt.legend(title="Indicator")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    plt.show()


def profit_percentage_graph(df: pd.DataFrame):
    df.sort_values(by="profit_percentage", ascending=False, inplace=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df["country"], df["profit_percentage"], marker="o")
    plt.xticks(rotation=90)
    plt.title("Profit Percentage")
    plt.ylabel("Profit Percentage (%)")
    plt.xlabel("countrys")
    plt.show()
