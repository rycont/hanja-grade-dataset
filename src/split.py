# 1. read `hanja.csv` file
# 2. split file by `level` column
# 3. write each split to a new CSV file with the name `{level}.csv`

import pandas as pd

# Read the CSV file

path = 'hanja.csv'
df = pd.read_csv(path)

# Split the DataFrame by level

level_groups = df.groupby('level')

# Write each split to a new CSV file

for level, group in level_groups:
    group.to_csv(f'{level}.csv', index=False)
