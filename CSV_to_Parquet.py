import pandas as pd
from pathlib import Path
def main():
    data_dir = Path("data")
    csv_path = data_dir / "downloaded_data.csv"
    parquet_path = data_dir / "downloaded_data.parquet"

    print(f"Loading {csv_path} ...")
    df = pd.read_csv(csv_path)

    print(f"Saving as {parquet_path} ...")
    df.to_parquet(parquet_path, engine="pyarrow", index=False)

    print("Done! Parquet file created.")

if __name__ == "__main__":
    main()
