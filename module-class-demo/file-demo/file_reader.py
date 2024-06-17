from pathlib import Path

path = Path('D:/python_STUDY/python/module-class-demo/file-demo/pi_digits.txt')
contents = path.read_text()
lines=contents.splitlines()
pi_line=""
for line in lines:
    pi_line+=line.strip()

print(pi_line)
print(len(pi_line))