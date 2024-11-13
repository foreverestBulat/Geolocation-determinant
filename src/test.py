import os
from git import Repo


# os.makedirs('temp_repo', exist_ok=True)
repo = Repo.clone_from('https://github.com/sapics/ip-location-db.git', 'temp_repo')




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

