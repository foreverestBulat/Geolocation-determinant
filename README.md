# Определитель геолокации
## Описание
Определяет геолокацию по запросу по ip каждый час

## Docker
- `docker compose build`
- `docker compose up`
- `http://0.0.0.0:8000`

## Настройка проекта
.env
```
DB_USER = "bulat"
DB_PASSWORD = "bulat"
DB_NAME = "save_ip"
DB_HOST = "localhost"
DB_PORT = 27017
```

Если у вас ошибка с подключением у MongoDB
```
pymongo.errors.OperationFailure: Authentication failed., full error: {'ok': 0.0, 'errmsg': 'Authentication failed.', 'code': 18, 'codeName': 'AuthenticationFailed'}
``` 
то может быть вам не нужно указывать user и пароль, поэтому измените MONGODB_URL в config.py на строку ниже
```
MONGODB_URL = f'mongodb://{MONGODB['HOST']}:{MONGODB['PORT']}'
```

Если вы хотите больше файлов для закачки в базу данных то добавьте ссылки csv файлов в CSV_FILES_URLS в config.py. К примеру:
```
CSV_FILES_URLS = [
'https://raw.githubusercontent.com/sapics/ip-location-db/refs/heads/main/asn-country/asn-country-ipv6.csv', 'https://raw.githubusercontent.com/sapics/ip-location-db/refs/heads/main/geolite2-geo-whois-asn-country/geolite2-geo-whois-asn-country-ipv4.csv'
]
```
ТАКЖЕ в main.py в строке 15 уберите значение 1000, чтобы было `await service.pulling_task()`, это ограничение сколько строк записать в бд

