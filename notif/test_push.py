from pushover import Pushover
from pathlib import Path
from datetime import datetime, time
app_key = Path('app_key.txt').read_text()
user_key = Path('user_key.txt').read_text()
ts = datetime.now().strftime('%H:%M %p')

po = Pushover(app_key)
po.user(user_key)

msg = po.msg(f'Motion Detected at {ts}\nhttps://10.0.0.240:8000')

msg.set('title', 'BirdCam Alert!')

po.send(msg)
print('Sent!')