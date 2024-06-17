from pathlib import Path
path=Path('D:/python_STUDY/python/module-class-demo/file-demo/programming.txt')
contents="I love programming.\n"
contents+="I love creating new games.\n"
contents+="I love making apps.\n"
path.write_text(contents)