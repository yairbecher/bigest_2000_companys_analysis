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
        if column in df.columns:
            df[column] = df[column].replace({'\$': '', ',': '', ' B': 'e9', ' M': 'e6'}, regex=True).astype(float).astype(int)
    df["avg_profit_percentage"] = (df["profit"] / df["sales"])
    return df



  # # # analysis # # #



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




def biuld_df_by_country(df: pd.DataFrame):
    data_dict = defaultdict(list)
    country_list = df['country'].unique()
    for country in country_list:
        df_small = df[df['country'] == country]
        data_dict['country'].append(country)
        data_dict['num_of_companys'].append(df_small.shape[0])
        data_dict['sales'].append(sum(df_small['sales']))
        data_dict['profit'].append(sum(df_small['profit']))
        data_dict['avg_profit_percentage'].append(df_small['avg_profit_percentage'].mean())
        data_dict['assets'].append(sum(df_small['assets']))
        data_dict['market_value'].append(sum(df_small['market_value']))

    df = pd.DataFrame(data_dict)
    return df



def feth_spsific_country(df: pd.DataFrame):
    contry = input('input cuontry for check: ')
    df_spsific_country = df[df['country'] == contry]
    return df_spsific_country


def merge_small_cuntry(df: pd.DataFrame):
    country_counts = df['country'].value_counts()
    df['big_countrys'] = df['country'].apply(lambda x: x if country_counts[x] >= 10 else 'other')
    return df


### save function ###

# def save_to_machine(list_of_dfs: list):
#     for df in list_of_dfs:

