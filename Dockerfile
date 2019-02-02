FROM nikolaik/python-nodejs:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pipenv install --system --deploy --ignore-pipfile
WORKDIR /code/js
RUN npm install
WORKDIR /code
COPY ./containers/local_settings.py.docker /code/containers/local_settings.py
CMD ["/code/start.sh"]:
