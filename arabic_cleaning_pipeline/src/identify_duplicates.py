import pandas as pd

def handle_duplicates_and_missing(df, text_column='sentences', min_words=3):
    df = df.dropna(subset=[text_column])
    
    # Drop rows with empty strings after stripping
    df[text_column] = df[text_column].astype(str).str.strip()
    df = df[df[text_column] != '']
    
    # Word count filtering
    df['word_count'] = df[text_column].apply(lambda x: len(str(x).split()))
    df = df[df['word_count'] >= min_words]

    # Drop duplicate rows based on text
    before = len(df)
    df = df.drop_duplicates(subset=text_column)
    after = len(df)
    
    print(f"Removed {before - after} duplicate rows. Final count: {after}")
    return df.drop(columns=['word_count'])
