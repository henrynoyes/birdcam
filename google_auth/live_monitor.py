import os
import time
import requests
import logging
from pathlib import Path
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('monitor.log', mode='w'),
    ]
)

class YouTubeLivestreamMonitor:
    YOUTUBE_API_BASE = 'https://www.googleapis.com/youtube/v3'
    auth_dir = Path(__file__).resolve().parent
    
    def __init__(self, credentials_file=(auth_dir / 'channel.json'), check_time_min=10):
        self.CREDENTIALS_FILE = credentials_file
        self.channel_id, self.api_key = self._load_credentials()

        self.check_time_min = check_time_min
    
    def _load_credentials(self):
        with open(self.CREDENTIALS_FILE, 'r') as f:
            creds = json.load(f)
        
        return creds['channel_id'], creds['api_key']
    
    def check_status(self):
        url = f'{self.YOUTUBE_API_BASE}/search'
        params = {
            'part': 'snippet',
            'channelId': self.channel_id,
            'eventType': 'live',
            'type': 'video',
            'key': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('items', []):
                titles = [stream['snippet']['title'] for stream in data['items']]
                logging.info(f"Channel is live with {len(titles)} streams: {' | '.join(titles)}")
                return True
            else:
                logging.info("Channel is not live")
                return False

        except Exception as e:
            logging.error(f"Error checking livestream status: {e}")
            return False
    
    def start_monitoring(self):
        logging.info(f"Monitoring started. Checking every {self.check_time_min} minutes")
        
        try:
            while True:
                is_live = self.check_status()
                
                if not is_live:
                    logging.info("System rebooting...")
                    os.system('/sbin/shutdown -r now')
                
                time.sleep(self.check_time_min * 60)
                
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user")
        except Exception as e:
            logging.error(f"Monitoring stopped due to error: {e}")

if __name__ == '__main__':
    monitor = YouTubeLivestreamMonitor()
    monitor.start_monitoring()