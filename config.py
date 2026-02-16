import json

with open(r"config\config.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with open(r"config\language\RU-ru.json", "r", encoding="utf-8") as file:
    data_lang = json.load(file)

with open(r"config\common-password\100k-most-used-passwords-NCSC.txt", "r", encoding="utf-8") as file:
    _common_pass = file.read()


common_password = list()

for i in _common_pass.split("\n"):
    common_password.append(i)