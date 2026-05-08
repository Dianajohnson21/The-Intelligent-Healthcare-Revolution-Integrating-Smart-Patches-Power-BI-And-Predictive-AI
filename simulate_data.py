import pandas as pd
import numpy as np

# Generate 1000 rows of synthetic patch data
data = {
    'timestamp': pd.date_range(start='2026-01-01', periods=1000, freq='T'),
    'heart_rate': np.random.normal(75, 10, 1000),
    'glucose_mg_dL': np.random.normal(100, 15, 1000),
    'wound_inflammation_index': np.random.uniform(0, 1, 1000)
}
df = pd.DataFrame(data)
# Save to CSV
df.to_csv('patch_data.csv', index=False)
print("success: patch_data.csv has been created!")

