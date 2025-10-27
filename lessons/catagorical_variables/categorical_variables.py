import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Example data
data = {
    'color': ['red', 'blue', 'green', 'red', 'blue'],
    'size': ['small', 'medium', 'large', 'small', 'large']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n")

# Label Encoding
label_encoder = LabelEncoder()
df['color_encoded'] = label_encoder.fit_transform(df['color'])
df['size_encoded'] = label_encoder.fit_transform(df['size'])
print("After Label Encoding:")
print(df)
print("\n")

# One-Hot Encoding
onehot = pd.get_dummies(df[['color', 'size']], prefix=['color', 'size'])
print("After One-Hot Encoding:")
print(onehot)