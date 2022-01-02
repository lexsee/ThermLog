import os

KEYDICT = {".":","}
file_path = None

def DateToNum(filename):
    with open(filename, "r") as f:
        file = f.read()
        for key in KEYDICT:
            value = KEYDICT[key]
            file = file.replace(key, value)
        return file

def WriteFile(file,item):
    with open(file, "w") as ff:
        ff.write(item)

def main(file_path):
    file_list = os.listdir(file_path)
    for file in file_list:
        if file.endswith(".xls"):
            try:
                item = DateToNum(file)
                WriteFile(file,item)
                print(f"\nФайл '{file}' исправлен!")
            except Exception as err:
                print(f"\nОшибка! Файл '{file}' не исправлен!"
                      f"\n{err}"
                      f"\nЗакройте файл '{file}' и попробуйте запустить программу ещё раз.")

main(file_path)
input("\n\nНажмите Enter для выхода из программы. ")
