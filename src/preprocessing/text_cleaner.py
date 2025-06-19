import re
import pandas as pd
import json
import configparser

def clean_text(text):
    """
    Cleans Amharic text by removing URLs, user mentions, and unwanted characters,
    while preserving essential punctuation and Amharic script.
    """
    if not isinstance(text, str):
        return ""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove user @mentions
    text = re.sub(r'\@\w+', '', text)
    # Remove characters that are not Amharic, numbers, or basic punctuation
    # This keeps Amharic characters (U+1200 to U+137F), numbers, and some punctuation.
    text = re.sub(r'[^\u1200-\u137F\s\d.,!?።]', '', text)
    # Normalize whitespace to a single space
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_raw_data():
    """
    Loads raw data, cleans it, and saves it to a processed file.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    raw_file = config['FILES']['RAW_DATA']
    processed_file = config['FILES']['PROCESSED_DATA']

    messages = []
    with open(raw_file, 'r', encoding='utf-8') as f:
        for line in f:
            messages.append(json.loads(line))

    if not messages:
        print("No messages found in raw data file. Exiting.")
        return

    df = pd.DataFrame(messages)
    print(f"Loaded {len(df)} messages from {raw_file}.")

    # Apply the cleaning function
    df['cleaned_text'] = df['text'].apply(clean_text)

    # Keep only rows where cleaned_text is not empty
    df = df[df['cleaned_text'] != '']

    # Save to CSV
    df.to_csv(processed_file, index=False, encoding='utf-8')
    print(f"Preprocessing complete. Saved {len(df)} cleaned messages to {processed_file}.")
    print("\nSample of processed data:")
    print(df[['text', 'cleaned_text']].head())

if __name__ == '__main__':
    preprocess_raw_data()