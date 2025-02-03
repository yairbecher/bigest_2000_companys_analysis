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
df.to_sql("companys", conn, if_exists="replace", index=False)
print('test1')




def min_max_sales(conn):
    query = "SELECT min(sales), max(sales) FROM countries"
    result = pd.read_sql_query(query, conn)
    print(result)
    return result

min_max_sales = min_max_sales(conn)
print('test')

# avg_profit_percentage

def df_by_country(conn):
    query = (f"""SELECT distinct country as country, count(country) as num_of_companys, sum(sales), sum(profit), sum(assets), sum(market_value), avg(avg_profit_percentage) as avg_profit_percentage
             FROM countries
             group by country
             order by num_of_companys desc""")
    result = pd.read_sql_query(query, conn)
    print(result)
    return result

df_by_country = df_by_country(conn)