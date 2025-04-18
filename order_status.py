import pandas as pd
import numpy as np
import os

# Define file path
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, 'order_data.csv')
output_path = os.path.join(base_dir, 'labeled_orders.csv')

# Read data (you can test 100K row )
df = pd.read_csv(input_path, nrows=100000)

# Classification process (Executed = 1, others = 0)
df['status_flag'] = np.where(df['status'] == 'Executed', 1, 0)

# Write to output file
df.to_csv(output_path, index=False)

print(f"Labeled data succesfully saved", "{output_path}")
