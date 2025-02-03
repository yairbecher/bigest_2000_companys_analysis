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

 ####Ranking of all the columns for each company and a scheme of the ranking so that the company with the highest ranking is the best###
def best_company(conn):
    # query = f"""   SELECT name,
    # DENSE_RANK() OVER(ORDER BY sales ASC) AS sales_rank,
    # DENSE_RANK() OVER(ORDER BY profit ASC) AS profit_rank,
    # DENSE_RANK() OVER(ORDER BY assets ASC) AS assets_rank,
    # DENSE_RANK() OVER(ORDER BY market_value ASC) AS market_value_rank,
    # DENSE_RANK() OVER(ORDER BY avg_profit_percentage ASC) AS avg_profit_percentage_rank
    # FROM countries
    # group by name"""

    query = """SELECT name, 
        (RANK() OVER(ORDER BY sales ASC) +
        RANK() OVER(ORDER BY profit ASC) +
        RANK() OVER(ORDER BY assets ASC) +
        RANK() OVER(ORDER BY market_value ASC) +
        RANK() OVER(ORDER BY avg_profit_percentage ASC)) AS total_rank
        FROM countries
        order by total_rank;"""
    result = pd.read_sql_query(query, conn)
    print(result)
    return result

df_renk = best_company(conn)


