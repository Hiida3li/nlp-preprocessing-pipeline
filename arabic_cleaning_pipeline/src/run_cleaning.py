# run_cleaning.py
import pandas as pd
from clean_pipeline import clean_text, count_words

# Load raw data
df = pd.read_csv("your_input_file.csv")  # Replace with actual file path

# ✅ Step 1: Remove exact duplicates (before cleaning)
before = len(df)
df = df.drop_duplicates(subset='sentences', keep='first')
after = len(df)
print(f"🧹 Removed {before - after} exact duplicate rows before cleaning.")

# Step 2: Clean the text
df['sentences'] = df['sentences'].apply(clean_text)

# Step 3: Word count
df['word_count'] = df['sentences'].apply(count_words)

# Step 4: Filter out short or empty messages
df = df[df['word_count'] >= 3]
df = df[df['sentences'].str.strip() != '']

# Step 5 (optional): Remove post-cleaning duplicates again (if needed)
cleaned_before = len(df)
df = df.drop_duplicates(subset='sentences', keep='first')
cleaned_after = len(df)
if cleaned_before != cleaned_after:
    print(f"🧹 Removed {cleaned_before - cleaned_after} duplicate rows after cleaning.")

# Save final output
df[['sentences']].to_csv("civil_pii_cleaned_deduplicated.csv", index=False)

# Show random sample
print(f"✅ Final number of rows: {len(df)}")
print(df[['sentences']].sample(min(5, len(df))))
