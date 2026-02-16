import re

text = "1qwertyQWERTY"

print(bool(re.search(r"[!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", text)))