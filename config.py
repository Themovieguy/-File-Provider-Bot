# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
      
# Owner Information
API_ID = int(environ.get("API_ID", "21586527"))
API_HASH = environ.get("API_HASH", "e0681e3ff584cac71897edd1251044f0")
ADMINS = int(environ.get("ADMINS", "1465125082"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://moviehouse0143new:pPZjf3pY6UaqHizi@cluster0.if2nnf3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "clonevjbotz")
DB_URI = environ.get("DB_URI", "mongodb+srv://contactthemovieguy:t9Nd0WQgNjjuYJZq@file-provider-bot.yp7zjba.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "vjbotz")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "6560235734:AAEFva5VtBmlnEpaQqfFW3uKcsDsFRcU_cA")
BOT_USERNAME = environ.get("BOT_USERNAME", "TheMovieGuyFileProvider_bot") # your bot username without @
PICS = (environ.get('PICS', 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfD7oa_JNyvm16jgskbmqNXXvHdyQQU5W2YQxXckxxpw_Moh4hpMrWaERAxRaBe0C_JyMWOogUxOLjCyQCeg1d52vw9aP0bkTH0l192-vbBZ-TetNA03v6MgKiPDHASbx4KSmbpPParAdhX6AN7waV4v9VJUnfdiCPAmo8hyGL-1XSorJRc8F5upnPZMQm/s1600/20240220_142447.png https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfD7oa_JNyvm16jgskbmqNXXvHdyQQU5W2YQxXckxxpw_Moh4hpMrWaERAxRaBe0C_JyMWOogUxOLjCyQCeg1d52vw9aP0bkTH0l192-vbBZ-TetNA03v6MgKiPDHASbx4KSmbpPParAdhX6AN7waV4v9VJUnfdiCPAmo8hyGL-1XSorJRc8F5upnPZMQm/s1600/20240220_142447.png')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "5")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "300")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002095019285"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002069903570')).split()]

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002095019285'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://the-movie-guy-stream-moviehouse.koyeb.app/"
    else:
        URL = "https://the-movie-guy-stream-moviehouse.koyeb.app/"
    
