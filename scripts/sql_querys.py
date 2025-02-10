import pandas as pd
import sqlite3
import os
# from run_analysis import columns_for_calc
from dfs_functions import prep_df

columns_for_calc = ['sales', 'profit', 'avg_profit_percentage', 'assets', 'market_value']

impot_file = os.environ.get('inpot_file')
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

    query = """SELECT name, DENSE_RANK() OVER(ORDER BY total_rank DESC) AS ranke
    FROM (SELECT name, 
        (DENSE_RANK() OVER(ORDER BY sales ASC) +
        DENSE_RANK() OVER(ORDER BY profit ASC) +
        DENSE_RANK() OVER(ORDER BY assets ASC) +
        DENSE_RANK() OVER(ORDER BY market_value ASC) +
        DENSE_RANK() OVER(ORDER BY avg_profit_percentage ASC)) AS total_rank
        FROM countries
        order by total_rank);"""
    result = pd.read_sql_query(query, conn)
    print(result)
    return result

df_renk = best_company(conn)


# Retrieve the top 3 most profitable companies for each country, ordered by profit.

def top_3_profitable_companies(conn):
    query = """with ramk_tabel as ( 
               SELECT country, name, RANK() OVER (PARTITION BY country ORDER BY profit DESC) AS rank 
               FROM countries)
    select country, GROUP_CONCAT(name, ', ') AS top_companies
    from ramk_tabel
    where rank < 4
    group by country
    """

    result = pd.read_sql_query(query, conn)
    print(result)
    return result

df_top_3_profitable_companies = top_3_profitable_companies(conn)



# Find the companies where the market value is less than their total assets. Rank them by the ratio of market value to assets.

def market_value_and_assets_Comparison(conn):
    query = """with negative_market_value as (select name, market_value - assets as gap from countries where gap > 0)
    select  NAME, RANK() OVER(ORDER BY GAP DESC) as gap from negative_market_value"""

    result = pd.read_sql_query(query, conn)
    print(result)
    return result

market_value_and_assets_Comparison = market_value_and_assets_Comparison(conn)

# Identify the companies with the highest sales but a below-average profit margin.

def highest_sales_but_low_profit(conn):
    query = """select name, sales, profit
    from countries
    where profit > (SELECT AVG(profit) FROM countries)
    order by sales"""

    result = pd.read_sql_query(query, conn)
    print(result)
    return result

df_highest_sales_but_low_profit = highest_sales_but_low_profit(conn)


# Determine what percentage of a country's total market value is held by its top 5 companies.

def best_compais_market_value_percentage(conn):
    # query = """with 5_best_companies as (select name, market_value rank() over(order by market_value desc) as rank
    # from countries
    # QUALIFY rank < 5) select * from 5_best_companies"""

    query = """   SELECT
                name, market_value
                
                FROM countries
                where (select RANK() OVER(ORDER BY market_value DESC) as rank) < 299800000000;"""

    result = pd.read_sql_query(query, conn)
    print(result)
    return result

df_best_compais_market_value_percentage = best_compais_market_value_percentage(conn)



query = '''SELECT
    a.bedrooms,
    COUNT(r.id) AS confirmed_reservations,
    (COUNT(r.id) * 100.0) / SUM(COUNT(r.id)) OVER () AS confirmed_reservations_%
FROM reservations r
JOIN apartments a ON r.apartment_id = a.apartment_id
WHERE a.city = 'New York'
  AND r.reservation_status = 'confirmed'
  AND r.check_in_date BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY a.bedrooms
ORDER BY a.bedrooms;'''


query = '''WITH confirmed_counts AS (
    SELECT 
        a.bedrooms, 
        COUNT(*) AS confirmed_reservations
    FROM reservations r
    JOIN apartments a ON r.apartment_id = a.apartment_id
    WHERE a.city = 'New York' 
      AND r.reservation_status = 'confirmed'
      AND r.check_in_date BETWEEN '2022-05-01' AND '2022-05-31'
    GROUP BY a.bedrooms
)
SELECT 
    bedrooms, 
    confirmed_reservations, 
    (confirmed_reservations * 100.0) / (SELECT SUM(confirmed_reservations) FROM confirmed_counts) AS confirmed_reservations_%
FROM confirmed_counts
ORDER BY bedrooms;
'''