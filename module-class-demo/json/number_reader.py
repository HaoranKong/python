from pathlib import Path
import json 

path=Path('D:/python_STUDY/python/module-class-demo/json/numbers.json')
contents=path.read_text()
numbers=json.loads(contents)

print(numbers)