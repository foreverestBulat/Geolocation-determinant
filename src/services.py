from motor.motor_asyncio import AsyncIOMotorCollection
import pandas
import ipaddress
from config import CSV_FILES_URLS


class DataPullingService:
    def __init__(self, db: AsyncIOMotorCollection):
        self.urls_csv = CSV_FILES_URLS
        self.db = db
    
    def ip_to_int_array(ip_address):
        try:
            ip = ipaddress.ip_address(ip_address)
        except ValueError:
            raise ValueError("Неверный IP адрес.")

        if isinstance(ip, ipaddress.IPv4Address):
            return [int(x) for x in ip.packed]
        elif isinstance(ip, ipaddress.IPv6Address):
            return list(ip.packed)
        else:
            raise ValueError("Неподдерживаемый тип IP адреса.")
    
    async def read_and_fill(self, url, n = 0):
        df = pandas.read_csv(url)
        print(url)
        for index, row in df.iterrows():
            start = row[df.columns[0]]
            end = row[df.columns[1]]
            country_code = row[df.columns[2]]

            existing_document = await self.db.find_one(
                {
                    'start': DataPullingService.ip_to_int_array(start),
                    'end': DataPullingService.ip_to_int_array(end)
                }
            )

            if existing_document:
                await self.db.update_one(
                    {
                        'start': DataPullingService.ip_to_int_array(start),
                        'end': DataPullingService.ip_to_int_array(end)
                    },
                    {
                        '$set': 
                        {
                            'country_code': country_code
                        }
                    }
                )
            else:
                await self.db.insert_one(
                {
                    'start': DataPullingService.ip_to_int_array(start),
                    'end': DataPullingService.ip_to_int_array(end),
                    'country_code': country_code
                })
            if n != 0 and index == n:
                break
    
    async def pulling_task(self, count_rows_loaded = 0):
        print('Start Pulling Service')
        for url in self.urls_csv:
            await self.read_and_fill(url, count_rows_loaded)
                
                
    async def fill_data_from_uploaded(self, n=0):
        path = 'src/csv/ipv4.csv'
        await self.read_and_fill(path, n)
        
        path = 'src/csv/ipv6.csv'
        await self.read_and_fill(path, n)