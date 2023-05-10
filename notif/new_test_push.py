from pushover import Pushover
from pathlib import Path
app_key = Path('app_key.txt').read_text()
user_key = Path('user_key.txt').read_text()


po = Pushover(app_key)
with open('/Users/henrynoyes/birdcam/static/living_room.jpg', 'rb') as bin:
    po.message(user=user_key, title='Testing new push', message='test', attachment=bin)
print('sent')