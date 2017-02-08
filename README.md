# My Python home server on Raspberry Pi
Мой домашний сервер на мини-компьютере Raspberry Pi, который я пишу на питоне.
Пока ещё полезных функций в нём нет.

Как начинать новый проект
-------------------------
Тут же опишу, как создать структуру директорий и окружение чтобы начать новый проект на питоне. Используем Python, virtualenv и Flask.  
Установить virtualenv, если его не было  
`$ sudo pip install virtualenv`

Создаём папку проекта и виртуальное окружение  
`$ mkdir myproject`  
`$ cd myproject`  
`$ virtualenv venv`  
`New python executable in venv/bin/python`  
`Installing setuptools, pip............done.`

В дальнейшем перед началом работы выполнить `$ . venv/bin/activate`, а для окончания работы `$ deactivate`.

Теперь устанавливаем Flask  
`$ . venv/bin/activate`  
`$ pip install Flask`  
Если IntelliJ IDEA не увидела Flask - это её проблемы. Идём в настройки проекта Project Structure и выбираем в качестве Project SDK питон из виртуального окружения.

Для начала создаём следующую базовую структуру папок:  
`myapp/static` - картинки, js, css  
`myapp/templates` - шаблоны страниц  
`myapp/__init__.py` - скрипт инициализации приложения  
`myapp/views.py` - простейшая функция представления  
`run.py` - скрипт запуска
