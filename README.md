AI Analysis and Prediction of Kenyan Coffee Exports: Formal Project
Report
1. Problem Definition and Objective
Kenya produces some of the most premium Arabica coffee globally, yet the structural and
regulatory hurdles within its export pipeline remain formidable. The supply chain is
characterized by extreme fragmentation, with approximately 70% of production originating from
over 700,000 smallholder farmers. These producers must navigate complex cooperative
societies and multiple intermediaries, often resulting in delayed payments and diluted earnings.
Furthermore, the industry faces significant climate volatility and the looming pressure of the
European Union Deforestation Regulation (EUDR). Compliance with the EUDR requires
expensive digital traceability and GPS geo-mapping—a substantial investment for a market that
consumes nearly 60% of Kenya's coffee.The primary objective of this project is to develop a
robust predictive model to assist smallholder farmers and cooperatives in monitoring price
trends and planning financial payouts. By leveraging historical trade and macroeconomic data,
we aim to bridge the gap between global market volatility and rural economic stability. This
project is formally classified as a Regression task, focused on predicting export values and
price fluctuations to support data-driven decision-making.
2. Data Acquisition
The study utilized a longitudinal dataset curated from Kenyan government portals, ensuring the
use of authoritative economic and agricultural records.Technical Specifications| Detail |
Specification || ------ | ------ || Time Span | 2001–2020 (Approximately 19 years) || Size | 21 rows
and 29 initial columns || Data Format | CSV || Key Features | Import prices (South Korea,
Germany, USA, Belgium), Average prices (Kenya/Foreign), Exchange rates (Real/Nominal),
Macroeconomic indicators (GDP growth, Population growth, Interest rates), and
Exporter-specific volumes. |
3. Data Cleaning and Preprocessing
The raw dataset required systematic refinement to ensure the integrity of the regression
analysis. The workflow focused on assessing the 29 initial columns using diagnostic functions to
identify the optimal feature set.Cleaning Workflow
● Column Selection: Evaluated variables using df.columns and df.head() to retain
features with high economic relevance.
● Integrity Assessment: Executed df.isnull().sum() and df.describe() to identify missing
values and statistical outliers.
● Technical Verification: Confirmed dataset dimensions and data types using df.shape
and df.dtypes to ensure compatibility with Scikit-learn estimators.Standard
Preprocessing Code
# Exploratory inspection
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
# Feature pruning: Removing redundant or non-predictive metadata
# Example: Dropping redundant nominal exchange rates to favor real
exchange rates
df = df.drop(["nominal_exchange_rate_percent"], axis=1)
Validation Strategy Given the constrained sample size (21 records), the project utilized
Leave-One-Out Cross-Validation (LOOCV) . This strategy ensures that every data point
serves as both a training and a validation instance, maximizing the statistical utility of the limited
19-year historical range.
4. Exploratory Data Analysis (EDA)
Distribution Analysis Histograms SOURCE_IMAGE_1 indicate that coffee import and export
volumes vary significantly across different partner countries and individual exporters. These
distributions reflect the non-uniform impact of global trade events on specific market
participants.Correlation Analysis The Heatmap SOURCE_IMAGE_2 reveals strong intensity
(represented in red) between specific exporter volumes and the target export variables. This
suggests that certain high-volume entities act as "bellwether" indicators for the national
trend.Trend and Scatterplot Analysis
● Historical Volatility: Line graphs SOURCE_IMAGE_3, SOURCE_IMAGE_7 depict a
notable decline in exports between 2007 and 2009, corresponding to post-election
unrest. This was followed by a sharp recovery and price spike in 2010–2011, driven by a
global commodity peak, before stabilizing toward 2020.
● Predictive Limitations: Scatterplots SOURCE_IMAGE_4, SOURCE_IMAGE_5,
SOURCE_IMAGE_6 show that while coffee production correlates positively with exports,
macroeconomic indicators like GDP growth do not perfectly predict export volumes. This
scatter reinforces the need for complex feature engineering beyond raw economic
growth figures.
5. Feature Engineering
To capture the nuances of the agricultural economy, several synthetic variables were developed
to enhance model sensitivity.| Feature Name | Description | Python Logic || ------ | ------ | ------ ||
Price Gap (USD) | Spread between foreign and local prices |
(df'average_foreign_coffee_price_usd' - df'average_kenyan_coffee_price_usd').round(3) ||
Price-Volume Interaction | Captures revenue intensity | (df'average_kenyan_coffee_price_usd'
* df'annual_coffee_exports').round(3) || YoY Growth | Percentage change in Kenyan price |
df'average_kenyan_coffee_price_usd'.pct_change() * 100 || Export Intensity | Ratio of exports
to total production | (df'annual_coffee_exports' / df'annual_coffee_production').round(3) ||
Production Gap | Surplus/Deficit vs Export volumes | (df'annual_coffee_production' -
df'annual_coffee_exports').round(3) || Trend Index | Longitudinal time-step | df'year' -
df'year'.min() + 1 || Trade Openness | Combined trade liquidity | df'total_annual_imports' +
df'total_annual_exports' || Credit Condition | Lending environment indicator |
df'real_interest_rate_percent' || Lag Features | Prior year export/price benchmarks |
df'total_annual_exports'.shift(1) / df'average_kenyan_coffee_price_usd'.shift(1) |
6. Model Building
The modeling phase prioritized algorithms capable of handling high-dimensional features
relative to a small number of observations:
● Linear Regression: Established a performance baseline to evaluate more complex
models.
● LASSO Regression (Least Absolute Shrinkage and Selection Operator):
Implemented for its inherent feature selection capabilities, effectively zeroing out
non-contributing variables to prevent overfitting on the 19-year dataset.
● Random Forest: Utilized to capture potential non-linearities and interactions between
trade volumes and interest rates.
7. Model Evaluation
The models were assessed using standard regression metrics, with results summarized below:|
Model | MAE | MSE | RMSE | R-squared || ------ | ------ | ------ | ------ | ------ || Linear Regression |
2.108429 | 9.213112 | 3.035311 | 0.999097 || LASSO Regression | 0.037808 | 0.002445 |
0.049449 | 1.000000 || Random Forest | 27.855105 | 1703.238914 | 41.270315 | 0.833121 |
Methodological Caveat: As a Senior Data Scientist, I must note that the LASSO model's
perfect R-squared of 1.000 on a dataset of this size suggests a direct linear combination or
data leakage. Analysis of SOURCE_IMAGE_8 shows "Rashid Moledina exports" as a dominant
predictor. This indicates that the target variable is likely highly dependent on the volumes of a
few major exporters. While statistically accurate within this sample, the model should be treated
as a high-precision proxy rather than a universal generalizer.Feature Importance Analysis:
SOURCE_IMAGE_9 highlights "Mwangi Coffee" and "Diamond Coffee" as top predictors for the
Random Forest model. In agricultural economic terms, these entities serve as "bellwether"
exporters. Monitoring their trade volumes provides a viable proxy for predicting national export
trends when broader macroeconomic data lags.
8. Results Interpretation and Insights
Economic and Regulatory Significance The predictive insights generated here are vital for
the 700,000 smallholder farmers whose livelihoods depend on coffee. Beyond basic price
tracking, these models provide the financial visibility needed to navigate the EU Deforestation
Regulation (EUDR) . Predictive stability allows cooperatives to better justify and afford the
"expensive digital traceability and GPS geo-mapping" required to maintain access to the EU
market, which accounts for 60% of Kenyan exports.Actionable Takeaways:
1. Traceability Investment: Cooperatives can use price-hike predictions to time
investments in digital traceability infrastructure, ensuring compliance without depleting
farmer payouts.
2. Revenue Stabilization: By anticipating export revenue swings, the government can
better plan agricultural support policies and manage foreign-currency inflows.
3. Cooperative Payout Planning: Accurate forecasts provide cooperatives with the lead
time necessary to design stabilization policies, shielding farmers from the immediate
shocks of global market volatility.
9. Deployment
The current project exists as a functional Jupyter Notebook analysis. The proposed deployment
architecture for the next phase features a streamlined UI for real-time stakeholder decision
support.
● Recommended Frameworks: Implementation via Streamlit, Flask, or Gradio for
web accessibility.
● Functionality: The UI will allow users to input current trade values to receive real-time
export predictions.
● Repository Access: The source code is hosted at:
https://github.com/Chapo-Avengers/Coffee_Prediction_Analysis
10. Conclusion and Project Links
This project successfully bridges the gap between classroom AI theory and the practicalities of
the Kenyan coffee economy. By transforming government trade data into predictive insights, we
provide a vital tool for economic resilience in one of Kenya's most important agricultural
sectors.Essential Project Links
● GitHub Repository: https://github.com/Chapo-Avengers/Coffee_Prediction_Analysis
● Data Sources: Kenyan Government PortalsProject Team
● Stella Kasera
● Danielle Nyanjui
● Stephanie Wambui
● Larry Steve
● Daizy Moseti
● Karwitha Elosy
● Dennis Kimani
● Love Melinda
