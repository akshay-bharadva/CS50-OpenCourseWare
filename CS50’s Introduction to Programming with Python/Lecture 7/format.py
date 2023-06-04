import re

name = input("What's your name? ").strip()
# :=
# Operator ":=" requires Python 3.8 or newer
if matches := re.search(r"^(.+), ?(.+)$", name):
    last, first = matches.groups()
    name = f"{first} {last}"


print(f"Hello, {name}")
