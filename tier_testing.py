import pandas as pd
import matplotlib.pyplot as plt

all_tiers = pd.read_csv('all_tiers.csv')
bronze_tiers = all_tiers[(all_tiers['label'] == 'Bronze')
| (all_tiers['label'] == 'bronze_control')]

bronze_tiers['month'] = pd.to_datetime(bronze_tiers['month'])
bronze_tiers = bronze_tiers.sort_values(by=['label', 'month'])

for label in ['Bronze', 'bronze_control']:
    bronze_plot = bronze_tiers[bronze_tiers['label'] == label]
    plt.plot(bronze_plot['month'], bronze_plot['accumulative_revenue'], label=label)


plt.legend()
plt.show()