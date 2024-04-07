
FROM python:3.12.2
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
ENV DJANGO_SETTINGS_MODULE=events.settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/venv/
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

