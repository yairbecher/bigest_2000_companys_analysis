import pandas as pd
import sqlite3


def fetch_specific_country(df: pd.DataFrame):
    country = input('Input country for check: ')

    conn = sqlite3.connect("df.db")
    df.to_sql("countries", conn, if_exists="replace", index=False)
    query = "SELECT * FROM countries WHERE country = ?"
    df_specific_country = pd.read_sql_query(query, conn, params=(country,))
    conn.close()

    return df_specific_country