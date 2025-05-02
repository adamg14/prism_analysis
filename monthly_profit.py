import pandas as pd
import matplotlib.pyplot as plt

# Load and prepare data
monthly_profit = pd.read_csv('montly_accumulative_profit.csv')
monthly_profit['month'] = pd.to_datetime(monthly_profit['month'])
monthly_profit = monthly_profit.sort_values(by=['label', 'month'])

# Define tiers
tiers = ['Bronze', 'Silver', 'Gold', 'Platinum']

# Create 2x2 subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10), sharex=True)

# Flatten axes array for easy indexing
axes = axes.flatten()

# Event date
event_date = pd.to_datetime('2024-01-02')

# Plot each tier and its control
for i, tier in enumerate(tiers):
    ax = axes[i]
    for suffix in ['', '_control']:
        label = tier + suffix
        data = monthly_profit[monthly_profit['label'] == label]
        ax.plot(data['month'], data['accumlative_profit'], label=label)

    ax.axvline(x=event_date, color='red', linestyle='--', linewidth=2)
    ax.set_title(f'{tier} vs {tier}_control')
    ax.legend()
    ax.grid(True)

# Global labels
fig.text(0.5, 0.04, 'Month', ha='center')
fig.text(0.04, 0.5, 'Accumulative Profit', va='center', rotation='vertical')

plt.tight_layout(rect=[0.05, 0.05, 1, 1])  # Leave space for global labels
plt.show()
