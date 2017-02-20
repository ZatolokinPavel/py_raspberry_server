# My Python home server on Raspberry Pi
Мой домашний сервер на мини-компьютере Raspberry Pi, который я пишу на питоне.
Пока ещё полезных функций в нём нет.

Запуск проекта
--------------
`$ cd myproject`  
`$ . venv/bin/activate`  
`$ ./run.py`  
После этого web-интерфейс приложения будет доступен по адресу http://127.0.0.1:8739/


Как начинать новый проект (общая инструкция)
--------------------------------------------
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
`$ pip install flask-wtf` (расширение для работы с формами)  
`$ pip install sqlalchemy` (расширение для работы с базами SQL)  
`$ pip install flask-sqlalchemy` (обёртка для SQLAlchemy под Flask)  
`$ pip install sqlalchemy-migrate` (автоматические миграции для базы данных)  
Если IntelliJ IDEA не увидела Flask - это её проблемы. Идём в настройки проекта Project Structure и выбираем в качестве Project SDK питон из виртуального окружения.

Для начала создаём следующую базовую структуру папок:  
`app/static` - картинки, js, css  
`app/templates` - шаблоны страниц  
`app/__init__.py` - скрипт инициализации приложения  
`app/views.py` - простейшая функция представления  
`run.py` - скрипт запуска (сделать его исполняемым)
