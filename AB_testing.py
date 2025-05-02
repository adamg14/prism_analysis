import pandas as pd
import matplotlib.pyplot as plt

ab_test = pd.read_csv('./A_B_Test.csv')

ab_test['month'] = pd.to_datetime(ab_test['month'])
ab_test = ab_test.sort_values(by=['label', 'month'])

for label in ['control', 'test']:
    ab_test_plot = ab_test[ab_test['label'] == label]
    plt.plot(ab_test_plot['month'], ab_test_plot['accumulative_revenue'], label=label)

event_date = pd.to_datetime('2024-01-02')        # ← change to your date
plt.axvline(x=event_date,
            color='red',                         # line color
            linestyle='--',                      # dashed style
            linewidth=2,                      
            )
plt.legend()   
plt.show()
