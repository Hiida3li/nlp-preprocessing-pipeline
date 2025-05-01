import pandas as pd
import os
from clean_pipeline import clean_text, count_words


df = pd.read_csv("data/raw/raw_data.csv")

# Remove all duplicates before cleaning
before = len(df)
df = df.drop_duplicates(subset='sentences', keep='first')
after = len(df)
print(f"Removed {before - after} exact duplicate rows before cleaning.")

df['sentences'] = df['sentences'].apply(clean_text)
df['word_count'] = df['sentences'].apply(count_words)

# Filter out short or empty messages
df = df[df['word_count'] >= 3]
df = df[df['sentences'].str.strip() != '']

# Remove post-cleaning duplicates again 
cleaned_before = len(df)
df = df.drop_duplicates(subset='sentences', keep='first')
cleaned_after = len(df)
if cleaned_before != cleaned_after:
    print(f"🧹 Removed {cleaned_before - cleaned_after} duplicate rows after cleaning.")

df[['sentences']].to_csv("civil_pii_cleaned_deduplicated.csv", index=False)

print(f"Final number of rows: {len(df)}")
print(df[['sentences']].sample(min(5, len(df))))
