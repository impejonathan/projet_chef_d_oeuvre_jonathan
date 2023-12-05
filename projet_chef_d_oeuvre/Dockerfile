FROM  python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]

CMD ["gunicorn", "-c", "gunicorn.conf.py", "projet_chef_d_oeuvre.wsgi:application"]


## docker run -p 80:80  -v C:\Users\impej\Documents\BRIEF\projet_chef_d_oeuvre_jonathan\projet_chef_d_oeuvre:/app livre
## docker build -t livre .