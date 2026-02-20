import re
import math

from config import data_lang

import config as cfg

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
            score += -15
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
        
        """"""
        if bool(re.search(r"\d", password)):
            score += 10
            messages.append(message_box["numbers"])
        
        else:
            score += -2.5 
            messages.append(message_box["not numbers"])


        text = [score, messages]

        return text
    

    def check_in_popular_password(self, password: str) -> list:
        """"""
        message_box = data_lang["second-check"]

        score = 0
        messages = []

        common_pass = cfg.common_password

        for i in common_pass:
            if (password.lower()) == (i.lower()):
                score += -100
                messages.append(message_box["check-false"])
                break

        for i in common_pass:
            if score <= -100:
                break

            elif (i.lower() in password.lower()) and (len(i) > 3):
                score -= 50
                messages.append((str(message_box["check-maybe"]).replace("<password>", f"{i}")))
                break
        
        if score >= 0:
            score += 50
            messages.append(message_box["check-true"])


        text = [score, messages]

        return text

    
    def check_entropy(self, password: str) -> int:
        number_bits = 0

        alphabet = 0

        alphabet_dictionaries = {
            r"[A-Z]": 26,
            r"[a-z]": 26,
            r"[А-Я]": 33,
            r"[а-я]": 33,
            r"[!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]": 40,
            r"\d": 10
        }

        for i in alphabet_dictionaries.keys():
            if bool(re.search(i, password)):
                alphabet += int(alphabet_dictionaries[str(i)])

        if alphabet <= 0: alphabet = 1


        number_bits = len(password) * math.log2(alphabet)

        return round(number_bits, 2)


#password = str(input("Password: "))


"""
test = Checked()
m1 = test.check_length_and_complexity(password)
#m1 = test.check_in_popular_password(password)
score = m1[0]
messages = m1[1]

print(f"Score: {score}\n\n")

for i in messages:
    print(f"Messages: {i}\n")
"""
