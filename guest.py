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
