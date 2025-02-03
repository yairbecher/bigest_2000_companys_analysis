import pandas as pd
import os
from dfs_functions import prep_df, calc_df_statistic, biuld_df_by_country, fetch_specific_country
from plots_functions import run_plots_analysis




impot_file = os.environ.get('impot_file')
df = pd.read_csv(impot_file)


columns_for_calc = ['sales', 'profit', 'avg_profit_percentage', 'assets', 'market_value']


df_prep = prep_df(df, columns_for_calc)

df_statistic_by_company = calc_df_statistic(df_prep, columns_for_calc)
df_by_country = biuld_df_by_country(df_prep)
df_statistic_by_country = calc_df_statistic(df_by_country, columns_for_calc)
# df_spsific_country = fetch_specific_country(df_prep)


plots = run_plots_analysis(df_by_country, columns_for_calc, df_statistic_by_company)



print(df.shape)

'CHECK FOR GITHUB 2'



