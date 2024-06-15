from pathlib import Path

name = input("Name: ")

path = Path('guest.txt')
path.write_text(name)
