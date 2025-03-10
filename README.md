# My Django Project

## Описание
Этот проект создан на Django. Он включает:
- Админку `/admin/`
- Главную страницу `/`
- Разделы `/about/`, `/contact/` и т. д.

## Установка
1. **Клонировать репозиторий**  
   ```sh
   git clone https://github.com/username/myproject.git
   cd myproject


# Django Project

## Описание

Простое Django-приложение с тремя страницами: Главная, О нас, Контакты.

### Структура кода

1. Главный urls.py (корень проекта)

Подключает маршруты:

admin/ для админки

'' (пустой путь) для приложения pages

2. urls.py в приложении pages

Определяет маршруты:

/ → home.html

/about/ → about.html

/contact/ → contact.html

3. views.py (представления)

Функции home, about, contact рендерят соответствующие шаблоны.

4. Шаблоны (templates/pages/)

home.html, about.html, contact.html содержат HTML-код страниц.

5. admin.py

Регистрирует модель ContactMessage для отображения в админке.

6. Настройки Django (settings.py)

APP_DIRS=True позволяет искать шаблоны в templates/ приложений.
