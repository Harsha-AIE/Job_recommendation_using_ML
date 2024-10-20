# preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(df):
    # Handle missing data
    df = df.dropna()

    # Encode categorical variables
    le = LabelEncoder()
    df['Job Title'] = le.fit_transform(df['Job Title'])

    # Feature scaling
    scaler = StandardScaler()
    df[['Job Title']] = scaler.fit_transform(df[['Job Title']])

    return df
