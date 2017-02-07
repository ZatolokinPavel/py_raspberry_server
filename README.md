# My Python home server on Raspberry Pi
Мой домашний сервер на мини-компьютере Raspberry Pi, который я пишу на питоне.
Пока ещё полезных функций в нём нет.

Как начинать новый проект
-------------------------
Тут же опишу, как создать структуру директорий и окружение чтобы начать новый проект на питоне. Используем Flask, virtualenv.  
Установить virtualenv, если его не было  
`$ sudo pip install virtualenv`

Создаём папку проекта и виртуальное окружение  
`$ mkdir myproject`  
`$ cd myproject`  
`$ virtualenv venv`  
`New python executable in venv/bin/python`  
`Installing setuptools, pip............done.`

В дальнейшем перед началом работы выполнить `$ . venv/bin/activate`, а для окончания работы `$ deactivate`.

Теперь устанавливаем flask  
`$ . venv/bin/activate`  
`$ pip install Flask`

И создаём следующую структуру папок:  
`app/static` - картинки, js, css  
`app/templates` - шаблоны страниц  
`app/__init__.py` - скрипт инициализации приложения  
`app/views.py` - простейшая функция представления  
`run.py` - скрипт запуска
