'''
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени
добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать
только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

from pathlib import Path


def files_rename(path: Path, numbers_qnt: int, ext: str,
                 new_ext: str, start: int, end: int, new_name: str = '') -> None:
    counter = 1
    if path.exists():
        for obj in path.iterdir():
            if obj.is_file():
                file_ext = obj.suffix
                if file_ext == ext:
                    new_file_name = obj.stem[start:end] + new_name + f'{counter:0>{numbers_qnt}}' + new_ext
                    obj.rename(new_file_name)
                    counter += 1


if __name__ == '__main__':
    files_rename(Path(r'C:\Users\77017\PycharmProjects\python_data_hw_7\test\images'), 5, ".jpg", ".jpeg", 3, 8,
                 new_name="NEW_FILE")
