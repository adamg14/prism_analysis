import pandas as pd
import matplotlib.pyplot as plt

cohort_df = pd.read_csv("./cohort_data.csv")

# start all cohorts at 0
zero_points = cohort_df.groupby('cohort_name').first().reset_index()
zero_points['cohort_accumlative_revenue'] = 0
zero_points['transaction_month'] = zero_points['transaction_month']

cohort_df = pd.concat([zero_points, cohort_df], ignore_index=True)

cohort_df["transaction_month"] = pd.to_datetime(cohort_df["transaction_month"])
cohort_df = cohort_df.sort_values(by=['cohort_name', 'transaction_month'])

for cohort in cohort_df["cohort_name"].unique():
    cohort_data = cohort_df[cohort_df['cohort_name'] == cohort]
    plt.plot(cohort_data['transaction_month'], cohort_data['cohort_accumlative_revenue'], label=cohort)

plt.show()