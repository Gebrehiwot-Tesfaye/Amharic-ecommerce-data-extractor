import pandas as pd
import re

def extract_product_and_price(text):
    # Simple rule-based extraction (replace with your model for real use)
    # Example: look for numbers as price, and known product keywords
    product_keywords = ['ጫማ', 'ልብስ', 'ባልሸምበት', 'ሻንጣ', 'የሴቶች', 'የልጆች']
    price_pattern = r'(\d{2,6})\s*ብር?'

    # Product extraction
    product = next((kw for kw in product_keywords if kw in text), None)

    # Price extraction
    price_match = re.search(price_pattern, text)
    price = price_match.group(1) if price_match else None

    return product, price

def main():
    # Load preprocessed messages
    df = pd.read_csv('data/processed/preprocessed_messages.csv')

    # Prepare output columns
    output_rows = []
    for _, row in df.iterrows():
        text = row['text']
        product, price = extract_product_and_price(str(text))
        output_rows.append({
            'vendor': row['channel'],  # or 'vendor' if you prefer
            'timestamp': row['date'],
            'views': row['view_count'],
            'text': text,
            'product': product,
            'price': price
        })

    out_df = pd.DataFrame(output_rows)
    out_df.to_csv('data/vendor_posts_with_ner.csv', index=False)
    print("✅ Saved NER-annotated posts to data/vendor_posts_with_ner.csv")

if __name__ == "__main__":
    main()
