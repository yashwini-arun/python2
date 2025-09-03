import pandas as pd
import numpy as np

data = {
    'Student': ['S1', 'S2', 'S3'],
    'Math': [85, 70, 90],
    'Science': [78, 88, 82],
    'English': [92, 76, 85]
}
df = pd.DataFrame(data)


weights = np.array([0.4, 0.3, 0.3])
df['GPA'] = np.dot(df[['Math', 'Science', 'English']], weights) / 20

print("Student GPA Data:\n", df)
