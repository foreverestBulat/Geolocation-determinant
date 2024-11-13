# import asyncio
# from fastapi import Depends
# import requests
import pandas

# from persistence import get_db
# from services import DataPullingService

df = pandas.read_csv('src/temp/tmp.csv')
print(len(df))


# db = get_db()
# asyncio.run(db.drop())
# service: DataPullingService = Depends(DataPullingService)

# print(type(service))

# url = 'https://raw.githubusercontent.com/sapics/ip-location-db/refs/heads/main/geolite2-geo-whois-asn-country/geolite2-geo-whois-asn-country-ipv4.csv'

# name = url.split('/').pop()

# df = pandas.read_csv(url)

# for index, row in df.iterrows():
#     # print(row['1.0.0.0'])
#     # print(row['AU'])
    
#     for column in df.columns:
#         print(f'{column}: {row[column]}')
#     print()

# 42540548375379353601446927518702501888,
# 42540548454607516115711265112246452223,JP

# 42540551544505854172020431260460515328,
# 42540551623734016686284768854004465663,KR

# response = requests.get(url)

# with open(f'temp/{name}', 'wb') as f:
#     f.write(response.content)


# # if response.status_code == 200:
#     # df = pandas.read_csv(response.content)
#     print(df)
# else:
#     print(f"Ошибка: {response.status_code}")

# pandas.read_csv(f'temp/{name}')

    

# a = 's/ad/asdfew'

# print(a.split('/').pop())


# from apscheduler.schedulers.background import BackgroundScheduler
# import time
# import datetime

# def my_job():
#   # Ваш код, который нужно выполнять каждые час
#     print('Completed')
#     now = datetime.datetime.now()
#     print(f"Задачa выполнена в {now.hour}:{now.minute}:{now.second}")

# scheduler = BackgroundScheduler()
# scheduler.add_job(my_job, 'interval', seconds=5)
# scheduler.start()

# # Остановка планировщика через 5 секунд
# scheduler.shutdown(wait=15)

# print('?')
# time.sleep(20)
# print('end')



# import os
# import requests

# url = 'https://raw.githubusercontent.com/sapics/ip-location-db/refs/heads/main/geolite2-geo-whois-asn-country/geolite2-geo-whois-asn-country-ipv4.csv'
# response = requests.get(url)

# print(os.getcwd())
# with open('temp/tmp.csv', 'wb') as f:
#     f.write(response.content)
    # print(f.readlines())
    # for line in f.readlines()[:10]:
    #     print(line)



# import os
# from git import Repo


# os.makedirs('temp_repo', exist_ok=True)
# repo = Repo.clone_from('https://github.com/sapics/ip-location-db.git', 'temp_repo')




# from git import Repo

# # Укажите URL репозитория
# repo_url = 'https://github.com/sapics/ip-location-db'
# # repo_url = 'https://github.com/sapics/ip-location-db/tree/main/asn-country'
# # repo_url = 'https - FORBIDDEN - github - FORBIDDEN - /username/repository.git'

# folder_name = 'tree/main/temp_repo'


# # repo = Repo.clone_from(repo_url, 'local_folder')



# # Заменяем эти значения на ваши данные
# target_folder = "asn-country" # имя папки, где лежат CSV файлы
# branch = "main"

# # Клонируем репозиторий
# repo = Repo.clone_from(repo_url, 'temp_repo')

# # Переключаемся на нужную ветку
# repo.git.checkout(branch)

# # Получаем все CSV файлы из указанной папки
# csv_files = [
#     file.path
#     for file in repo.tree(f"{target_folder}")
#     if file.name.endswith(".csv")
# ]

# # Выводим список CSV файлов
# print("Найденные CSV файлы:")
# for file in csv_files:
#     print(f"- {file}")


# csv_files = []
# repo = Repo.clone_from(repo_url, "temp_repo")
# for item in repo.tree().traverse():
#     if item.type == "blob" and item.name.endswith(".csv"):
#         csv_files.append(f"{repo_url}/tree/main/{item.path}") 

# print(csv_files)

