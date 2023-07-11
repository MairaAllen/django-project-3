from django.test import TestCase

# ТИПЫ ПОЛЕЙ БД
# BigIntegerField - большое числовое поле
# Виджет этого поля - TextInput

# BooleanField - поле истина\ложь
# виджет - CheckInput

# Charfield
# Виджет - TextInput
# обязательный аргумент : max_length

# TextField - Большое текстовое поле
# Виджет - Textarea

# DateField -поле даты

# 2 атрибута:
# auto_now = True -сохранение новой даты при любом сохранении модели
# то есть дата будет внесена при вызове Model.save()

# auto_now_add = True сохранение новой даты только при создании экземпляра
# виджет - Input type=date


# DataTameField - поле даты и времени
# Виджет - input type=datetime

# EmailField - поле почты
# проверяет валидность адреса почты через EmailValidator

# FileField - поле файла
# ImageField - поле изображения

# оба поля имеют необязательный аргумент - upload_to - директория загружаемых с сервера файлов

# ПОЛЯ ЧИСЕЛ
# IntegerField - 
# PositiveIntegerField
# SmallPositiveIntegerField

# ПОЛЯ СВЯЗИ
# ForeignKey (один-ко-многим)
# ManyToManyField(многие-ко-многим)
# OneToOneField(щдин-к-одному)

# class Meta
# db_table - для переименования таблицы модели
# verbose_name - для переименования модели
# verbose_name_plural - для переименования модели (мн.ч.)

