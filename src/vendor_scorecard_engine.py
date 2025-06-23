import pandas as pd
import numpy as np
from tabulate import tabulate

# Example: Load your processed data
# df = pd.read_csv('data/vendor_posts_with_ner.csv')

CHANNELS = ['helloomarketethiopia', 'HuluMar', 'guzomart', 'gareeodaa', 'huluorder']

def vendor_scorecard(df):
    results = []
    for vendor in CHANNELS:
        vendor_df = df[df['vendor'] == vendor].copy()
        if vendor_df.empty:
            continue

        # Ensure timestamp is datetime
        vendor_df['timestamp'] = pd.to_datetime(vendor_df['timestamp'])

        # Posting Frequency (posts per week)
        weeks = (vendor_df['timestamp'].max() - vendor_df['timestamp'].min()).days / 7
        weeks = max(weeks, 1)  # Avoid division by zero
        posts_per_week = vendor_df.shape[0] / weeks

        # Average Views per Post
        avg_views = vendor_df['views'].mean()

        # Top Performing Post
        top_post = vendor_df.loc[vendor_df['views'].idxmax()]
        top_product = top_post['product'] if pd.notnull(top_post['product']) else 'N/A'
        top_price = top_post['price'] if pd.notnull(top_post['price']) else 'N/A'

        # Average Price Point (exclude missing)
        prices = pd.to_numeric(vendor_df['price'], errors='coerce')
        avg_price = prices[prices.notnull()].mean() if not prices.dropna().empty else 'N/A'

        # Lending Score (customizable)
        lending_score = (avg_views * 0.5) + (posts_per_week * 0.5)

        results.append({
            'Vendor': vendor,
            'Avg. Views/Post': round(avg_views, 1),
            'Posts/Week': round(posts_per_week, 2),
            'Avg. Price (ETB)': round(avg_price, 1) if avg_price != 'N/A' else 'N/A',
            'Lending Score': round(lending_score, 1),
            'Top Product (Best Post)': top_product,
            'Top Price (Best Post)': top_price
        })
    return pd.DataFrame(results)

if __name__ == "__main__":
    df = pd.read_csv('data/vendor_posts_with_ner.csv')
    scorecard_df = vendor_scorecard(df)
    # Print pretty table in terminal
    print(tabulate(scorecard_df, headers='keys', tablefmt='psql', showindex=False))
    # Save as CSV for real tabular data
    scorecard_df.to_csv('data/vendor_scorecard.csv', index=False)
    print("\n✅ Scorecard saved as data/vendor_scorecard.csv")

# Example usage:
# scorecard_df = vendor_scorecard(df)
# print(scorecard_df.to_markdown(index=False))