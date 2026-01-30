import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8351544302:AAFyAVDOz665T6LpycDYBKu0tsisqN-5U1E")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29777466"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a04b3df726520026f207079aec2f9879")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8399557684"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://girnarimaharaj01_db_user:KsxBY4eoUBwRKXXw@cluster0.6firafk.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "girnarimaharaj01_db_user")

