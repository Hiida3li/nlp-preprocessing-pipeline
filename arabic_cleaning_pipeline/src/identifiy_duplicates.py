import pandas as pd
import os

df = pd.read_csv("arabic_cleaning_pipeline/data/raw/raw_data.csv")

before = len(df)
df = df.drop_duplicates(subset='sentences', keep='first')
after = len(df)

os.makedirs("data/deduplicated", exist_ok=True)
df.to_csv("data/deduplicated/raw_data_deduped.csv", index=False)

print(f"Removed {before - after} duplicates. Remaining rows: {after}")
