FROM nikolaik/python-nodejs:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code
COPY ./containers/local_settings.py.tpl /code/containers/local_settings.py
RUN ls -lah
# Install our requirements.
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["/code/start.sh"]:
