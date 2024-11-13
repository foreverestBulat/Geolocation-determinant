import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "MongoDB": {
        "NAME": os.environ.get("DB_NAME", "save_ip"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", 27017)
    }
}

MONGODB = DATABASES['MongoDB']
MONGODB_URL = f'mongodb://{MONGODB['HOST']}:{MONGODB['PORT']}'

CSV_FILES_URLS = ['https://raw.githubusercontent.com/sapics/ip-location-db/refs/heads/main/geolite2-geo-whois-asn-country/geolite2-geo-whois-asn-country-ipv4.csv']