# preprocess.py
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

def main():
    if len(sys.argv) < 2:
        print("Usage: python preprocess.py <input_excel_file>")
        sys.exit(1)

    in_path = sys.argv[1]

    
    print(f"📘 Loading dataset: {in_path}")
    df = pd.read_excel(in_path)
    print("Data loaded successfully")
    print(df.head())

    

    df_means = df.loc[:, 'id':'fractal_dimension_mean']
    print(" Selected mean columns")
    print(df_means.head())



    
    print("🔍 Checking missing values before imputation:")
    print(df_means.isnull().sum())

    
    imputer = SimpleImputer(strategy='mean')
    numeric_cols = df_means.select_dtypes(include=np.number).columns
    df_means[numeric_cols] = imputer.fit_transform(df_means[numeric_cols])

    
    if 'texture_mean' in df_means.columns:
        df_means['texture_mean'] = df_means['texture_mean'].fillna(df_means['texture_mean'].mean())
    if 'smoothness_mean' in df_means.columns:
        df_means['smoothness_mean'] = df_means['smoothness_mean'].fillna(df_means['smoothness_mean'].median())
    if 'symmetry_mean' in df_means.columns:
        df_means['symmetry_mean'] = df_means['symmetry_mean'].fillna(df_means['symmetry_mean'].median())

    print("Missing values handled successfully")

    
    before = df_means.shape[0]
    df_means.drop_duplicates(inplace=True)
    after = df_means.shape[0]
    print(f"🧹 Removed {before - after} duplicate rows")


    new_labels = []
    for col in df_means.columns:
        if '_mean' in col:
            new_labels.append(col.replace('_mean', ''))
        else:
            new_labels.append(col)
    df_means.columns = new_labels
    print(" Renamed columns to remove '_mean' suffix")

    
    if 'id' in df_means.columns:
        df_means.drop('id', axis=1, inplace=True)
    print(" Dropped 'id' column")

    
    print(" Final dataset description:")
    print(df_means.describe())

    
    out_dir = "/app/pipeline/results"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "data_preprocessed.csv")
    df_means.to_csv(out_path, index=False)
    print(f" Saved cleaned data to {out_path}")

    

    
    os.system(f"python analytics.py {out_path}")

if __name__ == "__main__":
    main()
