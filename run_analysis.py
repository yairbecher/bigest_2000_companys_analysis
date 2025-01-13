import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
from collections import defaultdict
from fetch_end_prep_functions import prep_df, calc_statistic_by_companys, biuld_df_by_country, bell_curve_for_statistic



file_path = '/Users/yairbecher/Yair staf/Python_learning/2000_largest_companys_data/Top 2000 Companies Financial Data 2024.csv'
df = pd.read_csv(file_path)


columns_for_calc = ['Sales', 'Profit', 'Assets', 'Market Value']

df_prep = prep_df(df, columns_for_calc)
df_statistic = calc_statistic_by_companys(df_prep, columns_for_calc)
bell_curve = bell_curve_for_statistic(df_statistic)
# df_spsific_country = companys_per_country(df)
df_by_country = biuld_df_by_country(df)
print(df.shape)

'CHECK FOR GITHUB'


