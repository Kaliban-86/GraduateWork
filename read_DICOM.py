import os
import pydicom
import numpy
import matplotlib.pyplot as plt

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
# print(ds)

# получаем доступ к конкртеной характеристике
print(ds.PatientOrientation)

#  смотрим размер файла если перевести в массив пикселей
print(ds.pixel_array.shape)

# можно посмотреть список открытых ключей (первые пять) и их количество
print(ds.dir()[:5], len(ds.dir()))

# переводим в массив numpy и проверяем тип и размер
dicom_array = numpy.array(ds.pixel_array)
print(type(dicom_array), dicom_array.shape)

# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# plt.show()

# В цикле проходимся по всем файлам в папке и в формате numpy загружаем в список
data_set_to_preproc = []

for dicom_file_name in file_list:
    ds = pydicom.read_file(f'{dir}/{dicom_file_name}')
    data_set_to_preproc.append(numpy.array(ds.pixel_array))

print(f'В списке {len(data_set_to_preproc)} файлов DICOM, размером {data_set_to_preproc[0].shape}', )

data_array_set_to_prepr = numpy.array(data_set_to_preproc)
print(data_array_set_to_prepr.shape)

plt.imshow(data_array_set_to_prepr[200])
plt.show()