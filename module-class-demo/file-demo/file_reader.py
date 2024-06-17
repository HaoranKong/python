from pathlib import Path


path=Path('file-demo/pi_digits.txt')
contents=path.read_text()
print(contents)