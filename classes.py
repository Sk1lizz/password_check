import re

from config import data_lang

"""
text = "dffF"
print(bool(re.search(r"[A-Z]", text)))"""

class Checked:
    """"""

    def check_length_and_complexity(self, password: str) -> list:
        """"""

        message_box = data_lang["first-check"]

        score = 0
        messages = []

        """Оценка длины пароля"""
        if len(password) >= 8:
            score += 10
            messages.append(message_box["len-8"])

            if len(password) >= 15:
                score += 5
                messages.append(message_box["len-15"])
        
        else:
            score += -5
            messages.append(message_box["len-7"])


        """Поиск заглавных букв"""
        if bool(re.search(r"[A-Z]", password)) or bool(re.search(r"[А-Я]", password)):
            score += 5
            messages.append(message_box["A-Z"])
        
        else:
            score += -2.5 
            messages.append(message_box["not A-Z"])
        

        """Поиск прописных букв"""
        if bool(re.search(r"[a-z]", password)) or bool(re.search(r"[а-я]", password)):
            score += 5
            messages.append(message_box["a-z"])
        
        else:
            score += -2.5 
            messages.append(message_box["not a-z"])

        """Поиск спецсимволов"""
        if bool(re.search(r"[!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", password)):
            score += 10
            messages.append(message_box["Special Character"])
        
        else:
            score += -5 
            messages.append(message_box["not Special Character"])


        text = [score, messages]

        return text

password = input("Password: ")

test = Checked()
m1 = test.check_length_and_complexity(password)
score = m1[0]
messages = m1[1]

print(f"Score: {score}\n\n")

for i in messages:
    print(f"Messages: {i}\n")
