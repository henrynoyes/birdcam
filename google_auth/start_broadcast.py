import json
from datetime import datetime, timedelta, timezone
from requests_oauthlib import OAuth2Session
import logging
from pathlib import Path

logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('broadcast.log', mode='w'),
            ]
        )

class YouTubeLivestream:
    YOUTUBE_API_BASE = 'https://www.googleapis.com/youtube/v3'
    auth_dir = Path(__file__).resolve().parent
    
    def __init__(self, credentials_file=(auth_dir / 'credentials.json'), token_file=(auth_dir / 'token.json')):
        self.CREDENTIALS_FILE = credentials_file
        self.TOKEN_FILE = token_file
        
        self.credentials, self.token = self._load_credentials()
        
        self.session = OAuth2Session(
            self.credentials['client_id'],
            token=self.token,
            auto_refresh_url=self.credentials['token_uri'],
            auto_refresh_kwargs={
                'client_id': self.credentials['client_id'],
                'client_secret': self.credentials['client_secret']
            },
            token_updater=lambda token: self._save_token(token)
        )
    
    def _load_credentials(self):
        with open(self.CREDENTIALS_FILE, 'r') as f:
            credentials = json.load(f)['web']
        
        with open(self.TOKEN_FILE, 'r') as f:
            token = json.load(f)
        
        return credentials, token
    
    def _save_token(self, token):
        logging.info('Saving new token')
        token['refresh_token'] = self.token['refresh_token']
        with open(self.TOKEN_FILE, 'w') as f:
            json.dump(token, f)
        self.token = token
    
    def youtube_post(self, endpoint, data=None, params=None):
        url = f'{self.YOUTUBE_API_BASE}/{endpoint}'

        try:
            response = self.session.post(url, json=data, params=params)
            response.raise_for_status()
        except:
            logging.info('Token expired, refreshing...')
            new_token = self.session.refresh_token(
                self.credentials['token_uri'],
                refresh_token=self.token['refresh_token']
            )
            self._save_token(new_token)
            response = self.session.post(url, json=data, params=params)
            response.raise_for_status()
            
        return response.json()
    
    def initialize_livestream(self):
        curr_date = datetime.now().strftime("%m/%d/%Y")
        title = f'BirdCam {curr_date}'
        description = f'Livestream start: {datetime.now().strftime("%A, %B %d, %Y %H:%M:%S")}'
        start_time = (datetime.now(timezone.utc) + timedelta(seconds=10)).strftime('%Y-%m-%dT%H:%M:%S')
        
        # create broadcast
        broadcast = self.youtube_post(
            'liveBroadcasts',
            data={
                'snippet': {
                    'title': title,
                    'description': description,
                    'scheduledStartTime': start_time
                },
                'status': {
                    'privacyStatus': 'public',
                    'selfDeclaredMadeForKids': False
                },
                'contentDetails': {
                    'enableAutoStart': True,
                    'enableAutoStop': True
                }
            },
            params={'part': 'snippet,status,contentDetails'}
        )
        
        # create stream
        stream = self.youtube_post(
            'liveStreams',
            data={
                'snippet': {'title': title},
                'cdn': {
                    'frameRate': 'variable',
                    'ingestionType': 'rtmp',
                    'resolution': 'variable'
                }
            },
            params={'part': 'snippet,cdn'}
        )
        
        # bind
        self.youtube_post(
            'liveBroadcasts/bind',
            params={
                'id': broadcast['id'],
                'streamId': stream['id'],
                'part': 'id'
            }
        )
        
        ingestion_info = stream['cdn']['ingestionInfo']
        rtmp_url = f'{ingestion_info["ingestionAddress"]}/{ingestion_info["streamName"]}'
        
        return rtmp_url

if __name__ == '__main__':
    logging.info('Creating YouTube livestream...')
    youtube = YouTubeLivestream()
    rtmp_url = youtube.initialize_livestream()
    print(rtmp_url)
    