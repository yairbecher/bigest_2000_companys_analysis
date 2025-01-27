import pandas as pd
import os
from dfs_functions import prep_df, calc_df_statistic, biuld_df_by_country, feth_spsific_country
from plots_functions import run_plots_analysis


file_path = os.environ.get('file_path')
df = pd.read_csv(file_path)


columns_for_calc = ['sales', 'profit', 'avg_profit_percentage', 'assets', 'market_value']


df_prep = prep_df(df, columns_for_calc)

df_statistic_by_company = calc_df_statistic(df_prep, columns_for_calc)
df_by_country = biuld_df_by_country(df_prep)
df_statistic_by_country = calc_df_statistic(df_by_country, columns_for_calc)
# df_spsific_country = feth_spsific_country(df)


plots = run_plots_analysis(df_by_country, columns_for_calc, df_statistic_by_company)



print(df.shape)

'CHECK FOR GITHUB 2'



