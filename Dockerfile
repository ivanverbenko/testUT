FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /site
COPY . /site/
WORKDIR /site

RUN pip install --upgrade pip
RUN pip install django
RUN pip install django-debug-toolbar

RUN python manage.py migrate
RUN python manage.py loaddata data.json
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]