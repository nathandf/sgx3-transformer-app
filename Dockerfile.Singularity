FROM python:3.9

RUN mkdir sgx3-transformer-app

COPY requirements.txt /sgx3-transformer-app/requirements.txt

RUN pip3 install -r /sgx3-transformer-app/requirements.txt

COPY main.py /sgx3-transformer-app/main.py

ENTRYPOINT [ "python", "/sgx3-transformer-app/main.py" ]