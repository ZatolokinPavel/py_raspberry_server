#coding: utf-8
__author__ = 'Zatolokin Pavel'

BASE_URL = '/py_back'                   # начало для всех uri приложения

CSRF_ENABLED = True                     # защита от межсайтовых поддельных запросов
SECRET_KEY = '56fv4df56v41df56v1s859'   # ключ для этой защиты. Используется для динамической генерации секретного ключа скрытого поля формы.
