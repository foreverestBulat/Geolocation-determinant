import pandas
from motor.motor_asyncio import AsyncIOMotorCollection


class DataPullingService:
    def __init__(self, db: AsyncIOMotorCollection):
        self.urls_csv = ['https://raw.githubusercontent.com/sapics/ip-location-db/refs/heads/main/geolite2-geo-whois-asn-country/geolite2-geo-whois-asn-country-ipv4.csv']
        self.db = db
    
    async def pulling_task(self):
        print('start task')
        for url in self.urls_csv:
            df = pandas.read_csv(url)
            for index, row in df.iterrows():
                start = row[df.columns[0]]
                end = row[df.columns[1]]
                country_code = row[df.columns[2]]

                existing_document = await self.db.find_one({'start': start, 'end': end})

                if existing_document:
                    await self.db.update_one(
                        {'start': start, 'end': end},
                        {'$set': {'country_code': country_code}}
                    )
                else:
                    await self.db.insert_one({
                        'start': start,
                        'end': end,
                        'country_code': country_code
                    })