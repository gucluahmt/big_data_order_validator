import pandas as pd
import numpy as np
import os

# Dosya yolu belirle
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, 'order_data.csv')
output_path = os.path.join(base_dir, 'labeled_orders.csv')

# Veriyi oku (ilk 100k satırla test edebilirsin)
df = pd.read_csv(input_path, nrows=100000)

# Sınıflandırma işlemi (Executed = 1, diğerleri = 0)
df['status_flag'] = np.where(df['status'] == 'Executed', 1, 0)

# Sonuç dosyasına yaz
df.to_csv(output_path, index=False)

print(f"Labeled veri başarıyla kaydedildi → {output_path}")
