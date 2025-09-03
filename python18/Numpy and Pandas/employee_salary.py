import pandas as pd
import numpy as np

data = {
    'Employee': ['E1', 'E2', 'E3', 'E4'],
    'Dept': ['IT', 'HR', 'Sales', 'IT'],
    'Salary': [50000, 40000, 60000, 55000]
}
df = pd.DataFrame(data)


bonus = np.random.randint(5, 15, len(df))
df['Bonus%'] = bonus
df['NewSalary'] = df['Salary'] * (1 + df['Bonus%']/100)


dept_avg = df.groupby('Dept')['NewSalary'].mean()

print("Salary Data:\n", df, "\nDept Avg:\n", dept_avg)
