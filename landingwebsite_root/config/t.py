import os
from dotenv import load_dotenv

load_dotenv(override=True)
SECRET_KEY = os.environ.get('secret')
print(SECRET_KEY)
