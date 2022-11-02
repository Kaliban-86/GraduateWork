import os
import pydicom
import numpy

# записываем в переменную путь к файлам
dir = 'to_read_DICOM'

# смотрим список файлов в директории с файлами DICOM
file_list = os.listdir(dir)

# выводим длинну списка файлов
print(len(file_list))

# выводим первый элемен
print(file_list[0])

# загружаем первый файл для изучения и смотрим его тип
ds = pydicom.read_file(f'{dir}/{file_list[0]}')
print(type(ds))

print(ds)
print(ds.Modality)