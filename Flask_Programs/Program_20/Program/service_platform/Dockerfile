FROM python:3.6.0 as backend
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock

RUN pip install  -i https://mirrors.aliyun.com/pypi/simple --upgrade pip==18.0  pipenv ; pipenv install --pypi-mirror https://mirrors.aliyun.com/pypi/simple && python3_link=$(which python3) && rm $python3_link && ln -s $(pipenv --py) $python3_link

COPY . /usr/src/app

#RUN pipenv run pyinstaller --upx-dir=/usr/src/app/contrib/deploy --onefile app.spec
#CMD ["ui api adapter worker"]
CMD ["python3", "app/app_runner.py"]

