FROM tiangolo/uwsgi-nginx-flask:python3.8

# Install pyton dependencies
COPY ./requirements.txt /app/requirements.txt
RUN  pip install -r /app/requirements.txt

# Install application
COPY ./app /app/app
COPY ./api /app/api
COPY ./static /app/static
COPY ./main.py /app/main.py
