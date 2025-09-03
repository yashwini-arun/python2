import pandas as pd
import numpy as np

data = {
    'Player': ['P1', 'P2', 'P3'],
    'Goals': [10, 5, 7],
    'Assists': [8, 12, 6],
    'Matches': [15, 18, 14]
}
df = pd.DataFrame(data)


weights = np.array([0.5, 0.3, 0.2])
df['Performance'] = np.dot(df[['Goals','Assists','Matches']], weights)

best_player = df.loc[df['Performance'].idxmax(), 'Player']
print("Player Performance:\n", df, "\nBest Player:", best_player)
