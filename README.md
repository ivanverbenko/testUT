# Тестовое задание UT

## Техническое задание
Ссылка на ТЗ: [Техническое задание](https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit?usp=sharing)

Проект разработан с использованием Django. Для тестирования количества SQL запросов к базе данных использовался `django-debug-toolbar`.
## Запуск докера с готовой базой


```bash
docker build . --tag test_up
docker run -p 8000:8000 test_up
http://localhost:8000/
admin 1:1
```