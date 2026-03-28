import pandas as pd
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <input_file>")
        sys.exit(1)

    in_path = sys.argv[1]


    try:
        if in_path.endswith(".xlsx"):
            df = pd.read_excel(in_path)
        else:
            
            try:
                df = pd.read_csv(in_path, encoding="utf-8")
            except UnicodeDecodeError:
                print("⚠️ UTF-8 failed, retrying with ISO-8859-1 encoding...")
                df = pd.read_csv(in_path, encoding="ISO-8859-1")
    except Exception as e:
        print(f" Failed to load {in_path}: {e}")
        sys.exit(1)

    print(" Data loaded successfully!")
    print(df.head())

    out_dir = "/app/pipeline/results"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "data_raw.csv")
    df.to_csv(out_path, index=False)
    print(f" Saved raw data to {out_path}")

    
    os.system(f"python preprocess.py {in_path}")

if __name__ == "__main__":
    main()
