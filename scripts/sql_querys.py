import pandas as pd
import sqlite3
import os
# from run_analysis import columns_for_calc
from dfs_functions import prep_df

columns_for_calc = ['sales', 'profit', 'avg_profit_percentage', 'assets', 'market_value']

impot_file = os.environ.get('impot_file')
df = pd.read_csv(impot_file)
df = prep_df(df, columns_for_calc)

conn = sqlite3.connect("df.db")
df.to_sql("countries", conn, if_exists="replace", index=False)
print('test1')




def min_max_sales(conn):
    query = "SELECT min(sales), max(sales) FROM countries"
    resolt = pd.read_sql_query(query, conn)
    print(resolt)
    return resolt

min_max_sales = min_max_sales(conn)
print('test')
# def fetch_specific_country():
#     country = input('Input country for check: ')
#
#     conn = sqlite3.connect("df.db")
#     df.to_sql("countries", conn, if_exists="replace", index=False)
#     query = "SELECT * FROM countries WHERE country = ?"
#     df_specific_country = pd.read_sql_query(query, conn, params=(country,))
#     conn.close()
#
#     return df_specific_country
#
#
# df = fetch_specific_country()
# print('test')