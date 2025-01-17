import pandas as pd
from fetch_end_prep_functions import prep_df, calc_df_statistic, biuld_df_by_country, bell_curve_for_statistic, companys_per_country, distribution_by_country, Trend_graph_by_country



file_path = '/Users/yairbecher/Yair staf/Python_learning/2000_largest_companys_data.git/Top 2000 Companies Financial Data 2024.csv'
df = pd.read_csv(file_path)


columns_for_calc = ['sales', 'profit', 'assets', 'market_value']


df_prep = prep_df(df, columns_for_calc)
df_statistic = calc_df_statistic(df_prep, columns_for_calc)
# bell_curve = bell_curve_for_statistic(df_statistic)
# df_spsific_country = companys_per_country(df)
df_by_country = biuld_df_by_country(df_prep)
Trend_graph_by_country = Trend_graph_by_country(df_by_country)
distribution_by_country = distribution_by_country(df_by_country)
df_statistic_by_country = calc_df_statistic(df_by_country, columns_for_calc)

print(df.shape)

'CHECK FOR GITHUB'



