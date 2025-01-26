import pandas as pd
import numpy as np
import seaborn as sns
import statistics as st
import matplotlib.pyplot as plt
from collections import defaultdict
from scipy.stats import norm
from sklearn.preprocessing import MinMaxScaler


def run_plots_analyss(df_by_country: pd.DataFrame, columns_for_calc: list, df_statistic_by_company: pd.DataFrame):
    profit_percentage_graph(df_by_country)
    distribution_by_country(df_by_country)
    investment_feasibility_index(df_by_country)
    mead_investment_feasibility_index(df_by_country)


def profit_percentage_graph(df: pd.DataFrame):
    df.sort_values(by="avg_profit_percentage", ascending=False, inplace=True)

    df["normalized_profit"] = df["avg_profit_percentage"] / df["num_of_companys"]

    plt.figure(figsize=(12, 6))

    plt.plot(df["country"], df["avg_profit_percentage"], marker="o", label="Avg Profit %")
    plt.plot(df["country"], df["normalized_profit"], marker="s", linestyle="--", color="red", label="Normalized Profit %")
    # plt.plot(df["country"], df["num_of_companys"], marker="o", color="green", label="num of companys")

    plt.xticks(rotation=90)
    plt.title("AVG Profit Percentage and Normalized Profit Percentage")
    plt.ylabel("Profit Percentage")
    plt.xlabel("Countries")
    plt.legend()
    plt.grid(True)
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

def investment_feasibility_index(df):
    df['company_weight'] = np.log(df['num_of_companys'])
    df['IPI'] = df['avg_profit_percentage'] * (df['profit'] / df['num_of_companys']) * df['company_weight']
    df = df.sort_values(by='IPI', ascending=False)

    plt.figure(figsize=(12, 10))
    sns.barplot(x='country', y='IPI', data=df, palette='viridis')
    plt.title('Investment Profitability Index by Country')
    plt.xlabel('country')
    plt.ylabel('Investment Profitability Index (IPI)')
    plt.xticks(rotation=90)

    formula = r"$\text{IPI} = \left(\frac{\text{Profit}}{\text{Sales}}\right) \times \left(\frac{\text{Profit}}{\text{Companies}}\right) \times \ln(\text{Companies})$"

    plt.annotate(
        formula,
        xy=(0.85, 0.90),
        xycoords='axes fraction',
        fontsize=12,
        color='black',
        ha='right',
        va='top',
        bbox=dict(facecolor='white', alpha=0.5, edgecolor='black')
    )

    plt.show()


def mead_investment_feasibility_index(df):
    df['company_weight'] = np.log(df['num_of_companys'])

    df['IPI'] = df['median_profit'] * (df['profit'] / df['num_of_companys']) * df['company_weight']
    df = df.sort_values(by='IPI', ascending=False)

    plt.figure(figsize=(12, 10))
    sns.barplot(x='country', y='IPI', data=df, palette='viridis')
    plt.title('Investment Profitability Index by Country')
    plt.xlabel('country')
    plt.ylabel('Investment Profitability Index (IPI)')
    plt.xticks(rotation=90)
    plt.show()