import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from dfs_functions import prep_df

impot_file = os.environ.get('inpot_file')
df = pd.read_csv(impot_file, index_col=0)

columns_for_calc = ['sales', 'profit', 'avg_profit_percentage', 'assets', 'market_value']
df = prep_df(df, columns_for_calc)


#To correctly divide the countries in half according to market value.
# Understand how to properly treat countries that don't appear much, because putting it in "other" can affect things that I'm not sure I understand


###First model regardless of country###

# # Encode categorical variables ('country')
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('country', OneHotEncoder(), ['country'])],remainder='passthrough')
#
# df_sorted = df.sort_values(by='market value', ascending=False)
#
# # Split the data by alternating large and small companies
# X_train = df_sorted.iloc[::2].drop(columns=['market value'])  # Select every other row starting from the largest
# X_test = df_sorted.iloc[1::2].drop(columns=['market value'])  # Select every other row starting from the second largest
#
# y_train = df_sorted.iloc[::2]['market value']
# y_test = df_sorted.iloc[1::2]['market value']


# Split the data into features and target
y = df['market_value']  # Target
df_with_country = df.drop(columns=['name'])  # Features including country
df_without_country = df.drop(columns=['name', 'country'])  # Features excluding country

df['country_encoded'] = df['country'].map(df['country'].value_counts())


X_train_w = df_with_country.iloc[::2].drop(columns=['market_value'])  # Select every other row starting from the largest
X_test_w = df_with_country.iloc[1::2].drop(columns=['market_value'])  # Select every other row starting from the second largest

y_train_w = df_with_country.iloc[::2]['market_value']
y_test_w = df_with_country.iloc[1::2]['market_value']


X_train_n = df_without_country.iloc[::2].drop(columns=['market_value'])  # Select every other row starting from the largest
X_test_n = df_without_country.iloc[1::2].drop(columns=['market_value'])  # Select every other row starting from the second largest

y_train_n = df_without_country.iloc[::2]['market_value']
y_test_n = df_without_country.iloc[1::2]['market_value']


# # Split the data into training and testing sets (50/50)
# X_train_w, X_test_w, y_train, y_test = train_test_split(X_with_country, y, test_size=0.5, random_state=42)
# X_train_n, X_test_n, y_train, y_test = train_test_split(X_without_country, y, test_size=0.5, random_state=42)
#
# # Define the preprocessing for the "country" column (only needed in the "with country" model)
preprocessor = ColumnTransformer(
    transformers=[
        ('country', OneHotEncoder(handle_unknown='ignore'), ['country'])  # Ignore unknown categories
    ],
    remainder='passthrough'
)

# Model with "country" included
model_pipeline_with_country = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Model without "country" (no preprocessing needed)
model_pipeline_without_country = Pipeline(steps=[
    ('regressor', LinearRegression())
])

# Train the model with "country" included
model_pipeline_with_country.fit(X_train_w, y_train_w)

# Train the model without "country"
model_pipeline_without_country.fit(X_train_n, y_train_n)

# Make predictions for both models
y_pred_n = model_pipeline_without_country.predict(X_test_n)
y_pred_w = model_pipeline_with_country.predict(X_test_w)


# Evaluate the models
mae_w = mean_absolute_error(y_test_w, y_pred_w)
r2_w = r2_score(y_test_w, y_pred_w)

mae_n = mean_absolute_error(y_test_n, y_pred_n)
r2_n = r2_score(y_test_n, y_pred_n)

# Output the results
print("Model with Country Included:")
print(f"Mean Absolute Error: {mae_w}")
print(f"R-squared: {r2_w}\n")

print("Model without Country:")
print(f"Mean Absolute Error: {mae_n}")
print(f"R-squared: {r2_n}")
