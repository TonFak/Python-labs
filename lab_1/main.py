from pathlib import Path
import shutil
folder = input()
files = list(Path(folder).glob("*"))
if len(files) > 0:
    cnt = 0
    for i in range(len(files)):
        if (not files[i].is_dir()) and (files[i].stat().st_size < 2048):
            print(files[i].name)
            cnt += 1
    if cnt > 0:
        Path('small').mkdir(exist_ok=True)
    for i in range(len(files)):
        if (not files[i].is_dir()) and (files[i].stat().st_size < 2048):
            path_file = Path(folder + '/' + files[i].name)
            to_small_file = Path('small')
            shutil.copy(path_file, to_small_file)
else:
    print('Файлы не найдены')