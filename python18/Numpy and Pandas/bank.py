import pandas as pd
import numpy as np

data = {
    'Customer': ['A', 'B', 'C', 'D'],
    'Balance': [10000, 25000, 15000, 5000]
}
df = pd.DataFrame(data)


rates = np.random.uniform(0.02, 0.06, len(df))
df['InterestRate'] = np.round(rates, 3)


df['InterestEarned'] = df['Balance'] * df['InterestRate']


df['NewBalance'] = df['Balance'] + df['InterestEarned']

print("Bank Customer Interest Data:\n", df)
