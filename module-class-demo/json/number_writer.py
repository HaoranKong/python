from pathlib import Path
import json

numbers=[2,3,5,7,11,13] 
path=Path('D:/python_STUDY/python/module-class-demo/json/numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)