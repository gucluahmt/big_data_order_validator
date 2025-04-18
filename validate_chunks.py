import pandas as pd
import os

base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, 'order_data.csv')
output_path = os.path.join(base_dir, 'invalid_orders.csv')

chunksize = 200000
error_rows = []

for chunk in pd.read_csv(input_path, chunksize=chunksize):
    invalid = chunk[chunk['amount'] <= 0]
    if not invalid.empty:
        error_rows.append(invalid)

if error_rows:
    result = pd.concat(error_rows)
    result.to_csv(output_path, index=False)
    print(f"{len(result)} invalid records found and saved to → {output_path}")
else:
    print("All records are valid. No issues detected.")

