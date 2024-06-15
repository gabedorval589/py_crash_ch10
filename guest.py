"""
1. Ask for names
2. Collect names
3. Write collection to a file, one name per line
"""
from pathlib import Path

while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")

  name = input ("Name: ")
  if name == 'q':
    break
  else:
    path = Path('guest_book.txt')
    path.write_text(name)
