# Analysis of the World's 2000 Largest Companies

## Data Source
The dataset used in this research was obtained from Kaggle and contains information about the 2000 largest companies in the world for 2023. You can access the dataset [here](https://www.kaggle.com/code/devraai/financial-insights-of-top-2000-companies-2024/input).

## Data Preparation
The following preprocessing steps were performed to clean and standardize the data:
- Removed currency symbols ("$").
- Converted financial values by replacing suffixes:
  - "M" (millions) was replaced with multiplication by `1e6`.
  - "B" (billions) was replaced with multiplication by `1e9`.
- Transformed financial data from string to integer format for further analysis.

## Created DataFrames
Several DataFrames were generated to facilitate analysis:
1. **Statistical Summary DataFrame:**
   - Calculates the mean, median, and standard deviation for key financial metrics across all companies.

2. **Country-Specific DataFrame:**
   - Filters and displays financial data for companies based in a selected country.

3. **Aggregated Country DataFrame:**
   - Groups companies by country and aggregates key financial indicators.

4. **Country-Level Statistics DataFrame:**
   - Computes the mean, median, and standard deviation for financial metrics on a per-country basis.

## Visualizations
Several visualizations were created to better understand the data and identify trends:
1. **Distribution of Companies by Country:**
   - A visualization showing the number of companies per country.

2. **Profit Percentage per Country:**
   - Displays the profit ratio for each country, normalized by the number of companies.

3. **Investment Profitability Index by Country:**
   - A mathematical formula applied to create an index predicting investment profitability across different countries.

## Future Research Directions
Several additional analyses and enhancements are planned to expand the research:

- **Exploring Further Visualizations:**
  - Identify and generate meaningful charts from the existing dataset.

- **Research Expansion:**
  - Consider new research directions to deepen insights.

- **Demographics and Education Data Integration:**
  - Incorporate country population sizes and analyze the working-age population.
  - Add data on the number of academic degrees per country.

- **Company-Level Analysis:**
  - Compare company profit relative to their total assets.

- **Regression Analysis:**
  - Use multiple linear regression to identify which variable (sales, profit, or assets) best predicts market value.

- **Macroeconomic Indicators:**
  - Integrate GDP per capita data for a more comprehensive analysis.

- **Geographical Data Representation:**
  - Develop an interactive world map using Tableau to illustrate the distribution of assets and companies across countries.

- **Market Value Prediction Model:**
  - Build a predictive model to estimate market value based on profit, assets, and sales.

- **Outlier Detection:**
  - Identify companies with unusual profits (both high and low) by predicting profit based on other variables and analyzing deviations.

---

This project aims to provide valuable insights into the global corporate landscape and guide potential investment strategies based on financial performance metrics.

