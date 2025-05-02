import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("first_touch.csv") 

df['month'] = pd.to_datetime(df['month'])

# Pivot the data
pivot_df = df.pivot_table(index='month', columns='first_touch_channel', values='revenue', aggfunc='sum')

# Sort by month
pivot_df = pivot_df.sort_index()

# Plot
pivot_df.plot()
plt.title("Monthly Revenue by First Touch Channel")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.legend(title="Channel")
plt.xticks(rotation=45)
plt.show()