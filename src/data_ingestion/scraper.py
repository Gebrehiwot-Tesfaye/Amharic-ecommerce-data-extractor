import configparser
import json
from telethon.sync import TelegramClient
from telethon.tl.types import Channel

async def fetch_messages(client, channel_name, limit=1000):
    """Fetches messages from a single Telegram channel."""
    messages_data = []
    try:
        entity = await client.get_entity(channel_name)
        if isinstance(entity, Channel):
            print(f"Fetching messages from {channel_name}...")
            async for message in client.iter_messages(entity, limit=limit):
                if message.text:
                    messages_data.append({
                        'channel': channel_name,
                        'message_id': message.id,
                        'text': message.text,
                        'date': message.date.isoformat()
                    })
    except Exception as e:
        print(f"Could not fetch messages from {channel_name}: {e}")
    return messages_data

def run_scraper():
    """Main function to run the scraper for all channels."""
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_id = config['TELEGRAM']['API_ID']
    api_hash = config['TELEGRAM']['API_HASH']
    channels = [c.strip() for c in config['TELEGRAM']['CHANNELS'].split(',')]
    output_file = config['FILES']['RAW_DATA']

    with TelegramClient('anon', api_id, api_hash) as client:
        all_messages = []
        for channel in channels:
            messages = client.loop.run_until_complete(fetch_messages(client, channel))
            all_messages.extend(messages)

        with open(output_file, 'w', encoding='utf-8') as f:
            for msg in all_messages:
                f.write(json.dumps(msg, ensure_ascii=False) + '\n')
        print(f"Scraping complete. Saved {len(all_messages)} messages to {output_file}")

if __name__ == '__main__':
    run_scraper()