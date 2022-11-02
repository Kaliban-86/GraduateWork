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

# выводим информацию из файла
print(ds)

# получаем доступ к конкртеной характеристике
print(ds.PatientOrientation)

#  смотрим размер файла если перевести в массив пикселей
print(ds.pixel_array.shape)

# можно посмотреть список открытых ключей (первые пять) и их количество
print(ds.dir()[:5], len(ds.dir()))

# переводим в массив numpy и проверяем тип и размер
dicom_array = numpy.array(ds.pixel_array)
print(type(dicom_array), dicom_array.shape)
