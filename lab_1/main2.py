from pathlib import Path
dir = input()
Path(dir).mkdir(exist_ok=True)
with open('artem3.txt') as file:
    line = list(file.read().split('\n'))[:-1]
    for i in range(len(line)):
        open(dir + '/' + line[i], 'w')
